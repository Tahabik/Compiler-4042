INFERRED_MARK = "<inferred>"

_PASSTHROUGH_TYPES = {
    "ReLU", "Sigmoid", "Tanh", "GELU", "Softmax", "LeakyReLU", "ELU", "Dropout",
}


def infer_missing_dims(model, diag):
    from semantic_analyzer import Literal, INT, SHAPE

    memo = {}
    inferred = []

    def get_int(node, name):
        lit = node.params.get(name)
        return lit.value if lit is not None and lit.type == INT else None

    def fill_or_check(node, pname, computed, as_shape=False):
        if computed is None:
            return
        lit = node.params.get(pname)
        if lit is None:
            value = (computed,) if as_shape else computed
            node.params[pname] = Literal(SHAPE if as_shape else INT, value, INFERRED_MARK)
            inferred.append((node.id, pname, computed))
            return
        declared = lit.value[-1] if lit.type == SHAPE else lit.value
        if isinstance(declared, int) and declared != computed:
            diag.error(
                f"Node '{node.id}' ({node.layer_type}) declares "
                f"'{pname}={declared}', but its predecessor(s) produce {computed}.",
                hint="Fix the declared parameter or the graph wiring.")

    def merge_shapes(node, shapes):
        known = [s for s in shapes if s is not None]
        if not known:
            return None
        first = known[0]
        for s in known[1:]:
            if s != first:
                diag.error(
                    f"Node '{node.id}' ({node.layer_type}) receives mismatched "
                    f"shapes {first} and {s} from different predecessors.")
                return None
        return first

    def runtime_dim_to_axis(dim, rank):
        axis = dim - 1 if dim >= 0 else dim
        idx = axis if axis >= 0 else rank + axis
        return idx if 0 <= idx < rank else None

    def conv_out(size, kernel, stride, padding):
        out = (size + 2 * padding - kernel) // stride + 1
        return out

    def h_linear(node, shapes):
        shape = merge_shapes(node, shapes)
        fill_or_check(node, "in_features", shape[-1] if shape else None)
        out_f = get_int(node, "out_features")
        if shape is None or out_f is None:
            return None
        return shape[:-1] + (out_f,)

    def h_conv(node, shapes, spatial_rank, has_padding):
        shape = merge_shapes(node, shapes)
        fill_or_check(node, "in_ch", shape[0] if shape else None)
        out_ch = get_int(node, "out_ch")
        kernel = get_int(node, "kernel")
        if shape is None or len(shape) != spatial_rank + 1 or out_ch is None or kernel is None:
            return None
        stride = get_int(node, "stride") or 1
        padding = (get_int(node, "padding") or 0) if has_padding else 0
        spatial = shape[1:]
        out_spatial = tuple(conv_out(s, kernel, stride, padding) for s in spatial)
        if any(s <= 0 for s in out_spatial):
            diag.error(
                f"Node '{node.id}' ({node.layer_type}) produces a non-positive "
                f"output size {out_spatial} from input shape {shape}.")
            return None
        return (out_ch,) + out_spatial

    def h_pool(node, shapes):
        shape = merge_shapes(node, shapes)
        if shape is None or len(shape) != 3:
            return None
        kernel = get_int(node, "kernel")
        if kernel is None:
            return None
        stride = get_int(node, "stride")
        if stride is None:
            stride = kernel  # matches nn.MaxPool2d/AvgPool2d's own default
        C, H, W = shape
        H2, W2 = conv_out(H, kernel, stride, 0), conv_out(W, kernel, stride, 0)
        if H2 <= 0 or W2 <= 0:
            diag.error(
                f"Node '{node.id}' ({node.layer_type}) produces a non-positive "
                f"output size ({H2}, {W2}) from input shape {shape}.")
            return None
        return (C, H2, W2)

    def h_batchnorm2d(node, shapes):
        shape = merge_shapes(node, shapes)
        fill_or_check(node, "num_features", shape[0] if shape else None)
        return shape

    def h_layernorm(node, shapes):
        shape = merge_shapes(node, shapes)
        fill_or_check(node, "normalized_shape", shape[-1] if shape else None, as_shape=True)
        return shape

    def h_flatten(node, shapes):
        shape = merge_shapes(node, shapes)
        if shape is None:
            return None
        rank = len(shape)
        start = get_int(node, "start_dim")
        end = get_int(node, "end_dim")
        start = 1 if start is None else start
        end = -1 if end is None else end
        s = start - 1 if start >= 0 else start
        e = end - 1 if end >= 0 else end
        s_idx = s if s >= 0 else rank + s
        e_idx = e if e >= 0 else rank + e
        if s_idx < 0 or e_idx >= rank or s_idx > e_idx:
            return None  # e.g. a start_dim=0 that reaches into the (untracked) batch axis
        merged = 1
        for d in shape[s_idx:e_idx + 1]:
            merged *= d
        return shape[:s_idx] + (merged,) + shape[e_idx + 1:]

    def h_embedding(node, shapes):
        shape = merge_shapes(node, shapes)
        emb = get_int(node, "embedding_dim")
        if shape is None or emb is None:
            return None
        return shape + (emb,)

    def h_rnn(node, shapes):
        shape = merge_shapes(node, shapes)
        fill_or_check(node, "input_size", shape[-1] if shape else None)
        hidden = get_int(node, "hidden_size")
        if shape is None or hidden is None:
            return None
        return shape[:-1] + (hidden,)

    def h_mha(node, shapes):
        shape = merge_shapes(node, shapes)
        fill_or_check(node, "embed_dim", shape[-1] if shape else None)
        return shape

    def h_passthrough(node, shapes):
        return merge_shapes(node, shapes)

    def h_concat(node, shapes):
        known = [s for s in shapes if s is not None]
        if not known:
            return None
        dim = get_int(node, "dim") or 0
        rank = len(known[0])
        idx = runtime_dim_to_axis(dim, rank)
        if idx is None:
            return None
        base, total = None, 0
        for s in known:
            if len(s) != rank:
                diag.error(
                    f"Node '{node.id}' (Concat) predecessors have shapes of "
                    f"different rank: {known}.")
                return None
            other = s[:idx] + s[idx + 1:]
            if base is None:
                base = other
            elif other != base:
                diag.error(
                    f"Node '{node.id}' (Concat, dim={dim}) predecessor shapes "
                    f"disagree outside the concatenated axis: {s} does not "
                    f"match the other branch(es)' non-concat shape {base}.")
                return None
            total += s[idx]
        if len(known) != len(shapes):
            return None  # can't total a dim across predecessors we haven't resolved yet
        result = list(known[0])
        result[idx] = total
        return tuple(result)

    def h_split(node, shapes):
        shape = merge_shapes(node, shapes)
        if shape is None:
            return None
        chunks = get_int(node, "chunks") or 2
        dim = get_int(node, "dim") or 0
        idx = runtime_dim_to_axis(dim, len(shape))
        if idx is None:
            return None
        size = shape[idx]
        if chunks == 0 or size % chunks != 0:
            diag.error(
                f"Node '{node.id}' (Split) dimension {dim} has size {size}, "
                f"not evenly divisible into {chunks} chunks.")
            return None
        result = list(shape)
        result[idx] = size // chunks
        return tuple(result)

    handlers = {
        "Linear": h_linear,
        "Conv2d": lambda n, s: h_conv(n, s, spatial_rank=2, has_padding=True),
        "Conv1d": lambda n, s: h_conv(n, s, spatial_rank=1, has_padding=False),
        "MaxPool2d": h_pool,
        "AvgPool2d": h_pool,
        "BatchNorm2d": h_batchnorm2d,
        "LayerNorm": h_layernorm,
        "Flatten": h_flatten,
        "Embedding": h_embedding,
        "LSTM": h_rnn,
        "GRU": h_rnn,
        "MultiHeadAttn": h_mha,
        "Add": h_passthrough,
        "Residual": h_passthrough,
        "Concat": h_concat,
        "Split": h_split,
    }
    for t in _PASSTHROUGH_TYPES:
        handlers[t] = h_passthrough

    def get_shape(node_id, visiting):
        if node_id in memo:
            return memo[node_id]
        if node_id in visiting:
            memo[node_id] = None
            return None
        visiting = visiting | {node_id}

        if node_id == model.input_id:
            shape = model.input_shape or None
            memo[node_id] = shape
            return shape

        node = model.nodes.get(node_id)
        if node is None:
            memo[node_id] = None
            return None

        pred_shapes = [get_shape(p, visiting) for p in node.in_edges]
        handler = handlers.get(node.layer_type)
        shape = handler(node, pred_shapes) if handler is not None else None
        memo[node_id] = shape
        return shape

    for node in model.nodes.values():
        get_shape(node.id, frozenset())

    for node_id, pname, dim in inferred:
        diag.info(f"Inferred '{pname}={dim}' for node '{node_id}' from its predecessor.")

    return inferred

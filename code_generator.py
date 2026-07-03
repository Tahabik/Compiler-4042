from collections import OrderedDict

from semantic_analyzer import Literal, SHAPE, BOOL, STRING, NONE

_POS, _KW = "pos", "kwarg"

LAYER_ARG_SPEC = {
    "Linear":        [("in_features", _KW, "in_features"), ("out_features", _KW, "out_features"), ("bias", _KW, "bias")],
    "Conv2d":        [("in_ch", _POS, None), ("out_ch", _POS, None), ("kernel", _KW, "kernel_size"), ("stride", _KW, "stride"), ("padding", _KW, "padding")],
    "Conv1d":        [("in_ch", _POS, None), ("out_ch", _POS, None), ("kernel", _KW, "kernel_size"), ("stride", _KW, "stride")],
    "BatchNorm2d":   [("num_features", _POS, None)],
    "LayerNorm":     [("normalized_shape", _POS, None)],
    "MaxPool2d":     [("kernel", _KW, "kernel_size"), ("stride", _KW, "stride")],
    "AvgPool2d":     [("kernel", _KW, "kernel_size"), ("stride", _KW, "stride")],
    "Dropout":       [("p", _KW, "p")],
    "Flatten":       [("start_dim", _KW, "start_dim"), ("end_dim", _KW, "end_dim")],
    "Embedding":     [("num_embeddings", _KW, "num_embeddings"), ("embedding_dim", _KW, "embedding_dim")],
    "MultiHeadAttn": [("embed_dim", _KW, "embed_dim"), ("num_heads", _KW, "num_heads")],
    "LSTM":          [("input_size", _KW, "input_size"), ("hidden_size", _KW, "hidden_size"), ("num_layers", _KW, "num_layers")],
    "GRU":           [("input_size", _KW, "input_size"), ("hidden_size", _KW, "hidden_size")],
    "ReLU": [], "Sigmoid": [], "Tanh": [], "GELU": [],
    "Softmax":       [("dim", _KW, "dim")],
    "LeakyReLU":     [("negative_slope", _KW, "negative_slope")],
    "ELU":           [("alpha", _KW, "alpha")],
}

PYTORCH_CLASS = {
    "Linear": "nn.Linear", "Conv2d": "nn.Conv2d", "Conv1d": "nn.Conv1d",
    "BatchNorm2d": "nn.BatchNorm2d", "LayerNorm": "nn.LayerNorm",
    "MaxPool2d": "nn.MaxPool2d", "AvgPool2d": "nn.AvgPool2d",
    "Dropout": "nn.Dropout", "Flatten": "nn.Flatten", "Embedding": "nn.Embedding",
    "MultiHeadAttn": "nn.MultiheadAttention", "LSTM": "nn.LSTM", "GRU": "nn.GRU",
    "ReLU": "nn.ReLU", "Sigmoid": "nn.Sigmoid", "Tanh": "nn.Tanh", "GELU": "nn.GELU",
    "Softmax": "nn.Softmax", "LeakyReLU": "nn.LeakyReLU", "ELU": "nn.ELU",
}

STRUCTURAL_OPS = {"Add", "Concat", "Residual", "Split"}
SEQUENCE_OPS = {"LSTM", "GRU"}


def _format_value(lit: Literal) -> str:
    if lit.type == SHAPE:
        dims = lit.value
        return str(dims[0]) if len(dims) == 1 else "(" + ", ".join(map(str, dims)) + ")"
    if lit.type == BOOL:
        return "True" if lit.value else "False"
    if lit.type == STRING:
        return repr(lit.value)
    if lit.type == NONE:
        return "None"
    return str(lit.value)


class CodeGenerator:

    def generate(self, model) -> str:
        self._prepare(model)
        lines = ["import torch", "import torch.nn as nn", "", ""]
        lines.append(f"class {model.name}(nn.Module):")
        lines.extend(self._gen_init(model))
        lines.append("")
        lines.extend(self._gen_forward(model))
        if model.config:
            lines.append("")
            lines.extend(self._gen_main(model))
        return "\n".join(lines) + "\n"

    def _prepare(self, model):
        self._out_edges_of = OrderedDict()
        for src, dst in model.edges:
            self._out_edges_of.setdefault(src, []).append(dst)

        residual_nodes = [n for n in model.nodes.values() if n.layer_type == "Residual"]
        self._residual_shortcut_of = {} # branch source id -> residual node id
        self._residual_main_of = {} # residual node id -> main-path pred id
        self._residual_identity_name = {} # residual node id -> snapshot var name
        for node in residual_nodes:
            shortcut, main = self._classify_residual(node)
            self._residual_shortcut_of[shortcut] = node.id
            self._residual_main_of[node.id] = main
            self._residual_identity_name[node.id] = ("identity" if len(residual_nodes) == 1 else f"identity_{node.id}")

        self._letter_idx = 0

    def _out_degree(self, node_id):
        return len(self._out_edges_of.get(node_id, []))

    def _classify_residual(self, node):
        p1, p2 = node.in_edges[0], node.in_edges[1]
        d1, d2 = self._out_degree(p1), self._out_degree(p2)
        if d1 > d2:
            return p1, p2 # shortcut, main
        if d2 > d1:
            return p2, p1
        return p2, p1

    def _needs_fresh_names(self, model, source_id):
        out_edges = self._out_edges_of.get(source_id, [])
        if len(out_edges) <= 1:
            return False
        real_count = 0
        for dst in out_edges:
            in_deg = len(model.nodes[dst].in_edges)
            if in_deg <= 1:
                real_count += 1
                continue
            is_covered_residual_shortcut = ( model.nodes[dst].layer_type == "Residual" and self._residual_shortcut_of.get(source_id) == dst)
            if not is_covered_residual_shortcut:
                return True
        return real_count >= 2

    def _next_letter(self):
        idx = self._letter_idx
        self._letter_idx += 1
        return chr(ord('a') + idx) if idx < 26 else f"br{idx}"


    def _gen_init(self, model):
        lines = ["    def __init__(self):", f"        super({model.name}, self).__init__()"]
        for node in model.nodes.values():
            if node.layer_type in STRUCTURAL_OPS:
                continue
            lines.append(f"        self.{node.id} = {self._format_ctor(node)}")
        return lines

    def _format_ctor(self, node):
        cls = PYTORCH_CLASS.get(node.layer_type, f"nn.{node.layer_type}")
        spec = LAYER_ARG_SPEC.get(node.layer_type)
        pos_args, kw_args = [], []
        if spec is None:
            for pname, lit in node.params.items():
                kw_args.append(f"{pname}={_format_value(lit)}")
        else:
            for dsl_name, mode, py_name in spec:
                if dsl_name not in node.params:
                    continue
                value = _format_value(node.params[dsl_name])
                if mode == _POS:
                    pos_args.append(value)
                else:
                    kw_args.append(f"{py_name}={value}")
        if node.layer_type == "MultiHeadAttn":
            kw_args.append("batch_first=True")
        return f"{cls}({', '.join(pos_args + kw_args)})"


    def _gen_forward(self, model):
        lines = [f"    def forward(self, {model.input_id}):"]
        var_of = {model.input_id: model.input_id}
        body = []

        pending_snapshots = OrderedDict()
        for source_id, residual_id in self._residual_shortcut_of.items():
            pending_snapshots.setdefault(source_id, []).append(residual_id)

        def emit_snapshots_for(source_id):
            for residual_id in pending_snapshots.get(source_id, []):
                name = self._residual_identity_name[residual_id]
                body.append(f"{name} = {var_of[source_id]}")

        emit_snapshots_for(model.input_id)

        for node_id in model.topo_order:
            if node_id == model.input_id:
                continue
            self._emit_node(model, model.nodes[node_id], var_of, body)
            emit_snapshots_for(node_id)

        lines.extend(f"        {line}" for line in body)
        lines.append(f"        return {var_of[model.output_id]}")
        return lines

    def _read_name(self, model, pred_id, var_of):
        if self._out_degree(pred_id) <= 1:
            return var_of[pred_id]
        if self._needs_fresh_names(model, pred_id):
            return self._next_letter()
        return var_of[pred_id]

    def _emit_node(self, model, node, var_of, body):
        preds = node.in_edges
        ltype = node.layer_type

        if ltype == "Residual":
            _, main_id = self._classify_residual(node)
            identity = self._residual_identity_name[node.id]
            body.append(f"x = {var_of[main_id]} + {identity}")
            var_of[node.id] = "x"
            return

        if ltype == "Add":
            body.append(f"x = {' + '.join(var_of[p] for p in preds)}")
            var_of[node.id] = "x"
            return

        if ltype == "Concat":
            dim = node.params["dim"].value if "dim" in node.params else 0
            items = ", ".join(var_of[p] for p in preds)
            body.append(f"x = torch.cat([{items}], dim={dim})")
            var_of[node.id] = "x"
            return

        if ltype == "Split":
            chunks = node.params["chunks"].value if "chunks" in node.params else 2
            dim = node.params["dim"].value if "dim" in node.params else 0
            body.append(f"parts = torch.chunk({var_of[preds[0]]}, {chunks}, dim={dim})")
            var_of[node.id] = "parts"
            return

        if len(preds) > 1:
            # A regular layer wired to multiple predecessors
            combined = " + ".join(var_of[p] for p in preds)
            body.append(f"x = self.{node.id}({combined})")
            var_of[node.id] = "x"
            return

        pred = preds[0]
        in_name = var_of[pred]
        out_name = self._read_name(model, pred, var_of)
        if ltype == "MultiHeadAttn":
            body.append(f"{out_name}, _ = self.{node.id}({in_name}, {in_name}, {in_name})")
        elif ltype in SEQUENCE_OPS:
            body.append(f"{out_name}, _ = self.{node.id}({in_name})")
        else:
            body.append(f"{out_name} = self.{node.id}({in_name})")
        var_of[node.id] = out_name


    def _gen_main(self, model):
        lines = ["if __name__ == '__main__':"]
        device_lit = model.config.get("device")
        batch_lit = model.config.get("batch_size")
        batch_size = batch_lit.value if batch_lit is not None else 1
        shape_args = ", ".join(str(d) for d in (batch_size,) + tuple(model.input_shape))
        if device_lit is not None:
            device_str = _format_value(device_lit)
            lines.append(f"    device = torch.device({device_str})")
            lines.append(f"    model = {model.name}().to(device)")
            lines.append(f"    {model.input_id} = torch.randn({shape_args}).to(device)")
        else:
            lines.append(f"    model = {model.name}()")
            lines.append(f"    {model.input_id} = torch.randn({shape_args})")
        lines.append(f"    print(model({model.input_id}).shape)")
        return lines

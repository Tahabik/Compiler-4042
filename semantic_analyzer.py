from collections import OrderedDict, defaultdict, deque

INT, FLOAT, BOOL, STRING, SHAPE, NONE, UNKNOWN = (
    "int", "float", "bool", "string", "shape", "None", "unknown",
)

_FLOATY = {FLOAT, INT}
_INTY = {INT}


LAYER_SPECS = {

    "Linear": {"in_features": _INTY, "out_features": _INTY, "bias": {BOOL}},
    "Conv2d": {"in_ch": _INTY, "out_ch": _INTY, "kernel": _INTY, "stride": _INTY, "padding": _INTY},
    "Conv1d": {"in_ch": _INTY, "out_ch": _INTY, "kernel": _INTY,"stride": _INTY},
    "BatchNorm2d": {"num_features": _INTY},
    "LayerNorm": {"normalized_shape": {SHAPE, INT}},
    "MaxPool2d": {"kernel": _INTY, "stride": _INTY},
    "AvgPool2d": {"kernel": _INTY, "stride": _INTY},
    "Dropout": {"p": _FLOATY},
    "Flatten": {"start_dim": _INTY, "end_dim": _INTY},
    "Embedding": {"num_embeddings": _INTY, "embedding_dim": _INTY},
    "MultiHeadAttn": {"embed_dim": _INTY, "num_heads": _INTY},
    "LSTM": {"input_size": _INTY, "hidden_size": _INTY, "num_layers": _INTY},
    "GRU": {"input_size": _INTY, "hidden_size": _INTY},

    "ReLU": {},
    "Sigmoid": {},
    "Tanh": {},
    "GELU": {},
    "Softmax": {"dim": _INTY},
    "LeakyReLU": {"negative_slope": _FLOATY},
    "ELU": {"alpha": _FLOATY},

    "Add": {},
    "Concat": {"dim": _INTY},
    "Residual": {},
    "Split": {"chunks": _INTY, "dim": _INTY},
}

MULTI_INPUT_OPS = {"Add", "Concat", "Residual"}


class Diagnostic:
    ERROR = "Error"
    WARNING = "Warning"

    def __init__(self, severity, message, hint=None):
        self.severity = severity
        self.message = message
        self.hint = hint

    def __str__(self):
        text = f"{self.severity}: {self.message}"
        if self.hint:
            text += f"\n    Hint: {self.hint}"
        return text


class Diagnostics:
    def __init__(self):
        self.items = []

    def error(self, message, hint=None):
        self.items.append(Diagnostic(Diagnostic.ERROR, message, hint))

    def warning(self, message, hint=None):
        self.items.append(Diagnostic(Diagnostic.WARNING, message, hint))

    def errors(self):
        return [d for d in self.items if d.severity == Diagnostic.ERROR]

    def warnings(self):
        return [d for d in self.items if d.severity == Diagnostic.WARNING]

    def has_errors(self):
        return any(d.severity == Diagnostic.ERROR for d in self.items)

    def __iter__(self):
        return iter(self.items)


class Literal:

    def __init__(self, type_tag, value, raw):
        self.type = type_tag # one of the type tags above
        self.value = value # (int/float/bool/str/tuple/None)
        self.raw = raw # original source text

    def __repr__(self):
        return f"Literal({self.type}, {self.value!r})"


class NodeInfo:
    def __init__(self, node_id, layer_type, params):
        self.id = node_id
        self.layer_type = layer_type
        self.params = params 
        self.in_edges = [] 
        self.out_edges = []


class SemanticModel:

    def __init__(self):
        self.name = None
        self.input_id = None
        self.input_shape = () 
        self.output_id = None
        self.nodes = OrderedDict()
        self.edges = []           
        self.config = OrderedDict()
        self.topo_order = []


class SemanticAnalyzer:
    def analyze(self, program_node):
        self.diag = Diagnostics()
        model = SemanticModel()

        if program_node is None or program_node.value != "program":
            self.diag.error("Malformed AST: expected a 'program' root node.")
            return model, self.diag

        model_node = _child(program_node, "model")
        graph_node = _child(program_node, "graph")
        config_node = _child(program_node, "config")

        if model_node is None or graph_node is None:
            self.diag.error("Program must contain both a 'model' and a 'graph' block.")
            return model, self.diag

        self._read_model(model_node, model)
        self._read_graph(graph_node, model)
        if config_node is not None:
            self._read_config(config_node, model)

        self._check_param_types(model)
        valid_ids = self._wire_edges(model)
        self._check_residual(model)
        self._check_orphans(model, valid_ids)
        self._check_acyclic_and_topo(model, valid_ids)
        self._check_reachability(model, valid_ids)

        return model, self.diag

    def _read_model(self, model_node, model):
        # children: [name_leaf, input_node, output_node]
        model.name = model_node.children[0].value if model_node.children else None

        input_node = _child(model_node, "input")
        if input_node is not None and input_node.children:
            model.input_id = input_node.children[0].value
            shape_node = input_node.children[1] if len(input_node.children) > 1 else None
            if shape_node is not None and shape_node.value == "shape":
                model.input_shape = tuple(int(d.value) for d in shape_node.children)
        else:
            self.diag.error("Model is missing an 'input' declaration.")

        output_node = _child(model_node, "output")
        if output_node is not None and output_node.children:
            model.output_id = output_node.children[0].value
        else:
            self.diag.error("Model is missing an 'output' declaration.")

    def _read_graph(self, graph_node, model):
        for child in graph_node.children:
            if child.value == "node":
                self._read_node(child, model)
            elif child.value == "edge":
                src = child.children[0].value
                dst = child.children[1].value
                model.edges.append((src, dst))

    def _read_node(self, node, model):
        node_id = node.children[0].value
        layer_type = node.children[1].value
        params_node = node.children[2] if len(node.children) > 2 else None

        params = OrderedDict()
        if params_node is not None and params_node.value == "params":
            for param in params_node.children:
                pname = param.children[0].value
                pval = _classify(param.children[1])
                if pname in params:
                    self.diag.error(
                        f"Duplicate parameter '{pname}' on node '{node_id}'.")
                params[pname] = pval

        if node_id in model.nodes:
            self.diag.error(f"Duplicate node id '{node_id}' in graph block.")
            return
        model.nodes[node_id] = NodeInfo(node_id, layer_type, params)

    def _read_config(self, config_node, model):
        for entry in config_node.children:
            key = entry.children[0].value
            model.config[key] = _classify(entry.children[1])

    def _check_param_types(self, model):
        for node in model.nodes.values():

            spec = LAYER_SPECS.get(node.layer_type)
            if spec is None:

                self.diag.error(
                    f"Node '{node.id}' uses unknown layer type "
                    f"'{node.layer_type}'.",
                    hint="Supported types: " + ", ".join(sorted(LAYER_SPECS)))
                
                continue

            for pname, lit in node.params.items():
                if pname not in spec:
                    self.diag.warning(
                        f"Node '{node.id}' ({node.layer_type}) has unexpected "
                        f"parameter '{pname}'.",
                        hint="Known parameters: "
                             + (", ".join(spec) if spec else "(none)"))
                    continue
                accepted = spec[pname]
                
                if lit.type not in accepted:
                    self.diag.error(
                        f"Parameter '{pname}' of {node.layer_type} expects "
                        f"{_or(accepted)}, got {lit.type} {lit.raw}.")

    def _wire_edges(self, model):
        valid_ids = set(model.nodes) | ({model.input_id} if model.input_id else set())

        if model.output_id is not None and model.output_id not in model.nodes:
            self.diag.error(
                f"Output node '{model.output_id}' is not declared in the graph.")

        for src, dst in model.edges:
            for endpoint in (src, dst):
                if endpoint not in valid_ids:
                    self.diag.error(
                        f"Edge references undefined node '{endpoint}'.",
                        hint="Declared ids are: ["
                             + ", ".join(valid_ids) + "]")
            if src in model.nodes:
                model.nodes[src].out_edges.append(dst)
            if dst in model.nodes:
                model.nodes[dst].in_edges.append(src)
        return valid_ids

    def _check_residual(self, model):
        for node in model.nodes.values():
            if node.layer_type == "Residual" and len(node.in_edges) != 2:
                self.diag.error(
                    f"Node '{node.id}' (Residual) has {len(node.in_edges)} "
                    f"incoming edges; expected exactly 2.")
            elif node.layer_type in ("Add", "Concat") and len(node.in_edges) < 2:
                self.diag.warning(
                    f"Node '{node.id}' ({node.layer_type}) has "
                    f"{len(node.in_edges)} incoming edge(s); expected 2 or more.")

    def _check_orphans(self, model, valid_ids):
        referenced = set()
        for src, dst in model.edges:
            referenced.add(src)
            referenced.add(dst)
        for node in model.nodes.values():
            if node.id == model.output_id:
                continue  # output is an endpoint by definition
            if node.id not in referenced:
                self.diag.warning(
                    f"Node '{node.id}' is declared but never referenced in any edge.")

    def _check_acyclic_and_topo(self, model, valid_ids):
        # Kahn's algorithm over input + graph nodes
        indegree = {nid: 0 for nid in valid_ids}
        adj = defaultdict(list)
        for src, dst in model.edges:
            if src in indegree and dst in indegree:
                adj[src].append(dst)
                indegree[dst] += 1

        queue = deque(sorted(n for n, d in indegree.items() if d == 0))
        order = []
        while queue:
            cur = queue.popleft()
            order.append(cur)
            for nxt in adj[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        if len(order) != len(indegree):
            remaining = [n for n in indegree if n not in set(order)]
            self.diag.error("Cycle detected involving nodes: " + ", ".join(sorted(remaining)) + ".",
                hint="NNGraph graphs must be acyclic DAGs.")
        else:
            model.topo_order = order

    def _check_reachability(self, model, valid_ids):
        if model.input_id is None:
            return
        adj = defaultdict(list)
        for src, dst in model.edges:
            adj[src].append(dst)

        seen = set()
        queue = deque([model.input_id])
        while queue:
            cur = queue.popleft()
            if cur in seen:
                continue
            seen.add(cur)
            queue.extend(adj[cur])

        for node in model.nodes.values():
            if node.id not in seen:
                self.diag.error(
                    f"Node '{node.id}' is not reachable from input "
                    f"'{model.input_id}'.")

        if model.output_id is not None and model.output_id not in seen:
            self.diag.error(
                f"Output node '{model.output_id}' is not reachable from input "
                f"'{model.input_id}'.")


def _child(node, value):
    for c in node.children:
        if c.value == value:
            return c
    return None


def _classify(value_node):
    if value_node.value == "shape":
        dims = tuple(int(d.value) for d in value_node.children)
        return Literal(SHAPE, dims, "(" + ", ".join(map(str, dims)) + ")")

    text = value_node.value
    if text == "true":
        return Literal(BOOL, True, text)
    if text == "false":
        return Literal(BOOL, False, text)
    if text == "None":
        return Literal(NONE, None, text)
    if len(text) >= 2 and text[0] == '"' and text[-1] == '"':
        return Literal(STRING, text[1:-1], text)
    try:
        return Literal(INT, int(text), text)
    except ValueError:
        pass
    try:
        return Literal(FLOAT, float(text), text)
    except ValueError:
        return Literal(UNKNOWN, text, text)


def _or(type_set):
    return " or ".join(sorted(type_set))

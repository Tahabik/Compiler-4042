from code_generator import _format_value, LAYER_ARG_SPEC
from shape_inference import INFERRED_MARK


def export_dot(model) -> str:
    lines = [
        f'digraph "{model.name or "NNGraph"}" {{',
        '    rankdir=LR;',
        '    node [shape=box, fontname="Helvetica", style=filled, fillcolor="#f5f5f5"];',
        '',
    ]

    if model.input_id:
        shape_str = ", ".join(str(d) for d in model.input_shape)
        lines.append(
            f'    {model.input_id} [shape=ellipse, fillcolor="#cfe8ff", '
            f'label="{_escape(model.input_id)}\\ntensor({shape_str})"];'
        )

    for node in model.nodes.values():
        label = f"{_escape(node.id)}\\n{_escape(node.layer_type)}({_escape(_format_params(node))})"
        attrs = f'label="{label}"'
        if node.id == model.output_id:
            attrs += ', peripheries=2, fillcolor="#ffe9b3"'
        lines.append(f'    {node.id} [{attrs}];')

    lines.append('')
    for src, dst in model.edges:
        edge_label = model.edge_labels.get((src, dst))
        if edge_label:
            lines.append(f'    {src} -> {dst} [label="{_escape(edge_label)}"];')
        else:
            lines.append(f'    {src} -> {dst};')

    lines.append('}')
    return "\n".join(lines) + "\n"


def _format_params(node):
    spec = LAYER_ARG_SPEC.get(node.layer_type)
    ordered_names = ([dsl_name for dsl_name, _, _ in spec] if spec is not None else list(node.params))
    remaining = [n for n in node.params if n not in ordered_names]

    parts = []
    for name in ordered_names + remaining:
        lit = node.params.get(name)
        if lit is None:
            continue
        text = f"{name}={_format_value(lit)}"
        if lit.raw == INFERRED_MARK:
            text += "*"  # marks a dimension the analyzer inferred, not one the user wrote
        parts.append(text)
    return ", ".join(parts)


def _escape(text):
    return text.replace("\\", "\\\\").replace('"', '\\"')

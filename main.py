import argparse
import sys

from custom_listener import build_ast
from semantic_analyzer import SemanticAnalyzer
from code_generator import CodeGenerator


def main(arguments):
    ast = build_ast(arguments.input)

    if arguments.show:
        from required_code_collection.ast_to_networkx_graph import show_ast
        show_ast(ast.root)

    if arguments.dump:
        print(ast.traverse_ast(ast.root))

    model, diagnostics = SemanticAnalyzer().analyze(ast.root)

    for diagnostic in diagnostics:
        print(diagnostic)

    if diagnostics.has_errors():
        print(f"\nSemantic analysis failed: {len(diagnostics.errors())} error(s).")
        return 1

    print(f"\nSemantic analysis passed for model '{model.name}'"
          f" ({len(diagnostics.warnings())} warning(s)).")

    code = CodeGenerator().generate(model)
    with open(arguments.output, 'w') as out:
        out.write(code)
    print(f"Generated PyTorch code written to '{arguments.output}'.")
    return 0


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description="NNGraph DSL compiler")
    argparser.add_argument('-i', '--input', help='Input .nng source',default=r'input/mlp.nng')
    argparser.add_argument('-o', '--output', help='Output .py path',default=r'output/mlp.py')
    argparser.add_argument('--show', action=argparse.BooleanOptionalAction,default=True,help='Render the AST (needs networkx/matplotlib/pydot)')
    argparser.add_argument('--dump', action='store_true',help='Print the post-order AST traversal')
    args = argparser.parse_args()
    sys.exit(main(args))

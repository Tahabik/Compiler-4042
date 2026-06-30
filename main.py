from antlr4 import *
import argparse
from custom_listener import CustomevmListener
from code_generator import CodeGenerator
from gen.evmTestLexer import evmTestLexer
from gen.evmTestParser import evmTestParser
from required_code_collection.ast_to_networkx_graph import show_ast


def main(arguments):
    stream = FileStream(arguments.input, encoding='utf8')
    lexer = evmTestLexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = evmTestParser(token_stream)
    parse_tree = parser.program()
    ast_builder_listener = CustomevmListener()
    ast_builder_listener.rule_names = parser.ruleNames
    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=ast_builder_listener)
    ast = ast_builder_listener.ast
    show_ast(ast.root)
    traversal = ast.traverse_ast(ast.root)
    print(traversal)
    code_gen = CodeGenerator()
    final_code = code_gen.generate(traversal)
    print(final_code)
    with open('evm_generator_output.txt','w') as evm_gen_out:
        evm_gen_out.write(final_code)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-i', '--input', help='Input source', default=r'input/test_switch_case.txt')
    # argparser.add_argument('-i', '--input', help='Input source', default=r'input/test_if_else.txt')
    argparser.add_argument('-o', '--output', help='Output path', default=r'output/test.evm-bytecode')
    args = argparser.parse_args()
    main(args)

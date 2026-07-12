from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

from gen.nngraphLexer import nngraphLexer
from gen.nngraphParser import nngraphParser
from gen.nngraphListener import nngraphListener
from required_code_collection.ast import AST
from required_code_collection.make_ast_subtree import make_ast_subtree


class CustomListener(nngraphListener):
    def __init__(self):
        self.ast = AST()


    def _keep_token(self, terminal):
        if terminal is not None:
            terminal.ast_value = self.ast.make_node(terminal.getText(), [])


    def exitProgram(self, ctx):
        # children: model, graph, (config?)
        make_ast_subtree(self.ast, ctx, "program", keep_node=True)


    def exitModelDecl(self, ctx):
        self._keep_token(ctx.IDENTIFIER())
        make_ast_subtree(self.ast, ctx, "model", keep_node=True)

    def exitModelItem(self, ctx):
        make_ast_subtree(self.ast, ctx, "modelItem")

    def exitInputDecl(self, ctx):
        self._keep_token(ctx.IDENTIFIER())
        make_ast_subtree(self.ast, ctx, "input", keep_node=True)

    def exitOutputDecl(self, ctx):
        self._keep_token(ctx.IDENTIFIER())
        make_ast_subtree(self.ast, ctx, "output", keep_node=True)


    def exitGraphDecl(self, ctx):
        make_ast_subtree(self.ast, ctx, "graph", keep_node=True)

    def exitGraphItem(self, ctx):
        make_ast_subtree(self.ast, ctx, "graphItem")

    def exitNodeDecl(self, ctx):
        self._keep_token(ctx.IDENTIFIER())
        # children become: id, layerType, (params?)
        make_ast_subtree(self.ast, ctx, "node", keep_node=True)

    def exitLayerType(self, ctx):
        # layerType : IDENTIFIER  -> leaf holding the layer name (e.g. "Linear")
        make_ast_subtree(self.ast, ctx, "layerType")

    def exitEdgeDecl(self, ctx):
        self._keep_token(ctx.IDENTIFIER(0)) # src
        self._keep_token(ctx.IDENTIFIER(1)) # dst
        make_ast_subtree(self.ast, ctx, "edge", keep_node=True)

    def exitEdgeLabel(self, ctx):
        self._keep_token(ctx.IDENTIFIER()) 
        self._keep_token(ctx.STRING())
        make_ast_subtree(self.ast, ctx, "label", keep_node=True)


    def exitConfigDecl(self, ctx):
        make_ast_subtree(self.ast, ctx, "config", keep_node=True)

    def exitConfigEntry(self, ctx):
        self._keep_token(ctx.IDENTIFIER())          # config key
        make_ast_subtree(self.ast, ctx, "config_entry", keep_node=True)


    def exitParamList(self, ctx):
        make_ast_subtree(self.ast, ctx, "params", keep_node=True)

    def exitParam(self, ctx):
        self._keep_token(ctx.IDENTIFIER()) 
        make_ast_subtree(self.ast, ctx, "param", keep_node=True)

    def exitValue(self, ctx):
        make_ast_subtree(self.ast, ctx, "value")

    def exitShape(self, ctx):
        dims = [self.ast.make_node(t.getText(), []) for t in ctx.INT()]
        ctx.ast_value = self.ast.make_node("shape", dims)
        self.ast.root = ctx.ast_value

    def exitNumber(self, ctx):
        ctx.ast_value = self.ast.make_node(ctx.getText(), [])
        self.ast.root = ctx.ast_value


def build_ast(path):
    input_stream = FileStream(path, encoding="utf-8")
    lexer = nngraphLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = nngraphParser(tokens)
    tree = parser.program()

    listener = CustomListener()
    ParseTreeWalker().walk(listener, tree)
    return listener.ast


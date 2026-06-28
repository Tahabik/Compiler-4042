from antlr4 import *
if "." in __name__:
    from .nngraphParser import nngraphParser
else:
    from nngraphParser import nngraphParser

# This class defines a complete generic visitor for a parse tree produced by nngraphParser.

class nngraphVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by nngraphParser#program.
    def visitProgram(self, ctx:nngraphParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nngraphParser#modelDecl.
    def visitModelDecl(self, ctx:nngraphParser.ModelDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nngraphParser#modelItem.
    def visitModelItem(self, ctx:nngraphParser.ModelItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nngraphParser#inputDecl.
    def visitInputDecl(self, ctx:nngraphParser.InputDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nngraphParser#outputDecl.
    def visitOutputDecl(self, ctx:nngraphParser.OutputDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nngraphParser#graphDecl.
    def visitGraphDecl(self, ctx:nngraphParser.GraphDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nngraphParser#graphItem.
    def visitGraphItem(self, ctx:nngraphParser.GraphItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nngraphParser#nodeDecl.
    def visitNodeDecl(self, ctx:nngraphParser.NodeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nngraphParser#layerType.
    def visitLayerType(self, ctx:nngraphParser.LayerTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nngraphParser#edgeDecl.
    def visitEdgeDecl(self, ctx:nngraphParser.EdgeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nngraphParser#edgeLabel.
    def visitEdgeLabel(self, ctx:nngraphParser.EdgeLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nngraphParser#configDecl.
    def visitConfigDecl(self, ctx:nngraphParser.ConfigDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nngraphParser#configEntry.
    def visitConfigEntry(self, ctx:nngraphParser.ConfigEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nngraphParser#paramList.
    def visitParamList(self, ctx:nngraphParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nngraphParser#param.
    def visitParam(self, ctx:nngraphParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nngraphParser#value.
    def visitValue(self, ctx:nngraphParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nngraphParser#shape.
    def visitShape(self, ctx:nngraphParser.ShapeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by nngraphParser#number.
    def visitNumber(self, ctx:nngraphParser.NumberContext):
        return self.visitChildren(ctx)



del nngraphParser
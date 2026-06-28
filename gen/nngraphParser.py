# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,28,161,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,3,0,40,8,0,1,
        0,1,0,1,1,1,1,1,1,1,1,4,1,48,8,1,11,1,12,1,49,1,1,1,1,1,2,1,2,3,
        2,56,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,5,5,70,
        8,5,10,5,12,5,73,9,5,1,5,1,5,1,6,1,6,3,6,79,8,6,1,7,1,7,1,7,1,7,
        1,7,1,7,3,7,87,8,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,98,8,
        9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,5,11,109,8,11,10,
        11,12,11,112,9,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,5,
        13,123,8,13,10,13,12,13,126,9,13,1,13,3,13,129,8,13,1,14,1,14,1,
        14,1,14,1,15,1,15,1,15,1,15,1,15,3,15,140,8,15,1,16,1,16,1,16,1,
        16,5,16,146,8,16,10,16,12,16,149,9,16,1,16,3,16,152,8,16,1,16,1,
        16,1,17,3,17,157,8,17,1,17,1,17,1,17,0,0,18,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,0,1,1,0,22,23,159,0,36,1,0,0,0,2,43,1,
        0,0,0,4,55,1,0,0,0,6,57,1,0,0,0,8,63,1,0,0,0,10,66,1,0,0,0,12,78,
        1,0,0,0,14,80,1,0,0,0,16,90,1,0,0,0,18,92,1,0,0,0,20,99,1,0,0,0,
        22,105,1,0,0,0,24,115,1,0,0,0,26,119,1,0,0,0,28,130,1,0,0,0,30,139,
        1,0,0,0,32,141,1,0,0,0,34,156,1,0,0,0,36,37,3,2,1,0,37,39,3,10,5,
        0,38,40,3,22,11,0,39,38,1,0,0,0,39,40,1,0,0,0,40,41,1,0,0,0,41,42,
        5,0,0,1,42,1,1,0,0,0,43,44,5,1,0,0,44,45,5,25,0,0,45,47,5,12,0,0,
        46,48,3,4,2,0,47,46,1,0,0,0,48,49,1,0,0,0,49,47,1,0,0,0,49,50,1,
        0,0,0,50,51,1,0,0,0,51,52,5,13,0,0,52,3,1,0,0,0,53,56,3,6,3,0,54,
        56,3,8,4,0,55,53,1,0,0,0,55,54,1,0,0,0,56,5,1,0,0,0,57,58,5,6,0,
        0,58,59,5,25,0,0,59,60,5,18,0,0,60,61,5,8,0,0,61,62,3,32,16,0,62,
        7,1,0,0,0,63,64,5,7,0,0,64,65,5,25,0,0,65,9,1,0,0,0,66,67,5,2,0,
        0,67,71,5,12,0,0,68,70,3,12,6,0,69,68,1,0,0,0,70,73,1,0,0,0,71,69,
        1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,71,1,0,0,0,74,75,5,13,0,0,
        75,11,1,0,0,0,76,79,3,14,7,0,77,79,3,18,9,0,78,76,1,0,0,0,78,77,
        1,0,0,0,79,13,1,0,0,0,80,81,5,4,0,0,81,82,5,25,0,0,82,83,5,18,0,
        0,83,84,3,16,8,0,84,86,5,14,0,0,85,87,3,26,13,0,86,85,1,0,0,0,86,
        87,1,0,0,0,87,88,1,0,0,0,88,89,5,15,0,0,89,15,1,0,0,0,90,91,5,25,
        0,0,91,17,1,0,0,0,92,93,5,5,0,0,93,94,5,25,0,0,94,95,5,11,0,0,95,
        97,5,25,0,0,96,98,3,20,10,0,97,96,1,0,0,0,97,98,1,0,0,0,98,19,1,
        0,0,0,99,100,5,16,0,0,100,101,5,25,0,0,101,102,5,20,0,0,102,103,
        5,24,0,0,103,104,5,17,0,0,104,21,1,0,0,0,105,106,5,3,0,0,106,110,
        5,12,0,0,107,109,3,24,12,0,108,107,1,0,0,0,109,112,1,0,0,0,110,108,
        1,0,0,0,110,111,1,0,0,0,111,113,1,0,0,0,112,110,1,0,0,0,113,114,
        5,13,0,0,114,23,1,0,0,0,115,116,5,25,0,0,116,117,5,20,0,0,117,118,
        3,30,15,0,118,25,1,0,0,0,119,124,3,28,14,0,120,121,5,19,0,0,121,
        123,3,28,14,0,122,120,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,
        125,1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,127,129,5,19,0,0,128,
        127,1,0,0,0,128,129,1,0,0,0,129,27,1,0,0,0,130,131,5,25,0,0,131,
        132,5,20,0,0,132,133,3,30,15,0,133,29,1,0,0,0,134,140,3,34,17,0,
        135,140,5,10,0,0,136,140,5,24,0,0,137,140,3,32,16,0,138,140,5,9,
        0,0,139,134,1,0,0,0,139,135,1,0,0,0,139,136,1,0,0,0,139,137,1,0,
        0,0,139,138,1,0,0,0,140,31,1,0,0,0,141,142,5,14,0,0,142,147,5,23,
        0,0,143,144,5,19,0,0,144,146,5,23,0,0,145,143,1,0,0,0,146,149,1,
        0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,151,1,0,0,0,149,147,1,
        0,0,0,150,152,5,19,0,0,151,150,1,0,0,0,151,152,1,0,0,0,152,153,1,
        0,0,0,153,154,5,15,0,0,154,33,1,0,0,0,155,157,5,21,0,0,156,155,1,
        0,0,0,156,157,1,0,0,0,157,158,1,0,0,0,158,159,7,0,0,0,159,35,1,0,
        0,0,14,39,49,55,71,78,86,97,110,124,128,139,147,151,156
    ]

class nngraphParser ( Parser ):

    grammarFileName = "nngraph.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'model'", "'graph'", "'config'", "'node'", 
                     "'edge'", "'input'", "'output'", "'tensor'", "'None'", 
                     "<INVALID>", "'->'", "'{'", "'}'", "'('", "')'", "'['", 
                     "']'", "':'", "','", "'='", "'-'" ]

    symbolicNames = [ "<INVALID>", "MODEL", "GRAPH", "CONFIG", "NODE", "EDGE", 
                      "INPUT", "OUTPUT", "TENSOR", "NONE", "BOOL", "ARROW", 
                      "LBRACE", "RBRACE", "LPAREN", "RPAREN", "LBRACK", 
                      "RBRACK", "COLON", "COMMA", "EQ", "MINUS", "FLOAT", 
                      "INT", "STRING", "IDENTIFIER", "WS", "LINE_COMMENT", 
                      "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_modelDecl = 1
    RULE_modelItem = 2
    RULE_inputDecl = 3
    RULE_outputDecl = 4
    RULE_graphDecl = 5
    RULE_graphItem = 6
    RULE_nodeDecl = 7
    RULE_layerType = 8
    RULE_edgeDecl = 9
    RULE_edgeLabel = 10
    RULE_configDecl = 11
    RULE_configEntry = 12
    RULE_paramList = 13
    RULE_param = 14
    RULE_value = 15
    RULE_shape = 16
    RULE_number = 17

    ruleNames =  [ "program", "modelDecl", "modelItem", "inputDecl", "outputDecl", 
                   "graphDecl", "graphItem", "nodeDecl", "layerType", "edgeDecl", 
                   "edgeLabel", "configDecl", "configEntry", "paramList", 
                   "param", "value", "shape", "number" ]

    EOF = Token.EOF
    MODEL=1
    GRAPH=2
    CONFIG=3
    NODE=4
    EDGE=5
    INPUT=6
    OUTPUT=7
    TENSOR=8
    NONE=9
    BOOL=10
    ARROW=11
    LBRACE=12
    RBRACE=13
    LPAREN=14
    RPAREN=15
    LBRACK=16
    RBRACK=17
    COLON=18
    COMMA=19
    EQ=20
    MINUS=21
    FLOAT=22
    INT=23
    STRING=24
    IDENTIFIER=25
    WS=26
    LINE_COMMENT=27
    BLOCK_COMMENT=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def modelDecl(self):
            return self.getTypedRuleContext(nngraphParser.ModelDeclContext,0)


        def graphDecl(self):
            return self.getTypedRuleContext(nngraphParser.GraphDeclContext,0)


        def EOF(self):
            return self.getToken(nngraphParser.EOF, 0)

        def configDecl(self):
            return self.getTypedRuleContext(nngraphParser.ConfigDeclContext,0)


        def getRuleIndex(self):
            return nngraphParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = nngraphParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.modelDecl()
            self.state = 37
            self.graphDecl()
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 38
                self.configDecl()


            self.state = 41
            self.match(nngraphParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModelDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MODEL(self):
            return self.getToken(nngraphParser.MODEL, 0)

        def IDENTIFIER(self):
            return self.getToken(nngraphParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(nngraphParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(nngraphParser.RBRACE, 0)

        def modelItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nngraphParser.ModelItemContext)
            else:
                return self.getTypedRuleContext(nngraphParser.ModelItemContext,i)


        def getRuleIndex(self):
            return nngraphParser.RULE_modelDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModelDecl" ):
                listener.enterModelDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModelDecl" ):
                listener.exitModelDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModelDecl" ):
                return visitor.visitModelDecl(self)
            else:
                return visitor.visitChildren(self)




    def modelDecl(self):

        localctx = nngraphParser.ModelDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_modelDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(nngraphParser.MODEL)
            self.state = 44
            self.match(nngraphParser.IDENTIFIER)
            self.state = 45
            self.match(nngraphParser.LBRACE)
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.modelItem()
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==6 or _la==7):
                    break

            self.state = 51
            self.match(nngraphParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModelItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inputDecl(self):
            return self.getTypedRuleContext(nngraphParser.InputDeclContext,0)


        def outputDecl(self):
            return self.getTypedRuleContext(nngraphParser.OutputDeclContext,0)


        def getRuleIndex(self):
            return nngraphParser.RULE_modelItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModelItem" ):
                listener.enterModelItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModelItem" ):
                listener.exitModelItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModelItem" ):
                return visitor.visitModelItem(self)
            else:
                return visitor.visitChildren(self)




    def modelItem(self):

        localctx = nngraphParser.ModelItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_modelItem)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.inputDecl()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.outputDecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(nngraphParser.INPUT, 0)

        def IDENTIFIER(self):
            return self.getToken(nngraphParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(nngraphParser.COLON, 0)

        def TENSOR(self):
            return self.getToken(nngraphParser.TENSOR, 0)

        def shape(self):
            return self.getTypedRuleContext(nngraphParser.ShapeContext,0)


        def getRuleIndex(self):
            return nngraphParser.RULE_inputDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputDecl" ):
                listener.enterInputDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputDecl" ):
                listener.exitInputDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputDecl" ):
                return visitor.visitInputDecl(self)
            else:
                return visitor.visitChildren(self)




    def inputDecl(self):

        localctx = nngraphParser.InputDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_inputDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(nngraphParser.INPUT)
            self.state = 58
            self.match(nngraphParser.IDENTIFIER)
            self.state = 59
            self.match(nngraphParser.COLON)
            self.state = 60
            self.match(nngraphParser.TENSOR)
            self.state = 61
            self.shape()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OUTPUT(self):
            return self.getToken(nngraphParser.OUTPUT, 0)

        def IDENTIFIER(self):
            return self.getToken(nngraphParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return nngraphParser.RULE_outputDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutputDecl" ):
                listener.enterOutputDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutputDecl" ):
                listener.exitOutputDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutputDecl" ):
                return visitor.visitOutputDecl(self)
            else:
                return visitor.visitChildren(self)




    def outputDecl(self):

        localctx = nngraphParser.OutputDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_outputDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(nngraphParser.OUTPUT)
            self.state = 64
            self.match(nngraphParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GraphDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GRAPH(self):
            return self.getToken(nngraphParser.GRAPH, 0)

        def LBRACE(self):
            return self.getToken(nngraphParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(nngraphParser.RBRACE, 0)

        def graphItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nngraphParser.GraphItemContext)
            else:
                return self.getTypedRuleContext(nngraphParser.GraphItemContext,i)


        def getRuleIndex(self):
            return nngraphParser.RULE_graphDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraphDecl" ):
                listener.enterGraphDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraphDecl" ):
                listener.exitGraphDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGraphDecl" ):
                return visitor.visitGraphDecl(self)
            else:
                return visitor.visitChildren(self)




    def graphDecl(self):

        localctx = nngraphParser.GraphDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_graphDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(nngraphParser.GRAPH)
            self.state = 67
            self.match(nngraphParser.LBRACE)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4 or _la==5:
                self.state = 68
                self.graphItem()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
            self.match(nngraphParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GraphItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nodeDecl(self):
            return self.getTypedRuleContext(nngraphParser.NodeDeclContext,0)


        def edgeDecl(self):
            return self.getTypedRuleContext(nngraphParser.EdgeDeclContext,0)


        def getRuleIndex(self):
            return nngraphParser.RULE_graphItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraphItem" ):
                listener.enterGraphItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraphItem" ):
                listener.exitGraphItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGraphItem" ):
                return visitor.visitGraphItem(self)
            else:
                return visitor.visitChildren(self)




    def graphItem(self):

        localctx = nngraphParser.GraphItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_graphItem)
        try:
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.nodeDecl()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.edgeDecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NodeDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NODE(self):
            return self.getToken(nngraphParser.NODE, 0)

        def IDENTIFIER(self):
            return self.getToken(nngraphParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(nngraphParser.COLON, 0)

        def layerType(self):
            return self.getTypedRuleContext(nngraphParser.LayerTypeContext,0)


        def LPAREN(self):
            return self.getToken(nngraphParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(nngraphParser.RPAREN, 0)

        def paramList(self):
            return self.getTypedRuleContext(nngraphParser.ParamListContext,0)


        def getRuleIndex(self):
            return nngraphParser.RULE_nodeDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNodeDecl" ):
                listener.enterNodeDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNodeDecl" ):
                listener.exitNodeDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNodeDecl" ):
                return visitor.visitNodeDecl(self)
            else:
                return visitor.visitChildren(self)




    def nodeDecl(self):

        localctx = nngraphParser.NodeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_nodeDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(nngraphParser.NODE)
            self.state = 81
            self.match(nngraphParser.IDENTIFIER)
            self.state = 82
            self.match(nngraphParser.COLON)
            self.state = 83
            self.layerType()
            self.state = 84
            self.match(nngraphParser.LPAREN)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 85
                self.paramList()


            self.state = 88
            self.match(nngraphParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LayerTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(nngraphParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return nngraphParser.RULE_layerType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLayerType" ):
                listener.enterLayerType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLayerType" ):
                listener.exitLayerType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLayerType" ):
                return visitor.visitLayerType(self)
            else:
                return visitor.visitChildren(self)




    def layerType(self):

        localctx = nngraphParser.LayerTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_layerType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(nngraphParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EdgeDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EDGE(self):
            return self.getToken(nngraphParser.EDGE, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(nngraphParser.IDENTIFIER)
            else:
                return self.getToken(nngraphParser.IDENTIFIER, i)

        def ARROW(self):
            return self.getToken(nngraphParser.ARROW, 0)

        def edgeLabel(self):
            return self.getTypedRuleContext(nngraphParser.EdgeLabelContext,0)


        def getRuleIndex(self):
            return nngraphParser.RULE_edgeDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdgeDecl" ):
                listener.enterEdgeDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdgeDecl" ):
                listener.exitEdgeDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdgeDecl" ):
                return visitor.visitEdgeDecl(self)
            else:
                return visitor.visitChildren(self)




    def edgeDecl(self):

        localctx = nngraphParser.EdgeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_edgeDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(nngraphParser.EDGE)
            self.state = 93
            self.match(nngraphParser.IDENTIFIER)
            self.state = 94
            self.match(nngraphParser.ARROW)
            self.state = 95
            self.match(nngraphParser.IDENTIFIER)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 96
                self.edgeLabel()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EdgeLabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(nngraphParser.LBRACK, 0)

        def IDENTIFIER(self):
            return self.getToken(nngraphParser.IDENTIFIER, 0)

        def EQ(self):
            return self.getToken(nngraphParser.EQ, 0)

        def STRING(self):
            return self.getToken(nngraphParser.STRING, 0)

        def RBRACK(self):
            return self.getToken(nngraphParser.RBRACK, 0)

        def getRuleIndex(self):
            return nngraphParser.RULE_edgeLabel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdgeLabel" ):
                listener.enterEdgeLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdgeLabel" ):
                listener.exitEdgeLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdgeLabel" ):
                return visitor.visitEdgeLabel(self)
            else:
                return visitor.visitChildren(self)




    def edgeLabel(self):

        localctx = nngraphParser.EdgeLabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_edgeLabel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(nngraphParser.LBRACK)
            self.state = 100
            self.match(nngraphParser.IDENTIFIER)
            self.state = 101
            self.match(nngraphParser.EQ)
            self.state = 102
            self.match(nngraphParser.STRING)
            self.state = 103
            self.match(nngraphParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConfigDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONFIG(self):
            return self.getToken(nngraphParser.CONFIG, 0)

        def LBRACE(self):
            return self.getToken(nngraphParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(nngraphParser.RBRACE, 0)

        def configEntry(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nngraphParser.ConfigEntryContext)
            else:
                return self.getTypedRuleContext(nngraphParser.ConfigEntryContext,i)


        def getRuleIndex(self):
            return nngraphParser.RULE_configDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfigDecl" ):
                listener.enterConfigDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfigDecl" ):
                listener.exitConfigDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfigDecl" ):
                return visitor.visitConfigDecl(self)
            else:
                return visitor.visitChildren(self)




    def configDecl(self):

        localctx = nngraphParser.ConfigDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_configDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(nngraphParser.CONFIG)
            self.state = 106
            self.match(nngraphParser.LBRACE)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 107
                self.configEntry()
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 113
            self.match(nngraphParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConfigEntryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(nngraphParser.IDENTIFIER, 0)

        def EQ(self):
            return self.getToken(nngraphParser.EQ, 0)

        def value(self):
            return self.getTypedRuleContext(nngraphParser.ValueContext,0)


        def getRuleIndex(self):
            return nngraphParser.RULE_configEntry

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfigEntry" ):
                listener.enterConfigEntry(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfigEntry" ):
                listener.exitConfigEntry(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConfigEntry" ):
                return visitor.visitConfigEntry(self)
            else:
                return visitor.visitChildren(self)




    def configEntry(self):

        localctx = nngraphParser.ConfigEntryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_configEntry)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(nngraphParser.IDENTIFIER)
            self.state = 116
            self.match(nngraphParser.EQ)
            self.state = 117
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nngraphParser.ParamContext)
            else:
                return self.getTypedRuleContext(nngraphParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(nngraphParser.COMMA)
            else:
                return self.getToken(nngraphParser.COMMA, i)

        def getRuleIndex(self):
            return nngraphParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = nngraphParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.param()
            self.state = 124
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 120
                    self.match(nngraphParser.COMMA)
                    self.state = 121
                    self.param() 
                self.state = 126
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 127
                self.match(nngraphParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(nngraphParser.IDENTIFIER, 0)

        def EQ(self):
            return self.getToken(nngraphParser.EQ, 0)

        def value(self):
            return self.getTypedRuleContext(nngraphParser.ValueContext,0)


        def getRuleIndex(self):
            return nngraphParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = nngraphParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(nngraphParser.IDENTIFIER)
            self.state = 131
            self.match(nngraphParser.EQ)
            self.state = 132
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(nngraphParser.NumberContext,0)


        def BOOL(self):
            return self.getToken(nngraphParser.BOOL, 0)

        def STRING(self):
            return self.getToken(nngraphParser.STRING, 0)

        def shape(self):
            return self.getTypedRuleContext(nngraphParser.ShapeContext,0)


        def NONE(self):
            return self.getToken(nngraphParser.NONE, 0)

        def getRuleIndex(self):
            return nngraphParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = nngraphParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_value)
        try:
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21, 22, 23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.number()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.match(nngraphParser.BOOL)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 136
                self.match(nngraphParser.STRING)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 4)
                self.state = 137
                self.shape()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 5)
                self.state = 138
                self.match(nngraphParser.NONE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShapeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(nngraphParser.LPAREN, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(nngraphParser.INT)
            else:
                return self.getToken(nngraphParser.INT, i)

        def RPAREN(self):
            return self.getToken(nngraphParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(nngraphParser.COMMA)
            else:
                return self.getToken(nngraphParser.COMMA, i)

        def getRuleIndex(self):
            return nngraphParser.RULE_shape

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShape" ):
                listener.enterShape(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShape" ):
                listener.exitShape(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShape" ):
                return visitor.visitShape(self)
            else:
                return visitor.visitChildren(self)




    def shape(self):

        localctx = nngraphParser.ShapeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_shape)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(nngraphParser.LPAREN)
            self.state = 142
            self.match(nngraphParser.INT)
            self.state = 147
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 143
                    self.match(nngraphParser.COMMA)
                    self.state = 144
                    self.match(nngraphParser.INT) 
                self.state = 149
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 150
                self.match(nngraphParser.COMMA)


            self.state = 153
            self.match(nngraphParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(nngraphParser.INT, 0)

        def FLOAT(self):
            return self.getToken(nngraphParser.FLOAT, 0)

        def MINUS(self):
            return self.getToken(nngraphParser.MINUS, 0)

        def getRuleIndex(self):
            return nngraphParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = nngraphParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 155
                self.match(nngraphParser.MINUS)


            self.state = 158
            _la = self._input.LA(1)
            if not(_la==22 or _la==23):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






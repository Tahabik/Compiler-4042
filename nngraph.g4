grammar nngraph;

program : modelDecl graphDecl configDecl? EOF;

modelDecl : MODEL IDENTIFIER LBRACE modelItem+ RBRACE;

modelItem: inputDecl | outputDecl;

inputDecl : INPUT IDENTIFIER COLON TENSOR shape;

outputDecl : OUTPUT IDENTIFIER ;


graphDecl : GRAPH LBRACE graphItem* RBRACE ;

graphItem: nodeDecl | edgeDecl ;

nodeDecl : NODE IDENTIFIER COLON layerType LPAREN paramList? RPAREN ;

layerType : IDENTIFIER ;

edgeDecl : EDGE IDENTIFIER ARROW IDENTIFIER edgeLabel? ;

edgeLabel : LBRACK IDENTIFIER EQ STRING RBRACK;

configDecl : CONFIG LBRACE configEntry* RBRACE ;

configEntry : IDENTIFIER EQ value ;


paramList : param (COMMA param)* COMMA? ;

param : IDENTIFIER EQ value ;

value : number | BOOL | STRING | shape | NONE ;

// A tensor/shape literal: a parenthesized tuple of dimensions like (3, 224, 224)
// or a single dimension like (128).
shape : LPAREN INT (COMMA INT)* COMMA? RPAREN ;

number : MINUS? (INT | FLOAT) ;

MODEL   : 'model' ;
GRAPH   : 'graph' ;
CONFIG  : 'config' ;
NODE    : 'node' ;
EDGE    : 'edge' ;
INPUT   : 'input' ;
OUTPUT  : 'output' ;
TENSOR  : 'tensor' ;
NONE    : 'None' ;
BOOL    : 'true' | 'false' ;

ARROW   : '->' ;
LBRACE  : '{' ;
RBRACE  : '}' ;
LPAREN  : '(' ;
RPAREN  : ')' ;
LBRACK  : '[' ;
RBRACK  : ']' ;
COLON   : ':' ;
COMMA   : ',' ;
EQ      : '=' ;
MINUS   : '-' ;

FLOAT : [0-9]+ '.' [0-9]+ ([eE] [+-]? [0-9]+)?
    | [0-9]+ [eE] [+-]? [0-9]+
    ;

INT : [0-9]+ ;

STRING
    : '"' ( ~["\\\r\n] | '\\' . )* '"'
    ;

IDENTIFIER
    : [a-zA-Z_] [a-zA-Z_0-9]*
    ;

WS : [ \t\r\n]+ -> skip ;
LINE_COMMENT  : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;

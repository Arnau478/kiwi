class TokenType:
    def __init__(self, id, repr=None):
        self.id = id
        self.repr = repr
    
    def __repr__(self):
        return self.id

PLUS = TokenType("PLUS", "+")
MINUS = TokenType("MINUS", "-")
MUL = TokenType("MUL", "*")
DIV = TokenType("DIV", "/")
LESS = TokenType("LESS", "<")
GREATER = TokenType("GREATER", ">")
LESS_EQ = TokenType("LESS_EQ", "<=")
GREATER_EQ = TokenType("GREATER_EQ", ">=")
OR = TokenType("OR", "||")
AND = TokenType("AND", "&&")
NOT = TokenType("NOT", "!")
NOT_EQ = TokenType("NOT_EQ", "!=")
EQ_EQ = TokenType("EQ_EQ", "==")
COLON = TokenType("COLON", ":")
LPAREN = TokenType("LPAREN", "(")
RPAREN = TokenType("RPAREN", ")")
LBRACE = TokenType("LBRACE", "{")
RBRACE = TokenType("RBRACE", "}")
EQ = TokenType("EQ", "=")
SEMI = TokenType("SEMI", ";")
IDENTIFIER = TokenType("IDENTIFIER")
KEYWORD = TokenType("KEYWORD")
INT_LITERAL = TokenType("INT_LITERAL")
EOF = TokenType("EOF", "EOF")

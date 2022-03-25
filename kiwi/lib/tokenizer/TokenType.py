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

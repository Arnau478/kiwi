from ast import Str
from lib.tokenizer.TokenType import TokenType

class Token:
    def __init__(self, type: TokenType, value: any = None, start: int = None, end: int = None) -> None:
        """Token class

        Args:
            type (TokenType): Token type (e.g. PLUS, KEYWORD).
            value (any, optional): Token's value. Defaults to None.
            start (int, optional): Start position. Defaults to None.
            end (int, optional): End position. Defaults to None.
        """
        self.type = type
        self.value = value
        self.start = start
        self.end = end
    
    def __repr__(self) -> Str:
        if(self.value): return f"<{self.type}({self.value})>"
        return f"<{self.type}>"

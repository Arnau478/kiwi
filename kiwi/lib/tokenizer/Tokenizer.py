import string
from lib.tokenizer.Token import Token
from lib.tokenizer.TokenType import TokenType
from lib.error.IllegalCharacter import IllegalCharacter

keywords = [
    "const",
    "fun",
    "if",
    "else",
    "return",
    "var",
    "while",
]

class Tokenizer:
    IGNORABLE_CHARACTERS = ["\n", " ", "\r", "\t"]

    def __init__(self, code: str) -> None:
        self.code = code
        self.idx = -1 # Store current char index (it starts at -1 so advance() call on __init__() will set it to 0)
        self.line = 1
        self.advance()
    
    def advance(self) -> None:
        # Increment index by one and reassign current_char (to None if EOF)
        self.idx += 1
        if self.idx < len(self.code):
            self.current_char = self.code[self.idx]
            if self.current_char == "\n": self.line += 1
        else:
            self.current_char = None
    
    def is_ignorable(self, char: str) -> bool:
        """Check if a character can be ignored by the tokenizer

        Args:
            char (str): Character to check

        Returns:
            bool: True if char can be skipped/ignored
        """

        return char in Tokenizer.IGNORABLE_CHARACTERS
    
    def match(self, char: str, advance: bool = True) -> bool:
        """Check for a character in current_char. If found, return true and advance it.

        Args:
            char (str): Character(s) to match. Note that this checks for any of the characters, not all of them.
            advance (bool): If True, when char matched it advances it. Defaults to True.

        Returns:
            bool: True if found, False if not
        """
        if self.current_char in char:
            if advance: self.advance()
            return True
        return False

    def tokenize(self) -> list:
        """Start tokenization process on Tokenizer object

        Returns:
            list: A list containing all the tokens
        """
        tokens = []

        while self.current_char:
            if self.is_ignorable(self.current_char):
                self.advance()
            elif self.match("+"):
                tokens.append(Token(TokenType.PLUS, start=self.idx-1, end=self.idx))
            elif self.match("-"):
                tokens.append(Token(TokenType.MINUS, start=self.idx-1, end=self.idx))
            elif self.match("*"):
                tokens.append(Token(TokenType.MUL, start=self.idx-1, end=self.idx))
            elif self.match("/"):
                tokens.append(Token(TokenType.DIV, start=self.idx-1, end=self.idx))
            elif self.match("<"):
                tokens.append(Token(TokenType.LESS, start=self.idx-1, end=self.idx))
            elif self.match(">"):
                tokens.append(Token(TokenType.GREATER, start=self.idx-1, end=self.idx))
            elif self.match(":"):
                tokens.append(Token(TokenType.COLON, start=self.idx-1, end=self.idx))
            elif self.match("("):
                tokens.append(Token(TokenType.LPAREN, start=self.idx-1, end=self.idx))
            elif self.match(")"):
                tokens.append(Token(TokenType.RPAREN, start=self.idx-1, end=self.idx))
            elif self.match("{"):
                tokens.append(Token(TokenType.LBRACE, start=self.idx-1, end=self.idx))
            elif self.match("}"):
                tokens.append(Token(TokenType.RBRACE, start=self.idx-1, end=self.idx))
            elif self.match("="):
                tokens.append(Token(TokenType.EQ, start=self.idx-1, end=self.idx))
            elif self.match(";"):
                tokens.append(Token(TokenType.SEMI, start=self.idx-1, end=self.idx))
            elif self.match(string.digits, advance=False):
                s = ""
                start = self.idx
                while self.current_char in string.digits:
                    s += self.current_char
                    self.advance()
                tokens.append(Token(TokenType.INT_LITERAL, value=int(s), start=start, end=self.idx))
            elif self.match(string.ascii_letters, advance=False):
                s = "" # Identifier's name
                start = self.idx # Save start position
                while self.current_char in string.ascii_letters:
                    s += self.current_char
                    self.advance()
                
                tokens.append(Token(TokenType.KEYWORD if s in keywords else TokenType.IDENTIFIER, value=s, start=start, end=self.idx))
            else:
                raise IllegalCharacter(self.current_char, self.line, self.code, description="Fired when an unexpected character was found while tokenizing your code")
        
        return tokens

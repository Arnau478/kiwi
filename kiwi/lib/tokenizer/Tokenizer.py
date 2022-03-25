import string
from lib.tokenizer.Token import Token
from lib.tokenizer import TokenType
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

    def get_line(self, idx: int):
        return self.code[:idx:].count("\n") + 1

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
                tokens.append(Token(TokenType.PLUS, line=self.get_line(self.idx-1)))
            elif self.match("-"):
                tokens.append(Token(TokenType.MINUS, line=self.get_line(self.idx-1)))
            elif self.match("*"):
                tokens.append(Token(TokenType.MUL, line=self.get_line(self.idx-1)))
            elif self.match("/"):
                tokens.append(Token(TokenType.DIV, line=self.get_line(self.idx-1)))
            elif self.match("<"):
                tokens.append(Token(TokenType.LESS, line=self.get_line(self.idx-1)))
            elif self.match(">"):
                tokens.append(Token(TokenType.GREATER, line=self.get_line(self.idx-1)))
            elif self.match(":"):
                tokens.append(Token(TokenType.COLON, line=self.get_line(self.idx-1)))
            elif self.match("("):
                tokens.append(Token(TokenType.LPAREN, line=self.get_line(self.idx-1)))
            elif self.match(")"):
                tokens.append(Token(TokenType.RPAREN, line=self.get_line(self.idx-1)))
            elif self.match("{"):
                tokens.append(Token(TokenType.LBRACE, line=self.get_line(self.idx-1)))
            elif self.match("}"):
                tokens.append(Token(TokenType.RBRACE, line=self.get_line(self.idx-1)))
            elif self.match("="):
                tokens.append(Token(TokenType.EQ, line=self.get_line(self.idx-1)))
            elif self.match(";"):
                tokens.append(Token(TokenType.SEMI, line=self.get_line(self.idx-1)))
            elif self.match(string.digits, advance=False):
                s = ""
                start = self.idx
                while self.current_char in string.digits:
                    s += self.current_char
                    self.advance()
                tokens.append(Token(TokenType.INT_LITERAL, value=int(s), line=self.get_line(start)))
            elif self.match(string.ascii_letters, advance=False):
                s = "" # Identifier's name
                start = self.idx # Save start position
                while self.current_char in string.ascii_letters:
                    s += self.current_char
                    self.advance()
                
                tokens.append(Token(TokenType.KEYWORD if s in keywords else TokenType.IDENTIFIER, value=s, line=self.get_line(start)))
            else:
                raise IllegalCharacter(self.current_char, self.line, self.code)
        
        tokens.append(Token(TokenType.EOF, line=self.get_line(self.idx-1)))
        
        return tokens

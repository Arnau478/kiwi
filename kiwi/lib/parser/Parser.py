from lib.error.UnexpectedToken import UnexpectedToken
from lib.error.UnexpectedEnd import UnexpectedEnd
from lib.tokenizer import TokenType

class Parser:
    def __init__(self, tokens, source) -> None:
        self.tokens = tokens
        self.source = source
        self.idx = -1
        self.line = 0
        self.advance()
    
    def advance(self):
        self.idx += 1
        if self.idx < len(self.tokens):
            self.current_tok = self.tokens[self.idx]
            self.line = self.current_tok.line
        else:
            self.current_tok = None

    def match(self, type, value=None, advance=True):
        if self.current_tok.type == type and (value == None or value == self.current_tok.value):
            if(advance): self.advance()
            return True
        return False
    
    def parse(self):
        self.par_program()
    
    def par_program(self):
        while self.current_tok and self.current_tok.type != TokenType.EOF:
            if(self.match(TokenType.KEYWORD, value="fun", advance=False)):
                self.par_fun()
            else:
                raise UnexpectedToken(self.current_tok, self.source)

            
        if self.current_tok == None:
            raise UnexpectedEnd(self.line, self.source)

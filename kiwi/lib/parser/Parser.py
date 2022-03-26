from lib.error.UnexpectedToken import UnexpectedToken
from lib.error.UnexpectedEnd import UnexpectedEnd
from lib.tokenizer import TokenType
from lib.parser import SyntaxNode

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
            if self.idx + 1 < len(self.tokens):
                self.next_tok = self.tokens[self.idx + 1]
        else:
            self.current_tok = None
            self.next_tok = None
        
        return self.current_tok

    def match(self, type, value=None, advance=True):
        if self.current_tok.type == type and (value == None or value == self.current_tok.value):
            if(advance): self.advance()
            return True
        return False
    
    def consume(self, type, value=None):
        if self.current_tok.type != type or (value and self.current_tok.value != value):
            raise UnexpectedToken(self.current_tok, self.source, f"'{type.repr if type.repr else value}'")
        tok = self.current_tok
        self.advance()
        return tok
    
    def bin_op(self, tokens, func):
        left = func()
        
        while self.current_tok.type in tokens:
            operator = self.current_tok
            self.advance()
            right = func()
            left = SyntaxNode.BinOp(left, operator, right)
        
        return left

    def parse(self):
        return self.par_program()
    
    def par_program(self):
        globals = []

        while self.current_tok and self.current_tok.type != TokenType.EOF:
            if self.match(TokenType.KEYWORD, value="fun", advance=False):
                globals.append(self.par_fun())
            elif self.match(TokenType.KEYWORD, value="const", advance=False):
                globals.append(self.par_var())
                self.consume(TokenType.SEMI)
            elif self.match(TokenType.KEYWORD, value="var", advance=False):
                globals.append(self.par_var())
                self.consume(TokenType.SEMI)
            else:
                raise UnexpectedToken(self.current_tok, self.source, "function or variable definition")
            
        if self.current_tok == None:
            raise UnexpectedEnd(self.line, self.source)

        return SyntaxNode.Program(globals)
    
    def par_var(self):
        constant = None
        if self.match(TokenType.KEYWORD, value="var"):
            constant = False
        elif self.match(TokenType.KEYWORD, value="const"):
            constant = True
        else:
            raise UnexpectedToken(self.current_tok, self.source, "'var' or 'const'")
        id = self.consume(TokenType.IDENTIFIER)
        self.consume(TokenType.COLON)
        type = self.par_type()
        self.consume(TokenType.EQ)
        val = self.par_expr()

        return SyntaxNode.Variable(id, type, val, constant)
    
    def par_type(self):
        if self.match(TokenType.IDENTIFIER, value="int"):
            return SyntaxNode.Type("int")
        else:
            raise UnexpectedToken(self.current_tok, self.source, "data type")
    
    def par_expr(self):
        if self.match(TokenType.KEYWORD, value="var", advance=False):
            return self.par_var()
        return self.par_assign()
    
    def par_assign(self):
        if(self.current_tok.type == TokenType.IDENTIFIER and self.next_tok.type == TokenType.EQ):
            id = self.advance()
            self.consume(TokenType.EQ)
            val = self.par_expr()
            
            return SyntaxNode.Assign(id, val) 
        
        return self.par_or()
    
    def par_or(self):
        return self.bin_op([TokenType.OR], self.par_and)

    def par_and(self):
        return self.bin_op([TokenType.AND], self.par_equality)

    def par_equality(self):
        return self.bin_op([TokenType.EQ_EQ, TokenType.NOT_EQ], self.par_comparison)

    def par_comparison(self):
        return self.bin_op([TokenType.LESS, TokenType.GREATER, TokenType.LESS_EQ, TokenType.GREATER_EQ], self.par_addition)
    
    def par_addition(self):
        return self.bin_op([TokenType.PLUS, TokenType.MINUS], self.par_multiplication)
        
    def par_multiplication(self):
        return self.bin_op([TokenType.MUL, TokenType.DIV], self.par_unary)
    
    def par_unary(self):
        if self.match(TokenType.NOT, advance=False) or self.match(TokenType.MINUS, advance=False):
            operator = self.advance()
            right = self.par_unary()
            
            return SyntaxNode.UnaryOp(operator, right)
        
        return self.par_call()
    
    def par_call(self):
        expr = self.par_atom()
        if(self.match(TokenType.LPAREN)):
            args = []
            while(not self.match(TokenType.RPAREN)):
                args.append(self.par_expr())
            return SyntaxNode.Call(expr, args)

        return expr
    
    def par_atom(self):
        if self.match(TokenType.INT_LITERAL, advance=False):
            ret = SyntaxNode.Literal(self.current_tok)
            self.advance()
            return ret
        elif self.match(TokenType.IDENTIFIER, advance=False):
            ret = SyntaxNode.Access(self.current_tok)
            self.advance()
            return ret
        else:
            raise UnexpectedToken(self.current_tok, self.source, "expression")


    def par_fun(self):
        self.consume(TokenType.KEYWORD, "fun")
        id = self.consume(TokenType.IDENTIFIER)
        self.consume(TokenType.LPAREN)
        args = []
        while not self.match(TokenType.RPAREN, advance=False):
            arg_id = self.consume(TokenType.IDENTIFIER)
            self.consume(TokenType.COLON)
            arg_type = self.par_type()
            args.append((arg_id, arg_type))
        self.consume(TokenType.RPAREN)
        self.consume(TokenType.COLON)
        type = self.par_type()
        body = self.par_stmt()

        return SyntaxNode.Function(id, type, args, body)

    def par_stmt(self):
        if self.match(TokenType.LBRACE):
            statements = []
            while not self.match(TokenType.RBRACE, advance=False):
                statements.append(self.par_stmt())
            
            self.consume(TokenType.RBRACE)

            return SyntaxNode.Block(statements)
        elif self.match(TokenType.KEYWORD, value="if"):
            self.consume(TokenType.LPAREN)
            condition = self.par_expr()
            self.consume(TokenType.RPAREN)
            then_body = self.par_stmt()
            
            else_body = None
            if self.match(TokenType.KEYWORD, value="else"):
                else_body = self.par_stmt()

            return SyntaxNode.If(condition, then_body, else_body)
        elif self.match(TokenType.KEYWORD, value="while"):
            self.consume(TokenType.LPAREN)
            condition = self.par_expr()
            self.consume(TokenType.RPAREN)
            body = self.par_stmt()

            return SyntaxNode.While(condition, body)
        elif self.match(TokenType.KEYWORD, value="return"):
            value = None
            if(not self.match(TokenType.SEMI)):
                value = self.par_expr()
                self.consume(TokenType.SEMI)
            
            return SyntaxNode.Return(value)
        else:
            expr = self.par_expr()
            self.consume(TokenType.SEMI)
            return expr

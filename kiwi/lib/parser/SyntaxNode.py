class SyntaxNode:
    def __repr__(self):
        dict = {}
        dict["_"] = self.__class__.__name__
        for key in self.__dict__:
            dict[key] = self.__dict__[key]
        return dict.__repr__()

class Type(SyntaxNode):
    def __init__(self, name):
        self.name = name
class Literal(SyntaxNode):
    def __init__(self, value):
        self.value = value
class Variable(SyntaxNode):
    def __init__(self, id, type, value, constant):
        self.id = id
        self.type = type
        self.value = value
        self.constant = constant
class Program(SyntaxNode):
    def __init__(self, globals):
        self.globals = globals
class Function(SyntaxNode):
    def __init__(self, id, type, args, body):
        self.id = id
        self.type = type
        self.args = args
        self.body = body
class Block(SyntaxNode):
    def __init__(self, statements):
        self.statements = statements
class Access(SyntaxNode):
    def __init__(self, var):
        self.var = var
class If(SyntaxNode):
    def __init__(self, condition, then_body, else_body):
        self.condition = condition
        self.then_body = then_body
        self.else_body = else_body
class BinOp(SyntaxNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
class Return(SyntaxNode):
    def __init__(self, value):
        self.value = value
class Call(SyntaxNode):
    def __init__(self, callee, args):
        self.callee = callee
        self.args = args
class While(SyntaxNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
class Assign(SyntaxNode):
    def __init__(self, id, val):
        self.id = id
        self.val = val

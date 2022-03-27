from lib.parser import SyntaxNode
from lib.kmc import Kmc

class Generator:
    def __init__(self, ast, source):
        self.ast = ast
        self.source = source
        self.kmc_code = Kmc.Code()
    
    def write(self, line):
        self.kmc_code.add(line)

    def generate(self):
        self.visit(self.ast)
        return self.kmc_code
    
    def visit(self, node):
        fun = getattr(self, f"visit_{node.__class__.__name__}")
        return fun(node)
    
    def visit_Program(self, node: SyntaxNode.Program):
        for glob in node.globals:
            self.visit(glob)
    
    def visit_Function(self, node: SyntaxNode.Function):
        self.write(Kmc.Label(f"_f_{node.id.value}"))
        self.write(Kmc.Instruction("ENTER", []))
        self.visit(node.body)
        self.write(Kmc.Instruction("LEAVE", []))
        self.write(Kmc.Instruction("RET", []))
    
    def visit_Block(self, node: SyntaxNode.Block):
        for stmt in node.statements:
            self.visit(stmt)
    
    def visit_Return(self, node: SyntaxNode.Return):
        self.write(Kmc.Instruction("LEAVE", []))
        self.write(Kmc.Instruction("RET", []))

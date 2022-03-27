class Code:
    def __init__(self):
        self.lines = []

    def add(self, line):
        self.lines.append(line)
    
    def to_str(self):
        s = ""
        for line in self.lines:
            s += line.to_str()
            s += "\n"
        s = s[:-1]
        return s
    
    def __repr__(self):
        return self.to_str()
    
class Instruction:
    def __init__(self, inst, args):
        self.inst = inst
        self.args = args
    
    def to_str(self):
        return f"\t\t{self.inst} {' '.join(self.args)}"
    
class Label:
    def __init__(self, name):
        self.name = name
    
    def to_str(self):
        return f"\t{self.name}:"
    
class Tag:
    def __init__(self, tag):
        self.tag = tag
    
    def to_str(self):
        return f"{self.tag}"
        

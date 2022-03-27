from lib.kmc import Kmc

class Generator:
    def __init__(self, kmc_code):
        self.kmc_code = kmc_code
        self.asm_code = ""
    
    def generate(self):
        for line in self.kmc_code.lines:
            if isinstance(line, Kmc.Instruction):
                if line.inst == "RET":
                    self.asm_code += f"\t\tret\n"
                elif line.inst == "ENTER":
                    self.asm_code += f"\t\tenter\n"
                elif line.inst == "LEAVE":
                    self.asm_code += f"\t\tleave\n"
                else:
                    raise Exception("Unimplemented ASM generation for KMC instruction " + line.__dict__.__str__())
            elif isinstance(line, Kmc.Label):
                self.asm_code += f"\t{line.name}:\n"
            else:
                raise Exception("Unimplemented case for line class " + str(line.__class__))
        
        return self.asm_code

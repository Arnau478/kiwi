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
                    self.asm_code += f"\t\tenter 0, 0\n"
                elif line.inst == "LEAVE":
                    self.asm_code += f"\t\tleave\n"
                elif line.inst == "JMP":
                    self.asm_code += f"\t\tjmp {line.args[0]}\n"
                elif line.inst == "CALL":
                    self.asm_code += f"\t\tcall {line.args[0]}\n"
                elif line.inst == "EXIT":
                    self.asm_code += f"\t\tmov ebx, eax\n"
                    self.asm_code += f"\t\tmov eax, 0x1\n"
                    self.asm_code += f"\t\tint 0x80\n"
                else:
                    raise Exception("Unimplemented ASM generation for KMC instruction " + line.__dict__.__str__())
            elif isinstance(line, Kmc.Label):
                self.asm_code += f"\t{line.name}:\n"
            elif isinstance(line, Kmc.Tag):
                self.asm_code += f"{line.tag}\n"
            else:
                raise Exception("Unimplemented case for line class " + str(line.__class__))
        
        return self.asm_code

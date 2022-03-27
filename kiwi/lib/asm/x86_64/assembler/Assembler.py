import os

class Assembler:
    def __init__(self, asm_code):
        self.asm_code = asm_code
    
    def assemble(self):
        tmp_path = "/tmp/kiwi"
        if not os.path.exists(tmp_path):
            os.mkdir(tmp_path)
        asm_file_path = tmp_path + "/t.s"
        obj_file_path = tmp_path + "/t.o"
        bin_file_path = tmp_path + "/t"
        asm_file = open(asm_file_path, "w+")
        asm_file.write(self.asm_code)
        asm_file.close()
        os.system(f"nasm {asm_file_path} -o {obj_file_path} -f elf64")
        os.system(f"ld {obj_file_path} -o {bin_file_path}")

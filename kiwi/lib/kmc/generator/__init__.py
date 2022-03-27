from lib.kmc.generator.Generator import Generator

def generate(ast, code):
    generator = Generator(ast, code)
    kmc_code = generator.generate()
    return kmc_code

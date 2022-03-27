import importlib
from . import Platform
from lib.error.PlatformError import PlatformError

def get_module(name):
    platform = Platform.get_platform().id
    try:
        return importlib.import_module(f"lib.asm.{platform}.{name}")
    except ImportError:
        raise PlatformError(platform)

def generate(kmc_code):
    module = get_module("generator")
    generator = module.Generator(kmc_code)
    asm_code = generator.generate()
    return asm_code

def assemble(asm_code):
    module = get_module("assembler")
    assembler = module.Assembler(asm_code)
    binout = assembler.assemble()
    return binout

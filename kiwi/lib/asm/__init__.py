import importlib
from . import Platform
from lib.error.PlatformError import PlatformError

def generate(kmc_code):
    platform = Platform.get_platform().id
    try:
        module = importlib.import_module(f"lib.asm.{platform}.generator")
    except ImportError:
        raise PlatformError(platform)
    generator = module.Generator(kmc_code)
    asm_code = generator.generate()
    return asm_code

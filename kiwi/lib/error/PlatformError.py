from lib.error.KiwiError import KiwiError

class PlatformError(KiwiError):
    def __init__(self, platform):
        super().__init__(f"Unsupported architecture: {platform}", description="Fired if the selected platform is unavailable for compiling")

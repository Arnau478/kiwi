import platform

class Platform:
    def __init__(self, id):
        self.id = id

def get_platform() -> Platform:
    return Platform(platform.machine())

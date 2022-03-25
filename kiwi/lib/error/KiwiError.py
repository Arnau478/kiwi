class KiwiError(Exception):
    def __init__(self, message=None, description=None) -> None:
        self.message = message
        self.description = description
        super().__init__(message)
    
    def get_throw_message(self):
        if self.message: return f": {self.message}"
        return ""
    
    def get_throw_extra(self):
        return ""

    def throw(self) -> None:
        str = f"\x1b[31m\x1b[1mERROR\x1b[0m \x1b[33m{self.__class__.__name__}\x1b[0m" # Title (eg. "ERROR KiwiError")
        str += self.get_throw_message() # Message
        if self.description: str += f"\n\x1b[2m(?) {self.description}\x1b[0m" # Description
        str += self.get_throw_extra() # Extra
        print(str)

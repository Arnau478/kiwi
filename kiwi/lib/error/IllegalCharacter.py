from lib.error.KiwiError import KiwiError

class IllegalCharacter(KiwiError):
    def __init__(self, char, line, code):
        self.line = line
        self.code = code
        super().__init__(f"Unexpected character: '{char}'", description="Fired when an unexpected character was found while tokenizing your code")

    def get_throw_extra(self):
        ret = ""
        ret += f"\n\n  \x1b[1mOn line {self.line}:\x1b[0m\n"
        if self.code.split("\n")[self.line-2]: ret += "\n    " + self.code.split("\n")[self.line-2]
        if self.code.split("\n")[self.line-1]: ret += "\n\x1b[1m>>\x1b[0m  \x1b[31m" + self.code.split("\n")[self.line-1] + "\x1b[0m"
        if self.code.split("\n")[self.line-0]: ret += "\n    " + self.code.split("\n")[self.line-0]
        ret += "\n"

        return ret

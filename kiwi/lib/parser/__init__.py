from lib.parser.Parser import Parser


def parse(tokens, source):
    parser = Parser(tokens, source)
    ast = parser.parse()
    return ast

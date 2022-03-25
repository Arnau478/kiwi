from lib.tokenizer.Tokenizer import Tokenizer

def tokenize(code):
    tokenizer = Tokenizer(code)
    tokens = tokenizer.tokenize()
    return tokens

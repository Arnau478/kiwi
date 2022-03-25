#!/usr/bin/env python3

##    ## #### ##      ## ####
##   ##   ##  ##  ##  ##  ## 
##  ##    ##  ##  ##  ##  ## 
#####     ##  ##  ##  ##  ## 
##  ##    ##  ##  ##  ##  ## 
##   ##   ##  ##  ##  ##  ## 
##    ## ####  ###  ###  ####

# Kiwi programming language compiler #

import argparse
from lib import parser
from lib import tokenizer
from lib.error.KiwiError import KiwiError

__version__ = "dev"

def compile(code) -> None:
    """Compile kiwi code

    Args:
        code (str): Kiwi source code
    """
    
    # Tokenize
    tokens = tokenizer.tokenize(code)
    
    # Parse
    ast = parser.parse(tokens, code)
    print(ast)

if(__name__ == "__main__"):
    try:
        cli_parser = argparse.ArgumentParser(description="Kiwi programming language compiler")
        cli_parser.add_argument("input", help="Input source file path")
        cli_parser.add_argument("-o", "--output", help="Output path for the compiled code")
        cli_parser.add_argument("-v", "--verbose", help="Verbose level", type=int)
        cli_parser.add_argument("--version", help="Show version", action="version", version=__version__)
        args = cli_parser.parse_args()
        compile(open(args.input, "r").read())
    except KiwiError as e:
        e.throw()

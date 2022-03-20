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

from modules import *

__version__ = "dev"

if(__name__ == "__main__"):
    cli_parser = argparse.ArgumentParser(description="Kiwi programming language compiler")
    cli_parser.add_argument("input", help="Input source file path")
    cli_parser.add_argument("-o", "--output", help="Output path for the compiled code")
    cli_parser.add_argument("-v", "--verbose", help="Verbose level")
    cli_parser.add_argument("--version", help="Show version", action="version", version=__version__)
    args = cli_parser.parse_args()
    print(args.__dict__)

#!/usr/bin/env python
# https://www.codewars.com/kata/58e61f3d8ff24f774400002c/train/python

import sys

def assembler_interpreter(program):
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: interpreter.py [program path]")
        exit(-1)
    try:
        f = open(sys.argv[1], 'r')
    except:
        print("Wrong arg!")
        exit(-1)

    prog = f.read().splitlines()
    output = assembler_interpreter(prog)
    print(output)
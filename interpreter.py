#!/usr/bin/env python
# https://www.codewars.com/kata/58e61f3d8ff24f774400002c/train/python

import sys
from collections import deque


def assembler_interpreter(program):
    # * Init
    pc = 0
    callstack = deque()
    registers = {}
    labels = {}
    cmpres = 0
    output = -1

    # * Preprocessing - delete comment stuff; process labels

    # del comments
    for idx, line in enumerate(program):
        if ';' in line:
            program[idx] = line[:line.index(';')]

    # fuck commas
    for idx, line in enumerate(program):
        if ',' in line:
            program[idx] = ''.join(filter(lambda c: c != ',', line))

    # deleting extra spaces
    program = [line.strip() for line in program]

    # del empty lines
    def isnotempty(line): return line
    program = list(filter(isnotempty, program))

    # indexing labels
    for idx, line in enumerate(program):
        if ':' in line:
            labels[line.strip()[:-1]] = idx
            del program[idx]

    # * Runtime
    # TODO: Fuck commas
    while pc < len(program):
        splited_line = program[pc].split()
        cmd, args = splited_line[0], splited_line[1:]

        if cmd == 'mov':
            if args[1] in registers:
                registers[args[0]] = registers[args[1]]
            else:
                registers[args[0]] = int(args[1])
        elif cmd == 'inc':
            registers[args[0]] = registers[args[0]]+1
        elif cmd == 'dec':
            registers[args[0]] = registers[args[0]]-1
        elif cmd == 'add':
            if args[1] in registers:
                registers[args[0]] = registers[args[0]]+registers[args[1]]
            else:
                registers[args[0]] = registers[args[0]]+int(args[1])
        elif cmd == 'sub':
            if args[1] in registers:
                registers[args[0]] = registers[args[0]]-registers[args[1]]
            else:
                registers[args[0]] = registers[args[0]]-int(args[1])
        elif cmd == 'div':
            if args[1] in registers:
                registers[args[0]] = registers[args[0]]//registers[args[1]]
            else:
                registers[args[0]] = registers[args[0]]//int(args[1])
        elif cmd == 'mul':
            if args[1] in registers:
                registers[args[0]] = registers[args[0]]*registers[args[1]]
            else:
                registers[args[0]] = registers[args[0]]*int(args[1])
        elif cmd == 'jmp':
            pc = labels[args[0]]
            continue
        elif cmd == 'cmp':
            if args[1] in registers:
                cmpres = registers[args[0]]-registers[args[1]]
            else:
                cmpres = registers[args[0]]-int(args[1])
        elif cmd == 'jne':
            if cmpres != 0:
                pc = labels[args[0]]
                continue
        elif cmd == 'je':
            if cmpres == 0:
                pc = labels[args[0]]
                continue
        elif cmd == 'jge':
            if cmpres >= 0:
                pc = labels[args[0]]
                continue
        elif cmd == 'jg':
            if cmpres > 0:
                pc = labels[args[0]]
                continue
        elif cmd == 'jle':
            if cmpres <= 0:
                pc = labels[args[0]]
                continue
        elif cmd == 'jl':
            if cmpres < 0:
                pc = labels[args[0]]
                continue
        elif cmd == 'call':
            callstack.append(pc)
            pc = labels[args[0]]
            continue
        elif cmd == 'ret':
            pc = callstack.pop()
        elif cmd == 'msg':
            #! FUCK COMMAS!
            output = ""
            for arg in "".join(args).split("'"):
                if arg in registers:
                    output = output+str(registers[arg])
                else:
                    output = output+arg
        elif cmd == 'end':
            if output == -1:
                output = 0
            break
        pc = pc+1

    return output


if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     print("Usage: interpreter.py [program path]")
    #     exit(-1)
    # try:
    #     f = open(sys.argv[1], 'r')
    # except:
    #     print("Wrong arg!")
    #     exit(-1)

    # prog = f.read().splitlines()
    # output = assembler_interpreter(prog)
    code = '''
        ; My first program
        mov  a, 5
        inc  a
        call function
        msg  '(5+1)/2 = ', a    ; output message
        end

        function:
            div  a, 2
            ret
        '''
    print(assembler_interpreter(code.splitlines()))

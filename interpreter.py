#!/usr/bin/env python
# https://www.codewars.com/kata/58e24788e24ddee28e000053

def simple_assembler(program):
    pc = 0
    pl = len(program)
    regs = {}
    
    def mov(reg, value):
        if value.isalpha():
            regs[reg] = regs[value] 
        else:
            regs[reg] = int(value) 
        
    def inc(reg):
        regs[reg] = regs[reg]+1
        
    def dec(reg):
        regs[reg] = regs[reg]-1
        
    def jnz(v1, v2):
        nonlocal pc
        if v1.isalpha():
            if regs[v1] != 0:
                pc = pc+int(v2)-1
        else:
            if v1 != 0:
                pc = pc+int(v2)-1
            
    cmds = {
                'mov':mov, 
                'inc':inc, 
                'dec':dec, 
                'jnz':jnz 
            }
            
    while pc < pl:
        curr_cmd = program[pc].split()
        pc = pc+1
        cmds[curr_cmd[0]](*curr_cmd[1:])
  # return a dictionary with the registers
    return regs

if __name__=="__main__":
    code = '''\
    mov c 12
    mov b 0
    mov a 200
    dec a
    inc b
    jnz a -2
    dec c
    mov a b
    jnz c -5
    jnz 0 1
    mov c a'''
    
    print(simple_assembler(code.splitlines()))
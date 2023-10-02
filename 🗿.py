# 🗿 🗿 🗿 #

import os, sys

args = sys.argv[1:]

if len(args) == 0:
    print('\x1b[31m🗿 GIMME A FILE\x1b[39m')
    exit(1)
if not os.path.exists(args[0]) and args[0] != '-':
    print('\x1b[31m🗿 GIMME AN ACTUAL FILE\x1b[39m')
    exit(1)
if not os.path.isfile(args[0]) and args[0] != '-':
    print('\x1b[31m🗿 GIMME AN ACTUAL ACTUAL FILE\x1b[39m')
    exit(1)
    
def parse( script:str, file:str ) -> list[list[int]]:
    prog:list[list[int]] = []
    cnt = 0
    for lno,line in enumerate(script.splitlines()):
        prog.append([])
        for col,c in enumerate(line):
            if c == ' ':
                prog[-1].append(cnt)
                cnt = 0
            elif c == '🗿':
                cnt += 1
            else:
                print('\x1b[31m🗿 `%s` WUT ??? (%s:%d:%d)'%(c,file,lno+1,col+2))
                exit(1)
        if cnt != 0:
            prog[-1].append(cnt)
        if len(prog[-1]) == 0:
            prog.pop()
        cnt = 0
    return prog

with open(args[0],'rt',encoding='utf-8') as f:
    
    moyai = parse(f.read(),args[0])
    ptr = 0
    
    stack = []
    
    if str(moyai) == '[[4], [1], [2], [1], [4]]':
        print('E')
        exit(0)
    
    while ptr < len(moyai):
        instr,*dat = moyai[ptr]
        
        if instr == 1:
            
            instr,*dat = dat
            
            if instr == 1:
                v = 0
                
                for d in dat:
                    if d == 0: v *= -1
                    if d == 1: v += 1
                    if d == 2: v -= 1
                    if d == 3: v *= 2
                    if d == 4: v *= 5
                    if d == 5: v /= 2
                    if d == 6: v /= 5
                    
                stack.append(v)
                
            elif instr == 2:
                
                stack.pop()
                
            elif instr == 3:
                
                print(stack.pop())
                
            elif instr == 4:
                
                stack.append(stack[-1])
                
        elif instr == 2:
            
            op,*_ = dat
            
            a,b = stack.pop(),stack.pop()
            
            if op == 1: stack.append(a+b)
            if op == 2: stack.append(a-b)
            if op == 3: stack.append(a*b)
            if op == 4: stack.append(a/b)
            
        elif instr == 3:
            
            instr,*dat = dat
            
            if instr == 1:
                
                wa = ''
                while stack[-1] != 0:
                    wa += chr(stack.pop())
                stack.append(wa[::-1])
                
            elif instr == 2:
                
                stack.append(int(stack.pop()))

            elif instr == 3:
                
                stack.append(ord(stack.pop()))
                
        ptr += 1
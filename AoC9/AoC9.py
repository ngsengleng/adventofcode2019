with open("AoC9.txt") as f:
    code = list(map(str,f.read().split(",")))
code = code + ['0'] * 9999999
inpt = 2
output = 0
i,a,b = 0,0,0
rBase = 0
while True:
    instr = code[i].zfill(5)
    opcode = int(instr[-2:])
    addr = [0,0,0]
    for n in range(3):
        if instr[2-n] == '0':
            addr[n] = int(code[i+1+n])
        elif instr[2-n] == '1':
            addr[n] = i+1+n
        elif instr[2-n] == '2':
            addr[n] = int(code[i+1+n]) + rBase
    a = int(code[addr[0]])
    b = int(code[addr[1]])
    if opcode == 99:                                    
        break
    elif opcode == 3:                                   
        code[addr[0]] = inpt
        i += 2
    elif opcode == 4:                        
        output = code[addr[0]]
        print(output)
        i += 2
    else:
        if opcode == 1:
            code[addr[2]] = str(a + b)
            i += 4
        elif opcode == 2:
            code[addr[2]] = str(a * b)
            i += 4
        elif opcode == 5:
            if a > 0:
                i = b
            else:
                i += 3
        elif opcode == 6:
            if a == 0:
                i = b
            else:
                i += 3
        elif opcode == 7:
            if a < b:
                code[addr[2]] = 1
            else:
                code[addr[2]] = 0
            i += 4
        elif opcode == 8:
            if a == b:
                code[addr[2]] = 1
            else:
                code[addr[2]] = 0
            i += 4
        elif opcode == 9:
            rBase += a
            i += 2


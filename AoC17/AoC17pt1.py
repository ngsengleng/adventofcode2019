with open("17pt1.txt") as f:
    code = list(map(str,f.read().split(",")))
code = code + ['0'] * 9999999
output = 0
i,a,b = 0,0,0
rBase = 0
outpt = []

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
        count += 1
        i += 2
    elif opcode == 4:                        
        output = code[addr[0]]
        outpt.append(output)
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


scaffold = [[]]
row = 0
for x in outpt:

    if x == '10':
        scaffold.append([])
        row += 1
    else:
        scaffold[row].append(chr(int(x)))

intersects = 0
for x in range(len(scaffold)-2):
    if x == 0:
        continue
    for y in range(len(scaffold[x])):
        if scaffold[x][y] == '#':
            try:
                if scaffold[x+1][y] == '#' and scaffold[x-1][y] == '#':
                    if scaffold[x][y+1] == '#' and scaffold[x][y-1] == '#':
                        intersects += x*y
            except IndexError:
                continue
print(intersects) 
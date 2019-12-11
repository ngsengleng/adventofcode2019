with open("11.txt") as f:
    code = list(map(str,f.read().split(",")))
code = code + ['0'] * 9999999
output = 0
i,a,b = 0,0,0
rBase = 0
coords = {(0 + 0j):1}  
turn_left = {"up":"left","left":"down","down":"right","right":"up"}
turn_right = {"up":"right","right":"down","down":"left","left":"up"}
move = {"up":1j,"left":-1,"down":-1j,"right":1}
curr_pos = (0 + 0j)
curr_dir = "up"
first = 0
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
        inpt = coords[curr_pos]
        code[addr[0]] = inpt
        i += 2
    elif opcode == 4:                        
        output = str(code[addr[0]])
        if first == 0:
            first = 1
            coords[curr_pos] = output
        elif first == 1:
            first = 0
            if output == '1':
                curr_dir = turn_right[curr_dir]
            elif output == '0':
                curr_dir = turn_left[curr_dir]
            curr_pos += move[curr_dir]
            if curr_pos not in coords:
                coords[curr_pos] = '0'
        #print(output)
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


hull = [ [" "] * 45 for i in range(6)]
for i in coords:
    if coords[i] == '1':
        hull[-int(i.imag)][int(i.real)] = "#"

for x in hull:
    print(x)

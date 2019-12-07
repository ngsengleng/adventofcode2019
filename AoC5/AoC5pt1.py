with open("AoC5.txt") as f:
    code = list(map(str,f.read().split(",")))

inpt = 1
output = 0
i,a,b = 0,0,0 # a and b are parameters
#part1


while True:
    opcode = int(code[i][-2:])
    if opcode == 99:                                    
        break
    elif opcode == 3:                                   
        code[int(code[i+1])] = inpt
        i += 2
    elif opcode == 4:
        if len(code[i]) == 3:
            if code[i][-3] == "1":
                output = code[i+1]
            else:                         
                output = code[int(code[i+1])]
        else:
            output = code[int(code[i+1])]
        print(output)
        i += 2
    else:                
        if len(code[i]) == 3:
            if code[i][-3] == "1":
                a = int(code[i+1])
            else:
                a = int(code[int(code[i+1])])
            b = int(code[int(code[i+2])])
        elif len(code[i]) == 4:
            if code[i][-3] == "1":
                a = int(code[i+1])
            else:
                a = int(code[int(code[i+1])])
            if code[i][-4] == "1":
                b = int(code[i+2])
            else:
                b = int(code[int(code[i+2])])
        else:
                a = int(code[int(code[i+1])])
                b = int(code[int(code[i+2])])
        if opcode == 1:
            code[int(code[i+3])] = str(a + b)
        else:
            code[int(code[i+3])] = str(a * b)
        i += 4
    
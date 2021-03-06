from itertools import permutations
with open("AoC7.txt") as f:
    code = list(map(str,f.read().split(",")))

thrusters = ['a','b','c','d','e',]
phase = ['0','1','2','3','4']
phasePerm = list(map(list,list(permutations(phase))))
signal= []

for n in phasePerm:
    inpt,phaseSetting = '0','0'
    output = 0
    for amp in thrusters:
        i,a,b = 0,0,0
        firstInput = 1
        phaseSetting = n[thrusters.index(amp)]
        if amp != 'a':
            inpt = output
        while True:
            opcode = int(code[i][-2:])
            if  opcode == 99:
                signal.append(int(output))                                    
                break
            elif opcode == 3:
                if firstInput == 1:
                    code[int(code[i+1])] = phaseSetting
                    firstInput = 0
                else:
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
                    i += 4
                elif opcode == 2:
                    code[int(code[i+3])] = str(a * b)
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
                        code[int(code[i+3])] = 1
                    else:
                        code[int(code[i+3])] = 0
                    i += 4
                elif opcode == 8:
                    if a == b:
                        code[int(code[i+3])] = 1
                    else:
                        code[int(code[i+3])] = 0
                    i += 4
print(sorted(signal)[len(signal)-1])
from itertools import permutations
with open("AoC7.txt") as f:
    prog = list(map(str,f.read().split(",")))
prog_list = {}
thrusters = ['a','b','c','d','e']
phase = ['5','6','7','8','9']
phasePerm = list(map(list,list(permutations(phase))))
signal= []
last_op = {}
for n in phasePerm:
    prog_list['a'] = prog.copy()
    prog_list['b'] = prog.copy()
    prog_list['c'] = prog.copy()
    prog_list['d'] = prog.copy()
    prog_list['e'] = prog.copy()
    i = 0
    loop = 0
    inpt,phaseSetting = '0','0'
    output = '0'
    last_op.clear()
    done = False
    while not done:
        for amp in thrusters:
            code = prog_list[amp]
            if loop != 0:
                i = last_op[amp]
            else:
                phaseSetting = n[thrusters.index(amp)]
                firstIn = 1
                i = 0
            a,b = 0,0
            inpt = output
            while True:
                opcode = int(code[i][-2:])
                if opcode == 99:
                    if amp == 'e':
                        signal.append(int(output)) 
                        done = True                                   
                    break
                elif opcode == 3:
                    if loop == 0 and firstIn == 1:
                        code[int(code[i+1])] = phaseSetting
                        firstIn = 0
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
                    last_op[amp] = i
                    break
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
        loop += 1
print(sorted(signal)[len(signal)-1])
print(last_op,loop)
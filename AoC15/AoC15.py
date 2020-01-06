with open("15.txt") as f:
    code = list(map(str,f.read().split(",")))
code = code + ['0'] * 9999999
curr_pos = (0 + 0j)
#direction = {'N': 1, 'S': 2, 'E': 3, 'W': 4}
move = {1: 1j, 2: -1j, 3: 1, 4: -1}
graph = {}

def computer(curr_pos,inpt):
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
            code[addr[0]] = str(inpt)
            i += 2
        elif opcode == 4:
            #points in direction from next to previous node
            #only main line is considered
            next_pos = curr_pos + move[inpt]                 
            output = int(code[addr[0]])
            if output == 2:
                if next_pos not in graph:
                    graph[next_pos] = curr_pos
                curr_pos = next_pos
                break
            elif output == 0:  
                if inpt == 1:
                    inpt = 3
                elif inpt == 2:
                    inpt = 4
                elif inpt == 3:
                    inpt  = 2
                elif inpt == 4:
                    inpt = 1
            elif output == 1:
                if next_pos not in graph:
                    graph[next_pos] = curr_pos
                curr_pos = next_pos
                if inpt == 1:
                    inpt = 4
                elif inpt == 2:
                    inpt = 3
                elif inpt == 3:
                    inpt  = 1
                elif inpt == 4:
                    inpt = 2
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
    return curr_pos

curr_pos = computer(curr_pos,1)

count = 0
def pathing(current):
    global count
    destination = (0 + 0j)
    if graph[current] != destination:
        count += 1
        pathing(graph[current])

pathing(12-18j)
print(count+1)
flipped = {}

#part2
for key, value in graph.items(): 
    if value not in flipped: 
        flipped[value] = [key] 
    else: 
        flipped[value].append(key) 

max_length = []
counter = 0
#for finding time taken to fill dead ends
def dead_ends(current,counter):
    try:
        counter += 1
        next_loc = flipped[current]
        for x in next_loc:
            dead_ends(x,counter)
    except KeyError:
        max_length.append(counter)

#time taken for main path
def main_path(current):
    global counter
    try:
        counter += 1
        next_loc = graph[current]
        if len(flipped[next_loc]) > 1:
            for x in flipped[next_loc]:
                if x == current:
                    continue
                else:
                    dead_ends(x,counter)
        main_path(graph[current])
    except KeyError:
        max_length.append(counter)

main_path(curr_pos)
print(sorted(max_length,reverse=True)[0])
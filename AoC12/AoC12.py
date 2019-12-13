from operator import add
from copy import deepcopy
from functools import reduce
from math import gcd
with open("12.txt") as f:
    scan = f.readlines()
scan = [x.strip().replace("<","").replace(">","").replace(" ","") for x in scan]
scan = [x.split(",") for x in scan]

moons = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
speed = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

for i in range(4):
    for j in range(3):
        moons[i][j] = int(scan[i][j][2:])
coords_initial = []
for i in range(3):
    coords_initial.append([moons[0][i],moons[1][i],moons[2][i],moons[3][i],0,0,0,0])
coords = deepcopy(coords_initial)
period = [0,0,0]
steps = 0
#movement of moons
for j in range(3):
    while True:
        moon = 0
        ptr = 0
        while moon != 4:
            ptr += 1
            if ptr >= 4:
                moon += 1    
            for i in range(3):
                if ptr == moon:
                    continue
                if ptr >= 4:
                    ptr = 0
                pos = moons[moon][i]
                cmpr = moons[ptr][i]
                if pos > cmpr:
                    speed[moon][i] -= 1
                elif pos < cmpr:
                    speed[moon][i] += 1
                else:
                    continue
        steps += 1
        for x in range(4):
            moons[x] = list(map(add,moons[x],speed[x]))
        for a in range(3):
            for b in range(4):
                coords[a][b] = moons[b][a]
                coords[a][b+4] = speed[b][a]
        if coords[j] == coords_initial[j]:
            period[j] = steps
            break

total = 0
#finding total energy
for i in range(4):
    ke = 0
    pe = 0
    for j in range(3):
        ke += abs(speed[i][j])
        pe += abs(moons[i][j])
    total += ke*pe
print(total)

# adapted from https://stackoverflow.com/questions/37237954/calculate-the-lcm-of-a-list-of-given-numbers-in-python
#user TakingItCasual
def lcm(lst):
    return reduce(lambda a,b: a*b // gcd(a,b), lst)

print(lcm(period))
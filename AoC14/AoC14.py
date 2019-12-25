import re
from math import ceil
with open("14.txt") as f:
    rxn = [x.strip().replace(",","") for x in f.readlines()]
rxn = [re.split("\s",x) for x in rxn]
for x in rxn:
    x.remove('=>')

factory = {}
for x in rxn:
    for i in range(len(x)):
        if x[len(x)-1] not in factory:
            factory[x[len(x)-1]] = []
            factory[x[len(x)-1]].append(int(x[len(x)-2]))
        if i >= len(x)-2 or i%2 != 0:
            continue
        else:
            factory[x[len(x)-1]].append((x[i],x[i+1]))

ore = 0
leftovers = {}
ore_count = 1

def process(ore_count,a,b):
    global ore
    buffer1 = ore_count * b
    if a[1] in leftovers:    
        if buffer1 > leftovers[a[1]]:
            ore_count = buffer1 - leftovers[a[1]]
            leftovers[a[1]] = 0
        elif buffer1 < leftovers[a[1]]:
            leftovers[a[1]] -= buffer1
            ore_count = buffer1 = 0
        else:
            buffer1 = ore_count = leftovers[a[1]] = 0
    else:
        ore_count = buffer1

    for x in factory[a[1]]:
        if isinstance(x,int):
            buffer2 = ceil(ore_count / x)
            if buffer2*x > ore_count:
                if a[1] not in leftovers:
                    leftovers[a[1]] = 0
                leftovers[a[1]] += buffer2*x - ore_count
            ore_count = buffer2
        else:
            if 'ORE' in x:
                ore += ore_count*int(factory[a[1]][1][0])
            else:
                process(ore_count,x,int(x[0]))
            


final = factory['FUEL'].copy()
trillion = 1000000000000
    

min_fuel,max_fuel = 1, 1275681*2
while min_fuel <= max_fuel:
    mid = (min_fuel + max_fuel) // 2
    leftovers.clear()
    final[0] = (mid,'FUEL')
    for x in final:
        ore_count = 1
        if isinstance(x,int):
            continue
        else:
            process(ore_count,x,int(x[0]))
    print(mid,ore,min_fuel,max_fuel)
    if ore > trillion:
        max_fuel = mid - 1
    elif ore <= trillion:
        min_fuel = mid + 1
    ore = 0

print(mid + 1)


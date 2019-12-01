import math

#setup
with open(r"AoC1.txt") as f:
    lines = f.readlines()
    lines = map(int, map(lambda x: x.strip(), lines))
    lines = list(lines)

#part1
total = 0
for line in lines:
    total += math.floor(line/3)-2  
print(total)

#part2
total = 0

for line in lines:
    while line > 0:
        out = math.floor(line/3)-2
        if out > 0:
            total = total + out
        line = out
print(total)

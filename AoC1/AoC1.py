import math

#setup
with open(r"AoC1.txt") as f:
    lines = f.readlines()
    lines[:] = [line.strip("\n") for line in lines]
    lines[:] = [int(line) for line in lines]

#part1
sum = 0
for line in lines:
    out = math.floor(int(line)/3)-2
    sum = sum + out
print(sum)

#part2
sum = 0
for line in lines:
    while line > 0:
        out = math.floor(int(line)/3)-2
        if out > 0:
            sum = sum + out
        line = out
print(sum)

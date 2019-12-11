import math

with open("AoC10.txt") as f:
    maps = [x.strip() for x in f.readlines()]
print(maps)

#locations of asteroids
coords = []
for y in range(len(maps)):
    for x in range (len(maps[y])):
        if maps[y][x] == "#":
            coords.append((x,y))
angles = []
longest = 0
prev_base = None
final_base = None
#all asteroids in sight
for a in coords:
    if len(angles) == 0:
        longest = len(angles)
        final_base = prev_base
    elif longest < len(angles):
        longest = len(angles)
        final_base = prev_base
    angles.clear()
    for b in coords:
        if a == b:
            continue
        opp = b[1] - a[1]
        adj = b[0] - a[0]
        try:
            angle = math.atan2(opp,adj)
        except ZeroDivisionError:
            angle = 90
        if angle not in angles:
            angles.append(angle)
    prev_base = a
print(longest, final_base)
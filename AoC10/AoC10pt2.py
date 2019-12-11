from math import atan2,pi
with open("AoC10.txt") as f:
    maps = [x.strip() for x in f.readlines()]

#locations of asteroids
coords = []
for y in range(len(maps)):
    for x in range (len(maps[y])):
        if maps[y][x] == "#":
            coords.append([x,y])

base = [13,17]
angles = set()
distance = {}
ans = []
#finding all possible angles in order
for a in coords:
    if a != base:
        opp = a[1] - base[1]
        adj = a[0] - base[0]
        dist = abs(opp) + abs(adj)
        try:
            angle = atan2(-opp,adj)
        except ZeroDivisionError:
            if opp > 0:
                angle = pi/2
            else:
                angle = -pi/2
        if angle > pi/2:
            angle -= 2*pi
        angles.add(angle)
        if angle in distance:
            distance[angle].append(dist)
        else:
            distance[angle] = []
            distance[angle].append(dist)
        ans.append([dist,a,angle])
angles = sorted(angles,reverse = True)

for i in distance:
    distance[i] = sorted(distance[i])
x = 0
count = 0
store1,store2 = 0,0
while True:
    copy = angles.copy()
    for i in copy:
        try:
            distance[i][x]
            count += 1
            if count == 200:
                store1 = i
                store2 = distance[i][x]
                break
        except IndexError:
            continue
    if count == 200:
        break
    x += 1
for i in ans:
    if store1 in i and store2 in i:
        print(i)
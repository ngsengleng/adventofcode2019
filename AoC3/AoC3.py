with open("AoC3.txt") as f:
    coords = list(f.read().split("\n"))
    line1 = coords[0].split(",")
    line2 = coords[1].split(",")

x1,y1 = 0,0 #define beginning coordinates
x2,y2 = 0,0
coord1 = set()
coord2 = set()

#part1
#storing all coordinates passed through by line 1
for n in range (len(line1)):
    move = line1[n]  
    direction, length = move[0],int(move[1:])
    if direction == 'L':
        for x in range(length):
            x1 -= 1
            coord1.add((x1,y1))
    elif direction == 'R':
        for x in range(length):
            x1 += 1
            coord1.add((x1,y1))
    elif direction == 'U':
        for x in range(length):
            y1 += 1
            coord1.add((x1,y1))
    elif direction == 'D':
        for x in range(length):
            y1 -= 1
            coord1.add((x1,y1))

#storing all coordinates passed through by line 2
for n in range (len(line2)):
    move = line2[n]  
    direction, length = move[0],int(move[1:])
    if direction == 'L':
        for x in range(length):
            x2 -= 1
            coord2.add((x2,y2))
    elif direction == 'R':
        for x in range(length):
            x2 += 1
            coord2.add((x2,y2))
    elif direction == 'U':
        for x in range(length):
            y2 += 1
            coord2.add((x2,y2))
    elif direction == 'D':
        for x in range(length):
            y2 -= 1
            coord2.add((x2,y2))

#finding intersects
intersections  = coord1.intersection(coord2)
def manhattan_dist(x):
    return (abs(x[0]) + abs(x[1]))
manhattanDist = sorted(map(manhattan_dist,intersections))
print(manhattanDist[0]) 

#part2
sums = list()
for coord in intersections:
    a = coord[0]
    b = coord[1]
    x1,y1,x2,y2 = 0,0,0,0
    total = 0
    for n in range (len(line1)):
        move = line1[n]  
        direction, length = move[0],int(move[1:])
        if x1 == a and y1 == b:
            break
        if direction == 'L':
            for x in range(length):
                x1 -= 1
                total += 1
                if x1 == a and y1 == b:
                    break
        elif direction == 'R':
            for x in range(length):
                x1 += 1
                total += 1
                if x1 == a and y1 == b:
                    break
        elif direction == 'U':
            for x in range(length):
                y1 += 1
                total += 1
                if x1 == a and y1 == b:
                    break
        elif direction == 'D':
            for x in range(length):
                y1 -= 1
                total += 1
                if x1 == a and y1 == b:
                    break
    
    for n in range (len(line2)):
        move = line2[n]  
        direction, length = move[0],int(move[1:])
        if x2 == a and y2 == b:
            break
        if direction == 'L':
            for x in range(length):
                x2 -= 1
                total += 1
                if x2 == a and y2 == b:
                    break
        elif direction == 'R':
            for x in range(length):
                x2 += 1
                total += 1
                if x2 == a and y2 == b:
                    break
        elif direction == 'U':
            for x in range(length):
                y2 += 1
                total += 1
                if x2 == a and y2 == b:
                    break
        elif direction == 'D':
            for x in range(length):
                y2 -= 1
                total += 1
                if x2 == a and y2 == b:
                    break
    sums.append(total)
print(sorted(sums))        
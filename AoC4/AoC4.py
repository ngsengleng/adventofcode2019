#part1
count = 0
for n in range (245183,790572):
    n = list(str(n))
    m = sorted(n)
    if m == n:
        for x in range(len(n)):
            if (x+1) == len(n):
                break
            if n[x+1] == n[x]:
                count += 1
                break     
print(count)

#part2
count = 0
for n in range (245183,790572):
    n = list(str(n))
    m = sorted(n)
    if m == n:
        double = 0
        m = set(n)
        for i in m:
            if n.count(i) == 2:
                double += 1
        if double != 0:
            count += 1
print(count)
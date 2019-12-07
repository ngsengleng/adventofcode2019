with open("AoC6.txt") as f:
    pairs = f.readlines()
orbits = {}
for x in pairs:
    a,b = x.strip().split(")")
    if a not in orbits:
        orbits[a] = []
    orbits[a].append(b)
#print(orbits)
count = 0
ans = 0
def trace(node,count):
    global ans 
    #print(count, ans)
    ans += count
    for x in node:
        if x in orbits:
            #print(x)
            trace(orbits[x], count+1)
        else:
            ans += count+1
            #print(x)
            #print("end")


trace(orbits['COM'],count)
print(ans)
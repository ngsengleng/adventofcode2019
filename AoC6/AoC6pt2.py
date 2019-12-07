with open("AoC6.txt") as f:
    pairs = f.readlines()
orbits = {}
for x in pairs:
    a,b = x.strip().split(")")
    if b not in orbits:
        orbits[b] = []
    orbits[b].append(a)
print(orbits)

you_list = []
san_list = []

def trace_you(node):
    for x in node:
        if x in orbits:
            you_list.append(x)
            trace_you(orbits[x])

def trace_san(node):
    for x in node:
        if x in orbits:
            san_list.append(x)
            trace_san(orbits[x])
trace_you(orbits['YOU'],)
trace_san(orbits['SAN'])

distance = []
while True:
    if len(san_list) < len(you_list):
        for n in san_list:
            if n in you_list:
                distance.append(san_list.index(n) + you_list.index(n))
    else:
        for n in you_list:
            if n in san_list:
                distance.append(san_list.index(n) + you_list.index(n))
    break
print(sorted(distance)[0]) 
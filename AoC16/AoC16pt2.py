with open("16.txt") as f:
    number = f.read().strip()
offset = int(number[0:7])
number = list(number * 10000)
number.reverse()
phase = 100
output = ['0'] * len(number)

for i in range(phase):
    if i == 0:
        inpt = number.copy()
    else:
        inpt = output.copy()
    total = 0
    for x in range(len(number) - offset):
        total += int(inpt[x])
        output[x] = abs(total) % 10

output.reverse()
print(output[offset:offset+8])
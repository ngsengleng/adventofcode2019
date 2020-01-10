with open("test.txt") as f:
    number = f.read().strip()
base = [0,1,0,-1]
output = ['0'] * len(number)
phase = 40
for i in range(phase):
    if i == 0:
        inpt = number
    else:
        inpt = output.copy()
    for x in range(len(inpt)):
        total = 0
        base_count = 0
        pos_count = 0
        for y in range(len(inpt)):
            digit = int(inpt[y])
            if y == 0:
                pos_count += 1
            if pos_count == x + 1:
                base_count += 1
                pos_count = 0
                if base_count == 4:
                    base_count = 0
            total += digit*base[base_count]
            pos_count += 1
        output[x] = abs(total)%10
    print(output)


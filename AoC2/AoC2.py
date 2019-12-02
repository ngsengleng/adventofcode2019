#part1
with open(r"AoC2.txt") as f:
    numbers = list(map(int,f.read().split(",")))

numbers2 = numbers.copy() #for part2
numbers[1] = 12
numbers[2] = 2

x = 0
def part1(numbers,x):
    while numbers[x] != 99:
        if numbers[x] == 1:
            numbers[numbers[x+3]] = numbers[numbers[x+1]] + numbers[numbers[x+2]]
        if numbers[x] == 2:
            numbers[numbers[x+3]] = numbers[numbers[x+1]] * numbers[numbers[x+2]]
        x += 4
part1(numbers,x)
print(numbers[0])

#part2
cNumbers = numbers2.copy()
for a in range (0,100):
    for b in range(0,100):
        cNumbers[1] = a
        cNumbers[2] = b
        x = 0
        part1(cNumbers,x)
        if cNumbers[0] != 19690720:
            cNumbers = numbers2.copy()
        else:
            sumz = 100*a+b
            print(sumz)
            exit(0)

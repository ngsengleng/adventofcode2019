from functools import reduce
from collections import defaultdict
with open("AoC8.txt") as f:
    image = str(f.read())
width = 25
height = 6
size = width*height
imageFile = [image[i:i+size] for i in range(0,len(image),size)]
zeroes = reduce(lambda a,b: a if a.count("0") < b.count("0") else b,imageFile)
print(zeroes.count("1")*zeroes.count("2"))

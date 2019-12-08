from functools import reduce
from collections import defaultdict
with open("AoC8.txt") as f:
    image = str(f.read())
width = 25
height = 6
size = width*height
imageFile = [image[i:i+size] for i in range(0,len(image),size)]
zeroes = reduce(lambda a,b: a if a.count("0") < b.count("0") else b,imageFile)
#reduce takes in the first two iterables from imageFile,passes into lambda
#it then passes into lambda the result of previous lambda call and next iterable of imageFile
#cycle continues until imageFile is exhausted
print(zeroes.count("1")*zeroes.count("2"))

from collections import defaultdict
with open("AoC8.txt") as f:
    image = str(f.read())
width = 25
height = 6
size = width*height
imageFile = defaultdict(list)
zeros,ones,twos,imageCount = 0,0,0,0
prev = 0
key = 0
ans = 0

for i in range(0,len(image),size):
    imageCount += 1
    img = image[i:i+size]
    zeros = img.count("0")
    ones = img.count("1")
    twos = img.count("2")
    imageFile[imageCount] = [zeros,ones,twos]


for i in imageFile:
    img = imageFile.get(i)
    if i == 1:
        prev = img[0]
    if img[0] <= prev:
        key = i
        prev = img[0]
        ans = img[1]*img[2]

  
print(key,ans)



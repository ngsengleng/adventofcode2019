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

for i in range(len(image)):
    if i%size == 0:
        imageCount += 1
        zeros,ones,twos = 0,0,0
    if image[i] == '0':
        zeros += 1
    elif image[i] == '1':
        ones += 1
    else:
        twos += 1            
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

with open("AoC8.txt") as f:
    image = str(f.read())
width = 25
height = 6
size = width*height
final = []
for i in range(size):
    while i < len(image):
        pixel = image[i]
        if pixel == '2':
            i += size
        else:
            if pixel == '0':
                pixel = '.'
            if pixel == '1':
                pixel = 'x'
            final.append(pixel)
            i += size
            break

for i in range(150):
    if (i+1)%25 == 0:
        print(final[i])
    else:
        print(final[i], end=" ")
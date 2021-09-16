from PIL import Image

imgPath = input("Enter path to a picture: ")

image = Image.open(imgPath)
obj = image.load()

sizeX = image.size[0]
RGBCode = []
text = ""
prevPix = image.getpixel((0, 0))

for x in prevPix:
    RGBCode.append(x)

for i in range(1, sizeX):
    curPix = image.getpixel((i, 0))
    if curPix != prevPix:
        for x in curPix:
            RGBCode.append(x)
        prevPix = curPix

for i in RGBCode:
    if i == 255:
        text += " "
    else:
        text += chr(i)

print(f"Coded text: {text}")

# textToImg.png
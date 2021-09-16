from PIL import Image, ImageDraw

text = input("Input text: ")
textHEX = []

text = list(text)

for i in range(len(text)):
    if text[i] == " ":
        textHEX.append(255)
    else:
        textHEX.append(ord(text[i]))


while len(textHEX) % 3 != 0:
    textHEX.append(255)

imgSizeX, imgSizeY = 200, 200
rectSizeX = (imgSizeX // (len(textHEX) // 3))
img = Image.new("RGB", (imgSizeX, imgSizeY), "white")
idraw = ImageDraw.Draw(img)

c = 0
for i in range(0, len(textHEX), 3):
    idraw.rectangle((c * rectSizeX, 0, c * rectSizeX + rectSizeX, imgSizeY), fill=(textHEX[i], textHEX[i + 1], textHEX[i + 2]))
    c += 1

img.save('textToImg.png')

print("Done! Your text was coded into textToImg.png")
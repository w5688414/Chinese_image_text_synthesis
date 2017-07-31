from PIL import Image

im = Image.open('output/images/0.jpg')
# im.show()
print(im.size)
print(im.mode)
print(im.format)
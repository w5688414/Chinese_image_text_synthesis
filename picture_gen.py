from PIL import Image
import matplotlib.pyplot as plt
import os



# img=Image.open('images/background.jpg')
img = Image.new("RGB", (512, 512), "white")
img=img.resize((800, 600), Image.ANTIALIAS)
for i in range(0,1000):
    imgname=str(i)+'.jpg'
    print(imgname)
    img.save(os.path.join('images',imgname))

# plt.figure("background")
# plt.imshow(img)
# plt.show()


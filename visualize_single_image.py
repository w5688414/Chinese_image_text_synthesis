from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2

picPath=r"output\images\0.jpg"
txtPath=r"output\groundTruth\0.txt"
img=Image.open(picPath)
im = np.array(img)
with open(txtPath,'r') as txtfile:
    for txt in txtfile.readlines():
        txtArr=txt.split()
        print(txtArr)
        x1=int(txtArr[0])
        y1=int(txtArr[1])
        x2=int(txtArr[2])
        y2=int(txtArr[3])
        cv2.rectangle(im,(x1,y1),(x2,y2),(255,0,0))


# img.show()
plt.figure("demo")
plt.imshow(im)
plt.show()
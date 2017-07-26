from PIL import Image
import matplotlib.pyplot as plt
import os
import numpy as np
from PIL import ImageFont
from PIL import ImageDraw
import cv2

from synthgen import TextRegions
from text_utils import TextSource, FontState

class ImageTextBoxFactory(object):

    def __init__(self):
        self.boxInfo=[]

    def add_text_to_image(self,region_dict,text,img,FS):
        # font = ImageFont.truetype('data/fonts/HYPPTiJ.ttf', 20)
        draw = ImageDraw.Draw(img)
        x=region_dict['x']
        y=region_dict['y']

        font=FS.sample()
        draw.text((x, y), text,(0, 0, 0), font=font)
        offsetx, offsety = font.getoffset(text)
        width, height = font.getsize(text)
        im = np.array(img)
        cv2.rectangle(im, (offsetx + x, offsety + y), (offsetx + x + width, offsety + y + height), (255, 0, 0),
                      1)  # 绘出矩形框
        dict={}
        dict['startX']=offsetx + x
        dict['startY']=offsety + y
        dict['endX']=offsetx + x + width
        dict['endY']=offsety + y + height
        dict['text']=text
        self.boxInfo.append(dict)
        # plt.figure('demo')
        # plt.imshow(im)
        # plt.show()
    def showResults(self):
        print(self.boxInfo)

    def output(self):
        with open("output/groundTruth/example.txt", "w") as file:
            for dict in self.boxInfo:
                lineText = "%s %s %s %s %s\n" % (
                dict['startX'], dict['startY'], dict['endX'], dict['endY'], dict['text'])
                file.write(lineText)
def main():
    ITBF=ImageTextBoxFactory()
    textSource = TextSource(r'data\words/')
    img = Image.new("RGB", (512, 512), "white")
    img = img.resize((600, 400), Image.ANTIALIAS)
    textRegion = TextRegions()
    FS = FontState()
    for i in range(0,20):
        word = textSource.sample_word()
        region_dict = textRegion.get_regions(img)
        ITBF.add_text_to_image(region_dict, word, img,FS)
    imgname = "example" + '.jpg'
    print(imgname)
    img.save(os.path.join('output/images', imgname))
    ITBF.showResults()



if __name__ == '__main__':
    main()
    # for i in range(0,10):
    #     imgname=str(i)+'.jpg'
    #     print(imgname)
    #     img.save(os.path.join('output/images',imgname))

    # plt.figure("background")
    # plt.imshow(img)
    # plt.show()


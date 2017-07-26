from PIL import Image
import matplotlib.pyplot as plt
import os
import numpy as np
from PIL import ImageFont
from PIL import ImageDraw
import cv2

from synthgen import TextRegions
from text_utils import TextSource


def add_text_to_image(region_dict,text,img):
    font = ImageFont.truetype('data/fonts/HYPPTiJ.ttf', 20)
    draw = ImageDraw.Draw(img)
    x=region_dict['x']
    y=region_dict['y']
    draw.text((x, y), text,(0, 0, 0), font=font)
    offsetx, offsety = font.getoffset(text)
    width, height = font.getsize(text)
    im = np.array(img)
    cv2.rectangle(im, (offsetx + x, offsety + y), (offsetx + x + width, offsety + y + height), (255, 0, 0),
                  1)  # 绘出矩形框
    plt.figure('demo')
    plt.imshow(im)
    plt.show()

if __name__ == '__main__':
    textSource = TextSource(r'data\words/')
    word=textSource.sample_word()

    # img=Image.open('images/background.jpg')
    img = Image.new("RGB", (512, 512), "white")
    img=img.resize((800, 600), Image.ANTIALIAS)
    textRegion = TextRegions()
    region_dict=textRegion.get_regions(img)
    add_text_to_image(region_dict,word,img)
    # for i in range(0,10):
    #     imgname=str(i)+'.jpg'
    #     print(imgname)
    #     img.save(os.path.join('output/images',imgname))

    # plt.figure("background")
    # plt.imshow(img)
    # plt.show()


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

    def visualize_imaage(self,index):
        '''
        visualize the image
        :param index:
        :return:
        '''
        imgname=str(index) + '.jpg'
        txtname = str(index) + ".txt"
        picPath =os.path.join( r"output\images",imgname)
        txtPath = os.path.join(r"output\groundTruth",txtname)

        img = Image.open(picPath)
        im = np.array(img)
        with open(txtPath, 'r') as txtfile:
            for txt in txtfile.readlines():
                txtArr = txt.split()
                print(txtArr)
                x1 = int(txtArr[0])
                y1 = int(txtArr[1])
                x2 = int(txtArr[2])
                y2 = int(txtArr[3])
                cv2.rectangle(im, (x1, y1), (x2, y2), (255, 0, 0))

        plt.figure("example")
        plt.imshow(im)
        plt.show()

    def output(self,index):
        '''
        output the  coordinate of objects in this picture
        :param index:
        :return:
        '''
        filename=str(index)+".txt"
        imgname=str(index)+".jpg"
        output_txt_path="output/groundTruth"
        if(not os.path.exists(output_txt_path)):
            os.makedirs(output_txt_path)
        path=os.path.join(output_txt_path,filename)
        with open(path, "w") as file:
            for dict in self.boxInfo:
                # uncomment the line below if you want the VOC2007 groundtruth format
                VOC2007LineText="%s %s %s %s %s %s\n" % (imgname, dict['text'],
                dict['startX'], dict['startY'], dict['endX'], dict['endY'])
                file.write(VOC2007LineText)

                #uncomment the line below if you want the ICDAR groundtruth format
                # ICDARLineText = "%s %s %s %s %s\n" % (
                # dict['startX'], dict['startY'], dict['endX'], dict['endY'], dict['text'])
                # file.write(ICDARLineText)


    def clear(self):
        '''
        clear the old data
        :return:
        '''
        self.boxInfo.clear()

def main():

    textSource = TextSource(r'data/words/')
    textRegion = TextRegions()
    FS = FontState()
    maxNumImages=10
    for i in range(0,maxNumImages):
        ITBF = ImageTextBoxFactory()
        img = Image.new("RGB", (512, 512), "white")
        img = img.resize((600, 400), Image.ANTIALIAS)
        generateData(FS, ITBF, img, textRegion, textSource,i)

    print("total image number:%s" %(maxNumImages))



def generateData(FS, ITBF, img, textRegion, textSource,index):
    for i in range(0, 20):
        word = textSource.sample_word()
        region_dict = textRegion.get_regions(img)
        ITBF.add_text_to_image(region_dict, word, img, FS)
    imgname = str(index) + '.jpg'
    print(imgname)
    output_path='output/images'
    if(not os.path.exists(output_path)):
        os.makedirs(output_path)
    img.save(os.path.join(output_path, imgname))
    ITBF.output(index)
    # ITBF.visualize_imaage(index)


if __name__ == '__main__':
    main()
    # for i in range(0,10):
    #     imgname=str(i)+'.jpg'
    #     print(imgname)
    #     img.save(os.path.join('output/images',imgname))

    # plt.figure("background")
    # plt.imshow(img)
    # plt.show()


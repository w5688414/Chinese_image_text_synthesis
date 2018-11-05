import os
import cv2
import xml.etree.ElementTree as ET
import numpy as np
from xml.dom.minidom import Document
import shutil

from PIL import Image


class formatConverter(object):



    def convert_voc(self,input_path,output_path):

        if(not os.path.exists(output_path)):
            os.mkdir(output_path)
            print("%s created" % (output_path))
            # return

        data_path=os.path.join(output_path,'VOC2007')

        if(not os.path.exists(data_path)):
            os.makedirs(data_path)

        annot_path = os.path.join(data_path, 'Annotations')
        imgs_path = os.path.join(data_path, 'JPEGImages')
        imgsets_path=os.path.join(data_path,'ImageSets', 'Main')
        if(not os.path.exists(imgsets_path)):
            os.makedirs(imgsets_path)
        imgsets_path_train = os.path.join(imgsets_path, 'trainval.txt')
        imgsets_path_test = os.path.join(imgsets_path, 'test.txt')

        if(not os.path.exists(annot_path)):
            os.makedirs(annot_path)
        if(not os.path.exists(imgs_path)):
            os.makedirs(imgs_path)

        input_img_path=os.path.join(input_path,"images")

        listimages=os.listdir(input_img_path)
        with open(imgsets_path_train,'w') as f:
            for imagefile in listimages:
                f.write(imagefile+"\n")
        with open(imgsets_path_test,'w') as f:
            for imagefile in listimages:
                f.write(imagefile + "\n")

        input_groundtruth_path=os.path.join(input_path,'groundTruth')
        groundTruths=os.listdir(input_groundtruth_path)
        for singleGround in groundTruths:
            txt_file_path=os.path.join(input_groundtruth_path,singleGround)
            print(txt_file_path)
            with open(txt_file_path,'r') as f:
                files=f.readlines()
                self.write_to_xml(files,annot_path,input_img_path,imgs_path)

    def write_to_xml(self,files, annot_path,input_img_path,out_img_path):
        img_name=files[0].strip().split()[0]
        print(img_name)
        ## copy image
        srt_path=os.path.join(input_img_path,img_name)
        dst_path=os.path.join(out_img_path,img_name)
        shutil.copy(srt_path,dst_path)

        # prepare xml file
        doc = Document()
        annotation = doc.createElement('annotation')
        doc.appendChild(annotation)

        folder = doc.createElement('folder')
        folder.appendChild(doc.createTextNode('VOC 2007'))
        annotation.appendChild(folder)

        filename = doc.createElement("filename")
        filename.appendChild(doc.createTextNode(img_name))
        annotation.appendChild(filename)

        input_img_file_path = os.path.join(input_img_path, img_name)
        img = cv2.imread(input_img_file_path)
        width = img.shape[0]
        height = img.shape[1]
        depth = img.shape[2]


        sizeimage = doc.createElement("size")
        imagewidth = doc.createElement("width")
        imageheight = doc.createElement("height")
        imagedepth = doc.createElement("depth")

        imagewidth.appendChild(doc.createTextNode(str(width)))
        imageheight.appendChild(doc.createTextNode(str(height)))
        imagedepth.appendChild(doc.createTextNode(str(depth)))

        sizeimage.appendChild(imagewidth)
        sizeimage.appendChild(imageheight)
        sizeimage.appendChild(imagedepth)

        annotation.appendChild(sizeimage)

        for lineFile in files:
            arrayFile = lineFile.strip().split()

            object = doc.createElement('object')
            name = doc.createElement('name')
            truncated = doc.createElement('truncated')
            difficult = doc.createElement('difficult')

            name.appendChild(doc.createTextNode(arrayFile[1]))
            truncated.appendChild(doc.createTextNode("1"))
            difficult.appendChild(doc.createTextNode("0"))

            object.appendChild(name)
            object.appendChild(truncated)
            object.appendChild(difficult)

            bndbox = doc.createElement("bndbox")
            xmin = doc.createElement("xmin")
            ymin = doc.createElement("ymin")
            xmax = doc.createElement("xmax")
            ymax = doc.createElement("ymax")

            x_min=str(arrayFile[2])
            y_min=str(arrayFile[3])
            x_max=str(arrayFile[4])
            y_max=str(arrayFile[5])

            xmin.appendChild(doc.createTextNode(str(x_min)))
            ymin.appendChild(doc.createTextNode(str(y_min)))
            xmax.appendChild(doc.createTextNode(str(x_max)))
            ymax.appendChild(doc.createTextNode(str(y_max)))

            bndbox.appendChild(xmin)
            bndbox.appendChild(ymin)
            bndbox.appendChild(xmax)
            bndbox.appendChild(ymax)

            object.appendChild(bndbox)
            annotation.appendChild(object)

        # 将dom对象写入本地xml文件
        xmlfilename=img_name.split(".")[0]+".xml"
        xmlfilePath=os.path.join(annot_path,xmlfilename)
        output_object = open(xmlfilePath, 'w')
        output_object.write(doc.toprettyxml(indent=' ' * 4))
        output_object.close()


if __name__ == '__main__':
    fc=formatConverter()
    fc.convert_voc("output","output/VOCdevkit")

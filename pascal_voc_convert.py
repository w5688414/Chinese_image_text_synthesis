import os
import cv2
import xml.etree.ElementTree as ET
import numpy as np
from xml.dom.minidom import Document

class formatConverter(object):



    def convert_voc(self,input_path,output_path):
        all_imgs = []

        classes_count = {}

        class_mapping = {}

        visualise = False

        if os.path.exists(output_path)==False:
            print("% not exists" %(output_path))
            return

        data_path=os.path.join(output_path,'VOC2012')

        if os.path.exists(data_path)==False:
            os.makedirs(data_path)

        annot_path = os.path.join(data_path, 'Annotations')
        imgs_path = os.path.join(data_path, 'JPEGImages')
        imgsets_path_trainval = os.path.join(data_path, 'ImageSets', 'Main', 'trainval.txt')
        imgsets_path_test = os.path.join(data_path, 'ImageSets', 'Main', 'test.txt')

        if os.path.exists(annot_path)==False:
            os.makedirs(annot_path)
        if os.path.exists(imgs_path)==False:
            os.makedirs(imgs_path)

        input_img_path=os.path.join(input_path,"images")
        listimages=os.listdir(input_img_path)
        with open(imgsets_path_trainval,'w') as f:
            for imagefile in listimages:
                f.write(imagefile+"\n")
        with open(imgsets_path_test,'w') as f:
            for imagefile in listimages:
                f.write(imagefile + "\n")
        input_groundtruth_path=os.path.join(input_path,'groundTruth')
        groundTruths=os.listdir(input_groundtruth_path)
        for singleGround in groundTruths:
            txt_file_path=os.path.join(input_groundtruth_path,singleGround)
            with open(txt_file_path) as f:
                files=f.readlines()
                self.write_to_xml(files,annot_path)

    def write_to_xml(self,files, annot_path):
        # 创建dom文档
        doc = Document()
        # 创建根节点
        annotation = doc.createElement('annotation')
        # 根节点插入dom树
        doc.appendChild(annotation)

        folder=doc.createElement("folder")
        folder_text=doc.createTextNode("my Data")
        folder.appendChild(folder_text)
        folder.appendChild(folder_text)
        annotation.appendChild(folder)

        flag=True
        imgfilename=''
        for lineFile in files:
            arrayFile=str(lineFile).split()
            print(arrayFile)
            if flag:
                filename = doc.createElement("filename")
                filename_text=doc.createTextNode(arrayFile[0])
                imgfilename=arrayFile[0]
                flag=False
                filename.appendChild(filename_text)
                annotation.appendChild(filename)
            object=doc.createElement('object')
            name=doc.createElement('name')
            name_text=doc.createTextNode(arrayFile[1])
            name.appendChild(name_text)
            object.appendChild(name)

            bndbox=doc.createElement("bndbox")
            xmin=doc.createElement("xmin")
            ymin=doc.createElement("ymin")
            xmax=doc.createElement("xmax")
            ymax=doc.createElement("ymax")

            xmin_text=doc.createTextNode(str(arrayFile[2]))
            ymin_text=doc.createTextNode(arrayFile[3])
            xmax_text=doc.createTextNode(arrayFile[4])
            ymax_text=doc.createTextNode(arrayFile[5])

            xmin.appendChild(xmin_text)
            ymin.appendChild(ymin_text)
            xmax.appendChild(xmax_text)
            ymax.appendChild(ymax_text)

            bndbox.appendChild(xmin)
            bndbox.appendChild(ymin)
            bndbox.appendChild(xmax)
            bndbox.appendChild(ymax)

            object.appendChild(bndbox)
            annotation.appendChild(object)
        # 将dom对象写入本地xml文件
        xmlfilename=imgfilename.split(".")[0]+".xml"
        xmlfilePath=os.path.join(annot_path,xmlfilename)
        with open(xmlfilePath, 'w') as f:
            doc.writexml(f, addindent=' ' * 4, newl='\n', encoding='gbk')


if __name__ == '__main__':
    fc=formatConverter()
    fc.convert_voc("output","output/VOCdevkit")

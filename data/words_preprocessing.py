#coding=utf-8
import codecs
import os

from data import is_chinese


class wordsCodeConvert():


    def getSourceFile(self):
        basePath=r'words'
        listPath=os.listdir(basePath)
        newpathlist=[]
        for path in listPath:
            newpath=os.path.join(basePath,path)
            newpathlist.append(newpath)
        print(newpathlist)
        return newpathlist

    def convertWords(self,listPath):
        for path in listPath:
            print(path)

            f=codecs.open(path,'r','gbk','ignore')
            filepaths = path.split('\\')
            filename=filepaths[-1]
            print(filename)

            output = open(filename, 'w')
            lines = f.readlines() #读取一行数据，转化为中文
            for line in lines:
                # newline=line.encode('utf-8')
                newline= is_chinese.extract_chineseSequence(line)
                print(newline)
                output.write(newline)
                output.write("\n")

            output.close()
            f.close()



if __name__ == '__main__':

    wcc=wordsCodeConvert()
    pathlist=wcc.getSourceFile()
    wcc.convertWords(pathlist)

    # path=r'words/是谁.txt'
    # # path=r'test.txt'
    # upath=unicode(path,'utf-8')
    # f = open(upath,'r')
    #
    # filepaths=path.split('/')
    # filename=filepaths[-1]
    # print(filename)
    #
    # output=open(filename,'w')
    # lines = f.readlines() #读取一行数据，转化为中文
    # for line in lines:
    #     print(line)
    #     output.write(line)
    #     output.write("\n")
    #
    # output.close()
    #
    #
    # f.close()

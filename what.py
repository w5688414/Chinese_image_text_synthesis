#coding=utf-8
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import codecs
import is_chinese

class wordsCodeConvert():


    def getSourceFile(self):
        basePath=r'lyrics'
        listPath=os.listdir(basePath)
        newpathlist=[]
        for path in listPath:
            newpath=os.path.join(basePath,path)
            newpathlist.append(newpath)
        return newpathlist

    def convertWords(self,listPath):
        for path in listPath:
            print(path)
            upath = unicode(path, 'utf-8')
            f=codecs.open(upath,'r','gbk','ignore')
            filepaths = path.split('/')
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

            f.close()
            output.close()



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

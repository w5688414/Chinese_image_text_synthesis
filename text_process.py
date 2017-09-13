import codecs

import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
import os

class text_preprocess(object):
    '''
    reference:http://www.cnblogs.com/WeyneChen/p/6675355.html

    '''
    def get_words_frequency(self):
        """
            Get frequency of words in words_list.
            return a dict.
        """
        file_path=r"data/lyrics/ALLLyrics.txt"
        file_object = codecs.open(file_path, 'r', 'utf-8', 'ignore')
        lines=file_object.readlines()
        word = []
        counter = {}
        for line in lines:
            line = line.strip().replace(' ','') #去掉所有的空格
            if len(line) == 0:
                continue
            for w in line:
                if not w in word:
                    word.append(w)
                if not w in counter:
                    counter[w] = 1
                else:
                    counter[w] += 1
        counter_list = sorted(counter.items(), key=lambda x: x[1], reverse=True)

        #print(counter_list[:50])
        self.output(counter_list)
        '''
        #可视化
        label = list(map(lambda x: x[0], counter_list[:50]))
        value = list(map(lambda y: y[1], counter_list[:50]))

        plt.bar(range(len(value)), value, tick_label=label)
        plt.show()
        '''

    def output(self,counter_list):
        output_dir=r"output/words"
        file_name="words.txt"
        output_path=os.path.join(output_dir,file_name)
        length=len(counter_list)
        print("字符总数: ",length)
        with open(output_path, "w",encoding='utf-8') as file:
            for word in counter_list:
                file.write(word[0])
                file.write("\n")
               # print(word[0])  #输出字典的键
                #print(word[1])  # 输出字典的值

if __name__ == '__main__':
    tp=text_preprocess();
    tp.get_words_frequency()
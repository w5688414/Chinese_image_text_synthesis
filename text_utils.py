import os
import random
import numpy as np
import os

from PIL import ImageFont


class FontState(object):
    """
        Defines the random state of the font rendering
     """

    def __init__(self, data_dir='data'):
        # get the names of fonts to use:
        self.FONT_LIST = os.path.join(data_dir, 'fonts/fontlist.txt')
        self.fonts = [os.path.join(data_dir, 'fonts', f.strip()) for f in open(self.FONT_LIST)]
        print(self.fonts)

    '''
     random generate a font
    '''
    def sample(self):
        font=random.choice(self.fonts)
        font=ImageFont.truetype(font, 20)
        print(font.getname())
        return font


class TextSource(object):
    """
        Provides text for words, paragraphs, sentences.
    """

    def __init__(self, fn):
        files = os.listdir(fn)
        # print(files)
        # files = files[0:-1]
        valid_files=[]
        for file in files:
            if(file.split('.')[-1]=='txt'):
                valid_files.append(file)
        random.shuffle(valid_files)
        filecnt = 10
        print(valid_files)
        self.txt=[]
        for filename in valid_files:
            filecnt -= 1
            if filecnt == 0:
                break
            fc = fn + filename
            print(fc)
            with open(fc, 'r') as f:
                for l in f.readlines():
                    line = l.strip()
                    # print(line)
                    self.txt.append(line)

        random.shuffle(self.txt)
        print(len(self.txt))

    '''
        random select words
    '''
    def sample_word(self):
        rand_line = self.txt[np.random.choice(len(self.txt))]
        print(rand_line)
        words = rand_line.split()
        while True:  #判断读取的一行是否为空
            if len(words)>0:
                break
            rand_line = self.txt[np.random.choice(len(self.txt))]
            print(rand_line)
            words = rand_line.split()

        rand_word = random.choice(words)
        print('sample_word_output', rand_word)
        return rand_word

if __name__ == '__main__':
    textSource=TextSource(r'data/words/')
    textSource.sample_word()

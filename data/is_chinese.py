# coding=utf-8
from __future__ import division
import codecs
import sys


def is_chinese(ch):
    # uc=ch.decode('utf-8')
    if u'\u4e00' <= ch <= u'\u9fff':
        return True
    else:
        return False


def is_ascii(s):
    return all(ord(c) < 128 for c in s)


def extract_chineseSequence(sequence):
    # print sequence
    newwords = ''
    for ch in sequence:
        if is_chinese(ch) or ch.isalnum():
            # print(ch)
            newwords = newwords + ch + " "
        else:
            newwords = newwords + ' '
            continue
    print(newwords)
    return newwords

if __name__ == '__main__':
    txt_source = 'words/number.txt'
    # f=open(txt_source,'r')
    f = codecs.open(txt_source, 'r', 'gbk', 'ignore')
    for line in f.readlines():
        extract_chineseSequence(line)



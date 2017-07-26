
from text_utils import FontState
import pygame
from pygame import freetype
import numpy as np
import pickle


pygame.init()
FS = FontState()

for i in range(len(FS.fonts)):
    print(i)
    font = freetype.Font(FS.fonts[i], size=12)
    print(font.name)
import random

from PIL import Image


class TextRegions(object):

    def __init__(self):
        self.minArea = 100  # number of pix

    """
    Get region  which are good for placing
    text.
    """

    def get_regions(self,img):
        width,height=img.size
        dict=self.randomRect(width,height)
        return dict

    '''
     random generate a fixed size of rectangle
    '''
    def randomFixedRect(self,rec_width,rec_height,width,height):
        insetX = random.randint(0, width - rec_width)
        insetY = random.randint(0, height - rec_height)
        dict = {}
        dict['x'] = insetX
        dict['y'] = insetY
        dict['width'] = rec_width
        dict['height'] = rec_height

    '''
        random generate a rectangle
    '''
    def randomRect(self, width, height):
        insetWidth = random.randint(0,width)%100
        insetHeight =  random.randint(0,height)%100
        insetX = random.randint(0,width - insetWidth)
        insetY = random.randint(0,height - insetHeight)
        dict={}
        dict['x']=insetX
        dict['y']=insetY
        dict['width']=insetWidth
        dict['height']=insetHeight
        print(dict)
        return dict

if __name__ == '__main__':
    img = Image.new("RGB", (512, 512), "white")
    img = img.resize((800, 600), Image.ANTIALIAS)
    textRegion=TextRegions()
    textRegion.get_regions(img)
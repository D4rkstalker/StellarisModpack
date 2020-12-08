from PIL import Image
import os, sys

path = "/Resize/"
dirs = os.listdir(path)

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f = os.path.splitext(path+item)
            imResize = im.resize((200,200))
            imResize.save(f + ' resized.png', 'PNG')

resize()
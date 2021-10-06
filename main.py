import anvil
import cv2
import numpy as np

def bll(name):
    return anvil.Block('minecraft', name)

img = cv2.imread('aa.png')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

names = {1:'white_wool', 2:'light_gray_wool', 3:'gray_wool', 4:'dark_gray_wool', 5:'black_wool'}

n_elem = len(names)
img = 255 - img
img = img/(255/n_elem)
img = img.astype(int)

sh = img.shape

my_region = anvil.EmptyRegion(0,0)

x = 0

for i in range(sh[0]):
    for j in range(sh[1]):
        y = sh[0] - i
        z = j
        if(img[i, j] != 0):
            my_region.set_block(bll(names[img[i, j]]), x, y, z)


#my_region.save('r.0.0.mca')

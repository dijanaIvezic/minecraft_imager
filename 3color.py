import anvil
import cv2
import numpy as np

def bll(name):
    return anvil.Block('minecraft', name)

img = cv2.imread('van.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

names = {(0,0,0):'black_wool',
        (0,0,1):'lapis_block',
        (0,0,2):'light_blue_concrete',
        (0,1,0):'green_concrete_powder',
        (0,1,1):'cyan_concrete_powder',
        (0,1,2):'light_blue_concrete_powder',
        (0,2,0):'emerald_block',
        (0,2,1):'lime_wool',
        (0,2,2):'diamond_block',
        (1,0,0):'crimson_planks',
        (1,0,1):'purple_concrete_powder',
        (1,0,2):'magenta_wool',
        (1,1,0):'green_wool',
        (1,1,1):'stripped_dark_oak_wood',
        (1,1,2):'purple_wool',
        (1,2,0):'lime_wool',
        (1,2,1):'melon',
        (1,2,2):'light_blue_wool',
        (2,0,0):'red_concrete',
        (2,0,1):'red_concrete_powder',
        (2,0,2):'magenta_concrete',
        (2,1,0):'orange_concrete',
        (2,1,1):'orange_concrete_powder',
        (2,1,2):'pink_wool',
        (2,2,0):'yellow_wool',
        (2,2,1):'gold_block',
        (2,2,2):'white_wool'
}

h = np.histogram(img, 3)
h = h[1][1:]
h[-1] = h[-1] + 1
img = np.digitize(img, h)
img = img.astype(int)

sh = img.shape

my_region = anvil.EmptyRegion(0,0)

y = 3

for i in range(sh[0]):
    for j in range(sh[1]):
        x = sh[0]-i
        z = j
        wh = img[i,j]
        my_region.set_block(bll(names[tuple(wh)]), x, y, z)

my_region.save('r.0.0.mca')

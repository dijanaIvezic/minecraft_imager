import cv2
import numpy as np
import glob
import anvil
import sklearn.neighbors as nn

names = glob.glob('.\\block/*.png')

colors = {}

for name in names:
    img = cv2.imread(name)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    srch = name.split(".\\block\\")
    srch = srch[1].split(".")[0]
    colors[tuple(img[5,5])] = srch

kys = colors.keys()
kys = np.array([list(x) for x in kys])

tree = nn.KDTree(kys)

def closest_color(rgb):
    rgb = np.array(rgb)
    distance, index = tree.query([rgb])
    l = kys[index[0]].tolist()[0]
    return tuple(l)

def bll(name):
    return anvil.Block('minecraft', name)

img = cv2.imread('t72.png')

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

sh = img.shape

my_region = anvil.EmptyRegion(0,0)

y = 60

for i in range(sh[0]):
    for j in range(sh[1]):
        x = sh[0]-i
        z = j
        img[i,j] = list(closest_color(img[i,j]))
        wh = colors[closest_color(img[i,j])]
        my_region.set_block(bll(wh), x, y, z)

img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.imwrite("AA.png", img)

my_region.save('r.0.0.mca')

import cv2
import numpy as np
import glob

names = glob.glob('.\\block/*.png')

for name in names:
    img = cv2.imread(name)

    img_0 = np.average(img[:, :, 0])
    img_1 = np.average(img[:, :, 1])
    img_2 = np.average(img[:, :, 2])

    img[:, :, 0] = img_0
    img[:, :, 1] = img_1
    img[:, :, 2] = img_2

    cv2.imwrite(name, img)


import os
import sys

import numpy as np

import cv2
import matplotlib.pyplot as plt

# # Define the image and annotation paths
# image_path = '/media/daanish/Samsung SSD/Edge AI/annotationimagesucs547'
# annotation_path = '/media/daanish/Samsung SSD/Edge AI/annoted'

# Get a list of all image files in the directory
im = cv2.imread('/media/daanish/Samsung SSD/Edge AI/annotationimagesucs547/aachen_000029_000019_leftImg8bit_foggy_beta_0.02_fake_0.png')
plt.imshow(im)

pl = []
l = 0;

while(True):
    p = plt.ginput(1)
    (px,py)=p[0][0],p[0][1]

    if px < 50 and py < 50:
        plt.close()
        break
    l+=1

    pl.append((int(px),int(py)))

plt.show()

cv2.fillPoly

    


p = plt.ginput(5)
print(p)
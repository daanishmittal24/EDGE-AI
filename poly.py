import os
import sys

import numpy as np
import cv2
import matplotlib.pyplot as plt

# Define the image and annotation paths
image_path = 'D:/Edge AI/annotationimagesucs547'
annotation_path = 'D:/Edge AI/annotation'

# Get a list of all image files in the directory
imlist = os.listdir(image_path)
im = cv2.imread(os.path.join(image_path, imlist[0]))
plt.imshow(im)

p = plt.ginput(5)
print(p)
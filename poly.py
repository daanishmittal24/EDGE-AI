import os
import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt

# # Define the image and annotation paths
image_path = '/media/daanish/Samsung SSD/Edge AI/annotationimagesucs547'
annotation_path = '/media/daanish/Samsung SSD/Edge AI/annoted'

# Get a list of all image files in the directory
im = cv2.imread('/media/daanish/Samsung SSD/Edge AI/annotationimagesucs547/aachen_000029_000019_leftImg8bit_foggy_beta_0.02_fake_0.png')
plt.imshow(im)

# Ensure the annotation directory exists
if not os.path.exists(annotation_path):
    os.makedirs(annotation_path)

pl = []
l = 0

while(True):
    p = plt.ginput(1) #select a single point to put in p
    (px,py)=p[0][0],p[0][1] #inn p, i denotes point no and j denotes coordinates

    if px < 80 and py < 80: # when all points selected, click on top left to quit
        plt.close()
        break
    l+=1

    pl.append((int(px),int(py)))

plt.show()

cv2.fillPoly(im , [np.array(pl)], (255,150,255))
cv2.imwrite()
cv2.imshow('win',im)
cv2.waitKey(0)
cv2.destroyAllWindows()

dst_txt = "/media/daanish/Samsung SSD/Edge AI/annotationimagesucs547/aachen_000029_000019_leftImg8bit_foggy_beta_0.02_fake_0.txt"
with open(dst_txt,'w') as f:
    for a in pl:
        f.write("(" + str(a[0]) + "," + str(a[1]) +")"+ '\n')
    f.write("\n")
    
    
#run for multiple images
#save segmented images using cv2.imwrite
#try to save multiple polygons in same image


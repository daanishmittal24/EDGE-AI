import os
import cv2

# Set the correct paths to your images and annotations
image_path = '/media/daanish/Samsung SSD/Edge AI/annotationimagesucs547'
annotation_path = '/media/daanish/Samsung SSD/Edge AI/annoted'

# Get a list of all image files in the directory
imlist = os.listdir(image_path)

font = cv2.FONT_HERSHEY_COMPLEX_SMALL
fontscale = 1
color = (0, 0, 255)
thickness = 1

# Ensure the annotation directory exists
if not os.path.exists(annotation_path):
    os.makedirs(annotation_path)

for im in imlist:
    # Construct the full path to the image
    img_path = os.path.join(image_path, im)
    # Read the image
    img = cv2.imread(img_path)

    if img is None:
        print(f"Failed to load image {im}")
        continue

    # Add labels to the image and draw borders
    org_car = (10, 20)
    img = cv2.putText(img, "car", org_car, font, fontscale, color, thickness)
    img = cv2.rectangle(img, (0, 0), (70, 50), color, 2)

    org_pole = (310, 20)
    img = cv2.putText(img, "pole", org_pole, font, fontscale, color, thickness)
    img = cv2.rectangle(img, (300, 0), (370, 50), color, 2)

    frame = im[:-4]  # Get the image filename without the extension
    dst_txt = frame + '.txt'  # Annotation file name

    with open(os.path.join(annotation_path, dst_txt), 'a') as f:
        while True:
            # Display the image and let the user select the ROI
            r = cv2.selectROI("Image", img)

            # Check if the selected ROI's top-left corner coordinates are less than 50
            if r[0] < 50 and r[1] < 50:
                break

            s = "undefined"
            r1 = cv2.selectROI("Image", img)
            if 0 < r1[0] < 70 and 0 < r1[1] < 50:
                s = "car"
            elif 300 < r1[0] < 370 and 0 < r1[1] < 50:
                s = "pole"

            # Calculate the bottom-right corner coordinates of the ROI
            xend = r[0] + r[2]
            yend = r[1] + r[3]

            # Write the ROI coordinates and label to the annotation file
            line = f"{s} {r[0]} {r[1]} {xend} {yend}\n"
            f.write(line)

    # Close all ROI windows
    cv2.destroyAllWindows()

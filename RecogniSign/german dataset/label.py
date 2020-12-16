import os
import cv2

image_dir = "Full/"

f = open("Full/gt.txt", 'r').readlines()

for image in f:
    temp = image.strip().split(';')
    name = temp[0].split('.')[0]
    label = temp[-1]

    img = cv2.imread(image_dir+name+'.ppm')

    height = img.shape[0]
    width = img.shape[1]

    x1 = int(temp[1])
    y1 = int(temp[2])

    x2 = int(temp[3])
    y2 = int(temp[4])

    x = str(((x2 + x1)/2.0)/width)[:8]
    y = str(((y2 + y1)/2.0)/height)[:8]
    w = str((x2 - x1)/width)[:8]
    h = str((y2 - y1)/height)[:8]

    data = label + " " + x + " " + y + " " + w + " " + h + "\n"

    with open(image_dir+image.split('.')[0]+'.txt', 'a') as f2:
        f2.write(data)
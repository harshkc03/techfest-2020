import cv2
import os

img = cv2.imread("Full/00001.ppm")

f = open("Full/00001.txt", 'r').readlines()[2].split()

height = img.shape[0]
width = img.shape[1]

x = float(f[1]) * width
y = float(f[2]) * height
w = float(f[3]) * width
h = float(f[4]) * height

x1 = x - (w/2)
y1 = y - (h/2)
x2 = x + (w/2)
y2 = y + (h/2)

start_point = (x1, y1) 
end_point = (x2, y2) 

color = (0, 0, 255) 
thickness = 2

image = cv2.rectangle(img,(int(x1),int(y1)),(int(x2),int(y2)),(0,0,255),3)

print(x1,y1,x2,y2)

cv2.imshow("Out", image)

cv2.waitKey()

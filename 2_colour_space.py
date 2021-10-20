import numpy as np
import cv2
img=cv2.imread("dog2.jpg")
# px = img[100,100]
# print(px)
# #access intesity values
# blue=img[100,100,0]
# print(blue)
# green = img[100,100,1]
# print(green)
# red = img[100,100,2]
# print(red)
# #Memory management
img1 = np.copy(img)
print(img1)
#primitve operation
cv2.imshow("BGR",img)
cv2.waitKey(0)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",img_gray)
cv2.waitKey(0)
print(img_gray)
#visualising images
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('image_gray', img_rgb)
cv2.waitKey(0)
img_ycr = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
cv2.imshow('image_ycr', img_ycr)
cv2.waitKey(0)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('image_hsv', img_hsv)
cv2.waitKey(0)
import numpy as np 
import cv2


img=cv2.imread("city_hall.jpg")
cv2.imshow("image",img)
cv2.waitKey(0)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=cv2.resize(gray,(600,400))
cv2.imshow("gray",gray)
cv2.waitKey(0)
sobelx = cv2.Sobel(gray,cv2.CV_32F,1,0,ksize=3)
sobely = cv2.Sobel(gray,cv2.CV_32F,0,1,ksize=3)
cv2.imshow("x",sobelx)
cv2.waitKey(0)
cv2.imshow("y",sobely)
cv2.waitKey(0)


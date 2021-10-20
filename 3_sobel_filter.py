import cv2
import numpy as np

image = cv2.imread('city_hall.jpg')  # read_img
image=cv2.resize(image,(600,400))   #resize 

cv2.imshow("inp",image)
cv2.waitKey(0)
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #converting gray

cv2.imshow("gray",image)
cv2.waitKey(0)

sobel_x=np.array([[-1,0,1],                 #sobel_x filter
                [-2,0,2],
                [-1,0,1]])
filter_image=cv2.filter2D(image,-1,sobel_x)
cv2.imshow("outx_threshold_without",filter_image)
a,b=cv2.threshold(filter_image,150,255,cv2.THRESH_BINARY) #thresholding noise
cv2.imshow("outx_threshold",b)
cv2.waitKey(0)
sobel_y=np.array([[-1,-2,-1],               #sobel_y filter
                [0,0,0],
                [1,2,1]])
filter_image=cv2.filter2D(image,-1,sobel_y)
a,b=cv2.threshold(filter_image,150,255,cv2.THRESH_BINARY)   #thresholding noise
cv2.imshow("outy_threshold",b)
cv2.waitKey(0)
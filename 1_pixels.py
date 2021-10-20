import numpy as np 
import cv2


img=cv2.imread("dog2.jpg") 

print("shape ",img.shape)
print("sum ",img.sum())
print("min ", img.min())
print("max ", img.max())
print("mean ", img.mean())
print("standard deviation ", img.std())
print(img)
cv2.imshow("output_window",img)
cv2.waitKey(0) #mill seconds

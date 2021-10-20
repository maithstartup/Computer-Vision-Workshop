import numpy as np
import cv2
parrot = cv2.imread('dog2.jpg', 0)
lion = cv2.imread('space_background.jpg', 0)
# weight_img1=float(input().strip())
# weight_img2=1.0-weight_img1
lion_resized = cv2.resize(lion, (parrot.shape[1], parrot.shape[0]))
img = cv2.addWeighted(parrot, 0.7, lion_resized, 0.3, 0.0)
cv2.imshow('image', img)
cv2.waitKey(0)

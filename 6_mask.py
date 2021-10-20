
import cv2
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('car_green_screen.jpg')
cv2.imshow("car",image)
cv2.waitKey(0)
# Print out the image dimensions (height, width, and depth (color))
print('Image dimensions:', image.shape)
print(image[0][0])
## TODO: Define our color selection boundaries in RGB values
lower_green = np.array([0,100,0])   #lower_bound - BGR
upper_green = np.array([50,255,50]) #upper_bound
# Define the masked area
mask = cv2.inRange(image, lower_green, upper_green)
# Vizualize the mask
plt.imshow(mask, cmap='gray')
# Mask the image to let the car show through
masked_image = np.copy(image)
masked_image[mask != 0] = [0, 0, 0]

# Display it!
cv2.imshow("mask",masked_image)
cv2.waitKey(0)
# Load in a background image, and convert it to RGB 
background_image = cv2.imread('sky.jpg')
cv2.imshow("back",background_image)
cv2.waitKey(0)
## TODO: Crop it or resize the background to be the right size (450x660)
back=cv2.resize(background_image,(660,450))
## TODO: Mask the cropped background so that the pizza area is blocked
back[mask ==0 ]=[0,0,0]
# complete_image = masked_image + crop_background
complete_image=back+masked_image
cv2.imshow("img",complete_image)
cv2.waitKey(0)
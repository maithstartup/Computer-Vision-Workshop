import cv2

image = cv2.imread('city_hall.jpg')

grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
grey=cv2.resize(grey,(600,400))
square_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
print(square_kernel)

erosion = cv2.erode(grey, square_kernel, iterations=1)
cv2.imshow('erosion', erosion)
cv2.waitKey(0)
dilation = cv2.dilate(grey, square_kernel, iterations=1)
cv2.imshow('dilation', dilation)
cv2.waitKey(0)
opening = cv2.morphologyEx(grey, cv2.MORPH_OPEN, square_kernel)
cv2.imshow('opening', opening)
cv2.waitKey(0)
closing = cv2.morphologyEx(grey, cv2.MORPH_CLOSE, square_kernel)
cv2.imshow('closing', closing)
cv2.waitKey(0)

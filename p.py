import numpy as np
import cv2

img = cv2.imread('/home/rashi/Desktop/opencv/tt.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('color_image',img)
cv2.imshow('gray_image',gray)
cv2.waitKey(0)
cv2.destroyAllWindows(0)

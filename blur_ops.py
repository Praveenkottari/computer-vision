import cv2
import numpy as np

img = cv2.imread('test.jpg')
output = cv2.imshow('original image', img)

#kernal blurring
kernal_25 = np.ones((25,25), dtype=np.float32)/625.0
output_kernal = cv2.filter2D(img, -1, kernal_25)
cv2.imshow('kernal 25', output_kernal)

#blur function
blur_func = cv2.blur(img, (25,25))
cv2.imshow('blur_function', blur_func)

#boxfilter
output_boxfilt = cv2.boxFilter(img, -1, (5,5), normalize=False)
cv2.imshow('box filter', output_boxfilt)

#gussian blur
output_guassian = cv2.GaussianBlur(img, (5,5),0)
cv2.imshow('gussian filter', output_guassian)



cv2.waitKey(0)
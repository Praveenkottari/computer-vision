import cv2
import numpy as np

img_file = 'test.jpg'
img = cv2.imread(img_file)

#kernal
kernal_ident = np.array([[0,0,0],[0,1,0],[0,0,0]])
kernal_3 = np.ones((3,3), dtype=np.float32) / 9.0
keranl_11 = np.ones((11,11), dtype=np.float32)/121.0

#apply filter
output_same = cv2.filter2D(img,-1,kernal_ident)
output_3 = cv2.filter2D(img, -1, kernal_3)
output_11 = cv2.filter2D(img, -1, keranl_11)
 
#show
# cv2.imshow('same', output_same)
# cv2.imshow('3 x 3', output_3)
# cv2.imshow('11 x 11', output_11)

# motion blur 

size = 15
kernal_blur = np.zeros((size, size))
kernal_blur[int((size-1)/2), :] =  np.ones(size)
kernal_blur = kernal_blur/size

output_blur = cv2.filter2D(img, -1, kernal_blur)


cv2.imshow('blur', output_blur)
cv2.imshow('original img', img)













cv2.waitKey()


# 
import cv2
import numpy as np

image = cv2.imread('test.jpg')

height , width = image.shape[:2]
print(image.shape)
# show  = cv2.imshow('image', image)

#Img resize by linear interpolation
img_linear = cv2.resize(image,None, fx=5.5 , fy =5.5, interpolation=cv2.INTER_LINEAR)

#imgae resize by cubic interpolation
img_cubic = cv2.resize(image,None,fx=5.5, fy=5.5, interpolation= cv2.INTER_CUBIC)

matrix  = cv2.getRotationMatrix2D((width/2 , height/2), 10, 1)
#apply above matrix to th image
rotat = cv2.warpAffine(image, matrix, (width,height))

#all images
cv2.imshow('original', image)
cv2.imshow('rotate', rotat)
cv2.imshow('linear', img_linear)
cv2.imshow('cubic', img_cubic)

if (cv2.waitKey()):
    cv2.destroyAllWindows()

import cv2

img = cv2.imread('test.jpg')

guasian_blur = cv2.GaussianBlur(img,(5,5),2)

#addweightage of shrppend image
output1 = cv2.addWeighted(img, 1.5, guasian_blur, -0.5, 0)
output2 = cv2.addWeighted(img, 3.5, guasian_blur, -2.5, 0)
output3 = cv2.addWeighted(img, 8.5, guasian_blur, -7.5, 0)

#show
cv2.imshow('sharp1', output1)
cv2.imshow('sharp2', output2)
cv2.imshow('sharp3', output3)

cv2.waitKey(0)
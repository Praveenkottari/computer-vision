import cv2

image = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Test image', image)

cv2.waitKey(5000)
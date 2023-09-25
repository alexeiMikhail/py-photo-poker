import cv2 as cv

img_grayscale = cv.imread('test.jpg', 0)

cv.imshow('grayscale image', img_grayscale)

cv.waitKey(0)
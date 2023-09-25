import cv2 as cv
import time


img = cv.imread('pineapple.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

disp = cv.imshow("disp", img)
cv.waitKey(900)
import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats 2.jpg")
cv.imshow("cats", img)

blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('blank', blank)
# print(f'blank shape = {blank.shape}')

# circle
circle = cv.circle(blank.copy(), (blank.shape[1]//2, blank.shape[0]//2), 100, 255, -1)
cv.imshow('circle', circle)
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
cv.imshow('rectangle', rectangle)

weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow("weird shape", weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow("weird shape mask image", masked)

cv.waitKey(0)


import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Photos/park.jpg")
# BGR2GRAY
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# print(f'img = {img}')
# print(f'img shape= {img.shape}')
# print(f'gray = {gray}')
# print(f'gray shape= {gray.shape}')

cv.imshow("Boston", img)
# cv.imshow("Gray", gray)

# BGR TO HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow("HSV", hsv)

#BGR TO L*A*B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab)

#BGR TO RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow("rgb", rgb)

#HSV TO BRG
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
# cv.imshow("hsv --> bgr", hsv_bgr)

#lab to bgr
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("lab --> bgr", lab_bgr)

cv.waitKey(0)
# plt.imshow(img)
# plt.imshow(rgb)
# plt.show()


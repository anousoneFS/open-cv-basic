import cv2 as cv

img = cv.imread("Photos/cats.jpg")
cv.imshow("cats", img)

# Averaging
blur = cv.blur(img, (3,3))
cv.imshow("Average blur", blur)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("Gaussian Blur", gauss)

#Median Blur
median = cv.medianBlur(img, 3)
cv.imshow("median blur", median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("bilateral", bilateral)

cv.waitKey(0)

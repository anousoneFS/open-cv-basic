import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")
blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("park", img[200:210, 200:210])
# cv.imshow("blank", blank)

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])[200:210, 200:210]
green = cv.merge([blank,g,blank])[200:210, 200:210]
red = cv.merge([blank,blank,r])[200:210, 200:210]

cv.imshow("b", blue)
cv.imshow("g", green)
cv.imshow("r", red)

# can not merged 
# merged = cv.merge([blue,green,red])
# cv.imshow("merged from blank", merged)

# cv.imshow("b", b)
# cv.imshow("g", g)
# cv.imshow("r", r)


print(f'img shape = {img.shape}')
print(f'blue shape = {b.shape}')
print(f'green shape = {g.shape}')
print(f'red shape = {r.shape}')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Grayscale", gray)

# merged = cv.merge([b,g,r])
# cv.imshow("merged images", merged)

cv.waitKey(0)


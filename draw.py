import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow("blank", blank)

# Point the image a certain colour
# blank[200:300, 300:400] = 0,0,255
# cv.imshow("Green", blank)

# draw a rectangle
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED)
# cv.rectangle(blank, (0,0), (blank.shape[1] // 2, blank.shape[0] // 2), (0,255,0), thickness=cv.FILLED)
# draw a circle
# cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (255,0,0), thickness=4)
# draw a line
# cv.line(blank, (0,0), (blank.shape[1] // 2, blank.shape[0] // 2), (255,255,255), thickness=5)
# write text
cv.putText(blank, "hi anousone", (100,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)

cv.imshow("rectangle", blank)

cv.waitKey(0)



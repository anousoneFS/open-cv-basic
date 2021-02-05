import cv2 as cv

# img = cv.imread("Photos/cat_large.jpg")
# cv.imshow("Cat", img)

capture = cv.VideoCapture("Videos/dog.mp4")
# capture = cv.VideoCapture(1)

while True:
    isTrue, frame = capture.read()

    if isTrue:
        cv.imshow("Video", frame)
        k = cv.waitKey(1) & 0xff
        if k == ord('q'):
            break
    else:
        break
    
capture.release()
cv.destroyAllWindows()

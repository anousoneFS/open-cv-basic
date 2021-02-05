import cv2 as cv

capture = cv.VideoCapture(0)
# capture = cv.VideoCapture("Videos/dog.mp4")
# capture = cv.VideoCapture("Photos/cat.jpg")

def rescaleFrame(frame, scale=0.75):
    # for Video, Image and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # for Live Video
    capture.set(3, width)
    capture.set(4, height)

while True:
    isTrue, frame = capture.read()

    if isTrue:
        cv.imshow("Video", frame)
        resize_frame = rescaleFrame(frame, 0.5)
        cv.imshow("Video resize", resize_frame)

        if cv.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()

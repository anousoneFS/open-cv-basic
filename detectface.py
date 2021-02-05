import cv2 as cv

capture = cv.VideoCapture(0)
cascade_face = cv.CascadeClassifier('haar_face.xml')

while True:
    isTrue, frame = capture.read()
    faces = cascade_face.detectMultiScale(frame, 1.1, 4)
    if isTrue:
        for (x,y,w,h) in faces:
            cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        cv.imshow("frame", frame)

        k = cv.waitKey(1) & 0xFF
        if k == ord('q'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()

import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    haar_face = cv.CascadeClassifier('haar_face.xml')
    faces_rect = haar_face.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
    print(f'Number of faces found = {len(faces_rect)}')
    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)

    if isTrue:
        cv.imshow("frame", frame)
        k = cv.waitKey(1) & 0xFF
        if k == ord('d'):
            break
    else:
        break
capture.release()
cv.destroyAllWindows()




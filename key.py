import cv2 as cv

while True:
    key = cv.waitKey(33) & 0b11111111
    if key == ord('d'):
        print(f'key = {key}')


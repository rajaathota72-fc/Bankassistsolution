import cv2
import sys
webcam = cv2.VideoCapture(0)
while True:
    ret,frame = webcam.read()
    cv2.imwrite("NewPicture.jpg", frame)
    k = cv2.waitKey(5)
    if k == 32:  # Esc key to stop
        break

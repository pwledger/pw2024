import numpy as np
import cv2
from matplotlib import pyplot as plt

capture = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(
    'opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')

while cv2.waitKey(33) != ord('q'):
    ret, frame = capture.read()
    faces = face_cascade.detectMultiScale(frame, 1.03, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("VideoFrame", frame)
    
capture.release()
cv2.destroyAllWindows()

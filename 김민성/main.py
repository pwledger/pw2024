import cv2
import numpy as np

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) < 0:
    ret, frame = capture.read()
    frame = cv2.rectangle(frame, (200, 200), (50, 50), (255, 255, 255), 5, cv2.LINE_8)
    cv2.imshow(frame)

capture.release()
cv2.destroyAllWindows()
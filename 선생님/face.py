import cv2

capture = cv2.VideoCapture(0)

while cv2.waitKey(33) != ord('q'):
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)
    
capture.release()
cv2.destroyAllWindows()

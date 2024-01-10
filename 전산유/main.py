import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) != ord('q'):
    ret, frame = capture.read()
    frame = cv2.rectangle(frame,(200 ,200), (50,50), (255, 0, 0), 5, cv2.LINE_8)
    cv2.imshow("VideoFrame", frame)

capture.release()
cv2.destroyAllWindows()
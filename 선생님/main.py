import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) != ord('q'):
    ret, frame = capture.read()
    # x : 200 , y : 200 위치에 가로 세로 50 짜리 사각형을 그리시오 
    frame = cv2.rectangle(frame, (500, 200), (200, 400), (255, 0, 0), 5, cv2.LINE_8)
    cv2.imshow("VideoFrame", frame)

capture.release()
cv2.destroyAllWindows()
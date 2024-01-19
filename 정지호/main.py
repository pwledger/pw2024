import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 너비
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # 높이

while cv2.waitKey(33) !=  ord('q'): # q 라는 키를 눌렀을 때 반복 종료
    ret, frame = capture.read()  # ret : 연결여부 , frame : 영상 정보
    cv2.imshow("VideoFrame", frame)

capture.release()
cv2.destroyAllWindows()
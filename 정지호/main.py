import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640) #너비
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) #높이
a = 0
while cv2.waitKey(33) !=  ord('q'): # Q 라는 키를 눌렀을 때 반복 종료
    a += 1
    ret, frame = capture.read() # ret : 연결여부 , frame : 영상 정보
    # x : 200 , y : 300 위치에 가로세로 50 짜리인 사각형을 그리시오 
    frame = cv2.rectangle(frame, (200+a, 300), (250+a, 350), (255, 0, 0), 5, cv2.LINE_8)
    cv2.imshow("VideoFrame", frame)

capture.release()
cv2.destroyAllWindows()
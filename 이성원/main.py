import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 카메라 화면의 가로 길이
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # 카메라 화면의 세로 길이
s = [200,200]
v = 50
speed = 2
while cv2.waitKey(33) != ord('q'):
    ret, frame = capture.read() # 카메라를 받아옴
    if ret :
       # x : 200 , y : 200 위치에 가로 세로 50 인 사각형을 그리시오 
       frame = cv2.rectangle(frame, (s[0]+speed,s[1]+speed),(s[0]+v+speed,s[1]+v+speed),(0,125,125),5,cv2.LINE_8)
       speed += 2
       if speed > 500 : speed = 0
       cv2.imshow("VideoFrame", frame) # 창에 화면이 뜸
    else:
        break 

capture.release()
cv2.destroyAllWindows()
import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1000) # 카메라 화면의 가로 길이
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 960) # 카메라 화면의 세로 길이
# 모델 가져오는방법
body_cascade = cv2.CascadeClassifier(".\opencv-master\data\haarcascades\haarcascade_fullbody.xml")
    
while cv2.waitKey(33) != ord('q'):
    ret, frame = capture.read() # 카메라를 받아옴x
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    body = body_cascade.detectMultiScale(gray, 1.01, 10, 0, minSize=(100, 100))
    for x,y,w,h in body:
        frame = cv2.rectangle(frame, (x,y) , (x+w , y+h) , (255, 0, 0), 5, cv2.LINE_8)
    s = f"people : {len(body)}"
    frame = cv2.putText(frame,s, (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
    cv2.imshow("VideoFrame", frame) # 창에 화면이 뜸


capture.release()
cv2.destroyAllWindows()
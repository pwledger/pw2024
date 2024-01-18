import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 카메라 화면의 가로 길이
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # 카메라 화면의 세로 길이
# 모델 가져오는방법
smile_cascade = cv2.CascadeClassifier(".\opencv-master\data\haarcascades\haarcascade_smile.xml")
    
while cv2.waitKey(33) != ord('q'):
    ret, frame = capture.read() # 카메라를 받아옴x
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    smile = smile_cascade.detectMultiScale(
        gray,
        scaleFactor = 1.5,
        minNeighbors=15,
        minSize=(25, 25)
    )
    for x,y,w,h in smile:
        frame = cv2.rectangle(frame, (x,y) , (x+w , y+h) , (255, 0, 255), 5, cv2.LINE_8)
    cv2.imshow("VideoFrame", frame) # 창에 화면이 뜸


capture.release()
cv2.destroyAllWindows()
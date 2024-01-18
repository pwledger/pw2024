import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 카메라 화면의 가로 길이
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # 카메라 화면의 세로 길이
# 모델 가져오는방법
face_cascade = cv2.CascadeClassifier(".\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml")
    
while cv2.waitKey(33) != ord('q'):
    ret, frame = capture.read() # 카메라를 받아옴x
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, 
        scaleFactor=1.1, 
        minNeighbors=5, 
        minSize=(30, 30))
    for x,y,w,h in faces:
        frame = cv2.rectangle(frame, (x,y) , (x+w , y+h) , (255, 0, 0), 5, cv2.LINE_8)
    cv2.imshow("VideoFrame", frame) # 창에 화면이 뜸


capture.release()
cv2.destroyAllWindows()
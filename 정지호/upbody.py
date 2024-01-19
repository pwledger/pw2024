import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 모델 가져오기 
face_cascade = cv2.CascadeClassifier(".\opencv-master\data\haarcascades\haarcascade_upperbody.xml")

while cv2.waitKey(33) != ord('q'):
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    upbody = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100,100))
    flame = cv2.putText(frame, f"number of people: {len(upbody)}", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)
    for x,y,w,h in upbody:
        frame = cv2.rectangle(frame, (x,y) , (x+w , y+h) , (255, 0, 0), 5, cv2.LINE_8)
    

    cv2.imshow("VideoFrame", frame)
    
capture.release()
cv2.destroyAllWindows()

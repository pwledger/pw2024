import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 모델 가져오기 
cascade = cv2.CascadeClassifier(".\opencv-master\data\haarcascades\haarcascade_upperbody.xml")

while cv2.waitKey(33) != ord('q'):
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    body = cascade.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (30,30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    for x,y,w,h in body:
        cv2.rectangle(frame, (x,y) , (x+w , y+h) , (0, 255, 0), 5)
    cv2.imshow("upper body", frame)
    
    
capture.release()
cv2.destroyAllWindows()
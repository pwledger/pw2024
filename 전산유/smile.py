# 웃었을 때에 감지를 해서 사각형을 그려주시오
import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

smile_cascade = cv2.CascadeClassifier(".\opencv-master\data\haarcascades\haarcascade_smile.xml")

while cv2.waitKey(33) != ord('q'):
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    smiles = smile_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=15,minSize=(25,25))
    if len(smiles) > 0:
        for x,y,w,h in smiles:
            frame = cv2.rectangle(frame,(x,y), (x+w, y+h),(255,0,0),5,cv2.LINE_8)
    cv2.imshow("VideoFrame", frame)
    
capture.release()
cv2.destroyAllWindows()
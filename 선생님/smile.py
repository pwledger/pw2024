#  웃었을 때에 감지를 해서 사각형을 그려 주시오 
# opencv\openCV_sumin\data\haarcascades\haarcascade_smile.xml 
# 위 모델을 사용해서 얼굴에 입을 어떻게 인식하는 지 확인 해 보세요

# python -m pip install opencv-python
import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1000) # 너비
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 800) # 높이

# 모델 인식하는 거 가져오기 스마일여부
smile_cascade = cv2.CascadeClassifier(".\opencv-master\data\haarcascades\haarcascade_smile.xml")

while cv2.waitKey(33) != ord('q'):
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 추가 
    smiles = smile_cascade.detectMultiScale(
            gray,
            scaleFactor = 1.5,
            minNeighbors=15,
            minSize=(25, 25)
        )
    if len(smiles) > 0:
        for x,y,w,h in smiles:
            frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 5, cv2.LINE_8) 
    cv2.imshow("VideoFrame", frame) 


capture.release()
cv2.destroyAllWindows()
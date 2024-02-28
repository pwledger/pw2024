import cv2
import numpy as np
import mediapipe as mp

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1200)

mp_hands = mp.solutions.hands# 손 인식 모델사용
balls = [(20,20) , (60,60)]
with mp_hands.Hands(model_complexity=0,min_detection_confidence=0.5,min_tracking_confidence=0.5) as hands:
    while True:
        s , image = cap.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # RGB 색 바꾸기
        results = hands.process(image)                 # 손 추적
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # 색 반전
        cx,cy = 0,0
        if results.multi_hand_landmarks:  # 손 인식 되었을 때 
            for hand in results.multi_hand_landmarks:
                for id , lm in enumerate(hand.landmark):
                    if id == 8:
                        h,w,c = image.shape
                        cx ,cy = int(lm.x*w) , int(lm.y*h) # cv2 에서 사용할 좌표 정보
                        cv2.circle(image , (cx , cy) , 20 ,(255,0,0) , cv2.FILLED)
        # 선 그린곳  
        if s :
            for i in range(30):
                image = cv2.line(image, (0, i*40), (1600, i*40), (0, 0, 255), 1, cv2.LINE_AA)
            for j in range(40):
                image = cv2.line(image, (j*40,0), (j*40,1200), (0, 0, 255), 1, cv2.LINE_AA)
        # 원 그린곳 
        for 좌표 in balls:
            cv2.circle(image, 좌표, 20, (0, 255, 0), cv2.FILLED, cv2.LINE_4)
            if 좌표[0] -20< cx < 좌표[0] + 20:
                if 좌표[1] -20< cy < 좌표[1] + 20:
                    print("ok")
                    del balls[0]

        cv2.imshow('MediaPipe Hands', image)

        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
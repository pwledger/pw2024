import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
while True:
    with mp_hands.Hands(model_complexity=0,min_detection_confidence=0.5,min_tracking_confidence=0.5) as hands:
        success, image = cap.read()
        if success:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # 색상 반전
            results = hands.process(image)  # 검출
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # 원 상태로

            if results.multi_hand_landmarks:
                for hand in results.multi_hand_landmarks:
                    x1,y1,x2,y2 = 0 , 0, 0 ,0
                    for id , lm in enumerate(hand.landmark):
                        h,w,c = image.shape  # 높이, 너비 , 채널 개수
                        cx ,cy = int(lm.x*w) , int(lm.y*h) # cv2 에서 사용할 좌표 정보
                        if id == 8:
                            cv2.circle(image , (cx , cy) , 20 ,(255,0,0) , cv2.FILLED)
                            x1 ,y1 = cx , cy
                        if id == 4:
                            cv2.circle(image , (cx , cy) , 20 ,(255,0,0) , cv2.FILLED)
                            x2 ,y2 = cx , cy
                    길이 =  ( (x1-x2)**2 + (y2-y1)**2 )**0.5
                    cv2.putText(image , f"distance : {길이}", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)

                    
            cv2.imshow('MediaPipe Hands', cv2.flip(image, 2))  # 보여주고

        if cv2.waitKey(5) & 0xFF == 27:  #  esc 키를 누르면 끝내기
            break
cap.release()




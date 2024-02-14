import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

with mp_hands.Hands(model_complexity=0,min_detection_confidence=0.5,min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:  # 카메라를 성공적으로 가쟈 오지 못하면
            print("Ignoring empty camera frame.")  # 메세지 풀력
            continue                # 위 부터 다시 실행 (12번째 코드 부터)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # RGB 색 바꾸기
        results = hands.process(image)                 # 인식

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        if results.multi_hand_landmarks:
            for hand in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
                
                x1,y1,x2,y2 = 0,0,0,0
                for id , lm in enumerate(hand.landmark):
                    h,w,c = image.shape
                    
                    cx ,cy = int(lm.x*w) , int(lm.y*h) # cv2 에서 사용할 좌표 정보
                    if id == 8:
                        cv2.circle(image , (cx , cy) , 20 ,(255,0,0) , cv2.FILLED)
                        x1 ,y1 = cx , cy
                    if id == 12:
                        cv2.circle(image , (cx , cy) , 20 ,(255,0,0) , cv2.FILLED)
                        x2 , y2 = cx , cy
                cv2.rectangle(image , (x1 ,y1) , (x2 , y2) , (255,0,0) , cv2.FILLED)
                    

               
        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))

        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
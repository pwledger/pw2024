import pyautogui
import time

"""print(pyautogui.size())
time.sleep(2)
print(pyautogui.position())
pyautogui.moveTo(100, 200, 2)
pyautogui.click()
pyautogui.click(button='right')
"""
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

screen_width, screen_height = pyautogui.size()

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
                x1,y1,x2,y2 = 0,0,0,0
                for id , lm in enumerate(hand.landmark): # id : landmark 번호 , lm 좌표비율 값
                    h,w,c = image.shape 
                    cx ,cy = int(lm.x*w) , int(lm.y*h) # cv2 에서 사용할 좌표 정보
                    if id == 8:
                        x1,y1 = cx,cy
                        cv2.circle(image , (cx , cy) , 10 ,(255,0,0) , cv2.FILLED)
                        pyautogui.moveTo(screen_width - cx*screen_width/w, cy*screen_height/h)
                    if id == 12:
                        x2,y2 = cx,cy
                        cv2.circle(image , (cx , cy) , 10 ,(255,0,0) , cv2.FILLED)
                # x1,y1,x2,y2 의 거리부터 출력
                
                # 클릭에 들어간느 부분을 완성해 보세요 tip) 8번 이랑 12번 사용 

        cv2.imshow('MediaPipe Hands', cv2.flip(image,1))

        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
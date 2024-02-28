import cv2
import mediapipe as mp
import autopy

# 모듈 초기화
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# 화면 크기
screen_width, screen_height = autopy.screen.size()

# 마우스 이동 속도 조절
autopy.mouse.set_speed(2.0)

# 카메라 초기화
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        break

    # 손 제스처 추적
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # 손이 감지되면
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # 엄지 손가락의 끝 위치 확인
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            thumb_x, thumb_y = int(thumb_tip.x * screen_width), int(thumb_tip.y * screen_height)

            # 마우스 이동
            autopy.mouse.move(screen_width - thumb_x, thumb_y)

    # 화면에 출력
    cv2.imshow("Hand Tracking", frame)

    # 종료 조건
    if cv2.waitKey(1) & 0xFF == 27:  # 'ESC' 키를 누르면 종료
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()
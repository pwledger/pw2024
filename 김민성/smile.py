import cv2

# 웃음 감지 모델 로드
smile_cascade = cv2.CascadeClassifier('opencv-master\data\haarcascades\haarcascade_smile.xml')

# 카메라 캡처
cap = cv2.VideoCapture(0)

while True:
    # 카메라에서 이미지 읽기
    ret, img = cap.read()

    # 그레이스케일로 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 웃음 감지
    smiles = smile_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=15, minSize=(25,25))

    # 감지된 웃음이 나는 부분을 사각형으로 표시
    for (x, y, w, h) in smiles:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # 이미지 출력
    cv2.imshow('Smiling Face', img)

    # 키 입력 대기
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 리소스 해제
cap.release()
cv2.destroyAllWindows()
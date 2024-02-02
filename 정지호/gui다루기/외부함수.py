import cv2

def p(entry,entry1,label,label1):
    t = entry.get()
    if t == "label":
        내용 = entry1.get()
        label.config(text = 내용)
    elif t == "label1":
        내용 = entry1.get()
        label1.config(text = 내용)

def add(e1,e2,label):
    a = int(e1.get())
    b = int(e2.get())
    answer = f"{a} + {b} = {a+b}"
    label.config(text=answer)

def 얼굴():
    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # 모델 가져오기 
    face_cascade = cv2.CascadeClassifier(".\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml")

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

def 포즈():
    body_cascade = cv2.CascadeClassifier("opencv-master\data\haarcascades\haarcascade_fullbody.xml")
    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while cv2.waitKey(33) != ord('q'):
        ret, frame = capture.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        bodies = body_cascade.detectMultiScale(gray, 1.1, 3)

        for (x, y, w, h) in bodies:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()

def 고양이():
    cat_cascade = cv2.CascadeClassifier("opencv-master\data\haarcascades\haarcascade_frontalcatface.xml")
    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    while cv2.waitKey(33) != ord('q'):
        ret, frame = capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cat_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))
        for x,y,w,h in faces:
            frame = cv2.rectangle(frame, (x,y) , (x+w , y+h) , (255, 0, 0), 5, cv2.LINE_8)
        cv2.imshow("VideoFrame", frame)
    capture.release()
    cv2.destroyAllWindows()



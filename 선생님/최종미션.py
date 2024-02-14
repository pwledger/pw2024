import tkinter
import tkinter.font as tk_font

window = tkinter.Tk()
window.title("인식하기 기능 버튼으로 만들기")
window.geometry("640x400+100+100")
window.resizable(False,False)
font = tk_font.Font(family="맑은 고딕", size=20)

# 열 가중치 설정
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

# 행 가중치 설정
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)

face_button = tkinter.Button(window , text = "얼굴인식" , font = font)
face_button.grid(column=0 , row = 0 ,  sticky="nsew")

pose_button = tkinter.Button(window , text = "포즈인식" , font = font)
pose_button.grid(column=1 , row = 0 ,sticky="nsew")

cat_button = tkinter.Button(window , text = "고양이인식" , font = font)
cat_button.grid(column=0 , row = 1,  sticky="nsew")

hand_button = tkinter.Button(window , text = "손인식" , font = font)
hand_button.grid(column=1 , row = 1 ,  sticky="nsew")

window.mainloop()
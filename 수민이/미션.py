import tkinter
import tkinter.font as tk_font
import face
window = tkinter.Tk()
window.title("인식하기 기능 버튼으로 만들기")
window.geometry("640x400+100+100")
window.resizable(False,False)
font = tk_font.Font(family="맑은 고딕", size=20)

# 버튼 4개를 만들어 주세요

# 1번 : 얼굴인식 버튼 .. 버튼을 누루면 얼굴인식하는 기능이 동작 되도록하고 ... 감지한 얼굴 인원수 가 나오도록 하기
b1 = tkinter.Button(window , text = "얼굴인식" , font = font , command= face.얼굴인식)
b1.pack()
# 2번 : 고양이얼굴 인식 버튼 .. 버튼을 누루면 얼굴인식하는 기능이 동작 되도록하고 ... 감지한 얼굴 인원수 가 나오도록 하기

# 3번 : 전체 몸 인식 .. 인식한 인원수 표시

# 4번 : 손인식 .. 아직 미정 


window.mainloop()
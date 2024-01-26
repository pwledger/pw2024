import tkinter
import tkinter.font as tk_font

window=tkinter.Tk()
window.title("test")
window.geometry("640x400+100+100")
window.resizable(False, False)
font = tk_font.Font(family="맑은 고딕",size=20)
#외부함수 가져오기
import 외부함수

entry=tkinter.Entry(window ,font = font)
entry.pack()

entry1=tkinter.Entry(window ,font = font)
entry1.pack()

button = tkinter.Button(window , text="실행" ,font = font  , command=lambda : 외부함수.p(entry,entry1,label,label1))
button.pack()

label = tkinter.Label(window , text = "결과1" ,font = font)
label.pack()

label1 = tkinter.Label(window , text = "결과2" ,font = font)
label1.pack()

window.mainloop()
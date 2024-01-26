import tkinter
import tkinter.font as tk_font
import 외부함수

window=tkinter.Tk()
window.title("test")
window.geometry("640x400+100+100")
window.resizable(False, False)
font = tk_font.Font(family="맑은 고딕",size=20)

entry=tkinter.Entry(window ,font = font)
entry.pack()

entry1=tkinter.Entry(window ,font = font)
entry1.pack()

button = tkinter.Button(window , text="제출" ,font = font  , command=lambda : 외부함수.add(entry,entry1,label))
button.pack()

label = tkinter.Label(window , text = "결과" ,font = font)
label.pack()

window.mainloop()
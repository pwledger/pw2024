import tkinter
import tkinter.font as tk_font
import 외부함수

window=tkinter.Tk()
window.title("정지호tkinter")
window.geometry("640x400+100+100")
window.resizable(False, False)

button = tkinter.Button(window,text = "얼굴인식", overrelief="solid", command= 외부함수.얼굴)

button1 = tkinter.Button(window,text = "포즈인식", overrelief="solid",command= 외부함수.포즈 )

button2 = tkinter.Button(window,text = "고양이인식", overrelief="solid",command= 외부함수.고양이 )

button3 = tkinter.Button(window,text = "손인식", overrelief="solid", )

button.place(x=50, y=50, width=100, height=50)
button1.place(x=370, y=50, width=100, height=50)
button2.place(x=50, y=350, width=100, height=50)
button3.place(x=370, y=350, width=100, height=50)

window.mainloop()

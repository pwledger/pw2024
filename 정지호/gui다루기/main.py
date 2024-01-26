import tkinter
import tkinter.font as tk_font

window=tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("640x400+100+100")
window.resizable(False, False)

font = tk_font.Font(family="맑은 고딕",size=20)
label=tkinter.Label(window, text="파이썬", width=10, height=5, fg="red", relief="solid" , font = font)
label.pack()

window.mainloop()
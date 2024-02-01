import tkinter
import tkinter.font as tk_font

window = tkinter.Tk()
window.title("계산기")
window.geometry("640x400+100+100")
window.resizable(False,False)

font = tk_font.Font(family="맑은 고딕", size=20)

entry = tkinter.Entry(window,font=font)
entry.grid(column=4,row=0)
s = ""

def 기능(n):
    global s
    s += str(n)
    entry.delete(0,tkinter.END)
    entry.insert(0,s)
for i in range(10):
    b = tkinter.Button(window, text=f"{i}",font=font,bg="gray",fg="white",command=lambda i = i : 기능(i))
    b.grid(column=i%3,row=i//3 + 1)

plus = tkinter.Button(window,text=f"+",font=font,bg="gray",fg="white",command=lambda : 기능("+"))
plus.grid(column=3,row=1)
minus = tkinter.Button(window,text=f"-",font=font,bg="gray",fg="white",command=lambda : 기능("-"))
minus.grid(column=3,row=2)
times = tkinter.Button(window,text=f"x",font=font,bg="gray",fg="white",command=lambda : 기능("*"))
times.grid(column=3,row=3)

def end():
    global s
    s= entry.get()
    s = str(eval(s))
    entry.delete(0,tkinter.END)
    entry.insert(0,s)

equal = tkinter.Button(window,text=f"=",font=font,bg="gray",fg="white",command=end)
equal.grid(column=2,row=4)
def x():
    global s
    s = s[:len(s)-1]
    entry.delete(0,tkinter.END)
    entry.insert(0,s)

det = tkinter.Button(window,text=f"X",font=font,bg="gray",fg="white",command=x)
det.grid(column=1,row=4)
window.mainloop()
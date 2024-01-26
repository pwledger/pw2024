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
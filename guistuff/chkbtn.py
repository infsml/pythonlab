import tkinter as tk
t = tk.Tk()
t.geometry("640x480")


s = tk.StringVar()

texts = ['Omae','wa','mo','shinderu']
varsi = [tk.BooleanVar() for i in texts]
l = tk.Label(t,textvariable=s)

def upd():
    k=''
    for i in range(len(varsi)):
        if varsi[i].get():
            k += texts[i] + ' '
    s.set(k)

ck = [tk.Checkbutton(t,text=texts[i],variable=varsi[i],command=upd) for i in range(len(texts))]
for i in ck:
    i.pack()
l.pack()
t.mainloop()

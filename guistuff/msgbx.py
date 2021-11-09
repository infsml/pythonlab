import tkinter as tk
from tkinter import messagebox
t = tk.Tk()
t.geometry("640x480")

def sm(txt):
    k=messagebox.showinfo("FYI",txt+" was pressed")
    print(k)
    print(type(k))

#messagebox.showinfo("FYI","Omae wa mo shinderu")
b1 = tk.Button(t,text="red",command=lambda :sm("red"),relief=tk.SUNKEN)
b2 = tk.Button(t,text="blue",command = lambda :sm("blue"),activeforeground = "#5683eb")
b1.pack()
b2.pack()
t.mainloop()


#86,131,235
#56, 83, eb

import tkinter as tk
t = tk.Tk()
t.geometry("640x480")


s = tk.StringVar()

e = tk.Entry(t,textvariable=s,show='*')
l = tk.Label(t,textvariable=s)
e.pack()
l.pack()
t.mainloop()

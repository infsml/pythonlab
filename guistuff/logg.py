import tkinter as tk
t = tk.Tk()
t.geometry("640x480")


s1 = tk.StringVar()
s2 = tk.StringVar()
s3 = tk.StringVar()
s4 = tk.StringVar()

bol1 = tk.BooleanVar()

def login():
    s4.set("user: "+s1.get()+"\npass: "+s2.get())

l1 = tk.Label(t,text="User")
l2 = tk.Label(t,text="Pass")
e1 = tk.Entry(t,textvariable=s1)
e2 = tk.Entry(t,textvariable=s2,show="*")
def chkb():
    if bol1.get():
        e2.config(show = '')
        #l3.config(textvariable = s2)
    else:
        e2.config(show='*')
        #l3.config(textvariable = s3)

c1 = tk.Checkbutton(t,text = "Show password",command=chkb,variable=bol1)
b1 = tk.Button(t,text="Login",command = login)
l3 = tk.Label(t,textvariable=s3)
l4 = tk.Label(t,textvariable=s4)

l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
c1.grid(row=2,column=0)
l3.grid(row=2,column=1)
b1.grid(row=3,column=0)
l4.grid(row=4,column=0)

t.mainloop()

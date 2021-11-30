import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.geometry('640x480')

i = tk.BooleanVar()
i2 = tk.IntVar()
i3 = tk.StringVar()

rads = ['life','death','neither']
kst = 'all those who require it'.split()

def sothat():
	k = comb.get() + ' '
	if i.get():
		k += 'be '
	k += rads[i2.get()] + ' '
	c = lbx.curselection()
	for i5 in range(len(kst)):
		if i5 in c:
			k += kst[i5] + ' '
	i3.set(k)

but = tk.Button(win,text="Show",command=sothat);
comb = ttk.Combobox(win,values=['May','Maybe','Probably'])
chkbtn = tk.Checkbutton(win,text="be",variable=i)
rad1 = tk.Radiobutton(win,text="life",variable=i2,value=0)
rad2 = tk.Radiobutton(win,text="death",variable=i2,value=1)
rad3 = tk.Radiobutton(win,text="neither",variable=i2,value=2)
lbx = tk.Listbox(win,selectmode=tk.MULTIPLE)
for i5 in range(len(kst)):
	lbx.insert(i5,kst[i5])
lb = tk.Label(win,textvar=i3)
but.pack()
comb.pack()
chkbtn.pack()
rad1.pack()
rad2.pack()
rad3.pack()
lbx.pack()
lb.pack()
win.mainloop()
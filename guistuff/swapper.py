import tkinter as tk
t = tk.Tk()
t.geometry("640x480")

items = "Katra van dees is back".split(' ')
chks = []
varch = []
chks2 = []
varch2 = []
for i in range(len(items)):
    varch.append(tk.BooleanVar())
    varch2.append(tk.BooleanVar())
    chks.append(tk.Checkbutton(t,text=items[i],variable = varch[i]))
    chks[i].grid(row=i,column=0)
    chks2.append(tk.Checkbutton(t,text=items[i],variable = varch2[i]))
    #chks2[i].grid(row=i,column=1)
    #chks2[i].forget_grid()

def swp():
    k1 = 0
    k2 = 0
    for i range(len(chks)):
        

b = tk.Button(t,text='Swap',command=swp)
b.grid(row=len(items),column=0)
t.mainloop()

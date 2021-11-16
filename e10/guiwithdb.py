import tkinter as tk
import sqlite3

class GuiWithDB:
	def __init__(self):
		self.db = sqlite3.connect('data.db')
		self.cur = self.db.cursor()
		self.cur.execute('create table if not exists phonebook(name varchar(30),numb varchar(20));')
		self.db.commit()
		self.win = tk.Tk()
		self.win.geometry('640x480')
		self.fram = tk.Frame(self.win)
		self.fram.pack(side='top',expand=True,fill='both')
		self.insnamevar = tk.StringVar()
		self.insnumbvar = tk.StringVar()
		self.updnamevar = tk.StringVar()
		self.updnumbvar = tk.StringVar()
		self.deletnamevar =tk.StringVar()
		self.create_main()
		self.win.mainloop()
		self.db.close()
	def clear(self):
		for wid in self.fram.winfo_children():
			wid.destroy()
	def create_main(self):
		self.clear()
		but0 = tk.Button(self.fram,text='Insert',command=self.create_inser)
		but1 = tk.Button(self.fram,text='Delete',command=self.create_delet)
		but2 = tk.Button(self.fram,text='Update',command=self.create_upd)
		but3 = tk.Button(self.fram,text='Show',command=self.create_show)
		but0.pack()
		but1.pack()
		but2.pack()
		but3.pack()
	def create_inser(self):
		self.clear()
		lab1 = tk.Label(self.fram,text='Name')
		lab2 = tk.Label(self.fram,text='Numb')
		ent1 = tk.Entry(self.fram,textvar=self.insnamevar)
		ent2 = tk.Entry(self.fram,textvar=self.insnumbvar)
		but0 = tk.Button(self.fram,text='Insert',command=self.insourname)
		but1 = tk.Button(self.fram,text='Back',command=self.create_main)
		lab1.grid(row=0,column=0)
		ent1.grid(row=0,column=1)
		lab2.grid(row=1,column=0)
		ent2.grid(row=1,column=1)
		but0.grid(row=2,column=0)
		but1.grid(row=2,column=1)
	def create_show(self):
		self.clear()
		self.cur.execute('select * from phonebook;');
		dat = self.cur.fetchall()
		k = ''
		for i in dat:
			k += i[0] + '   ' +i[1]+'\n'
		lab1 = tk.Label(self.fram,text=k)
		but1 = tk.Button(self.fram,text='Back',command=self.create_main)
		lab1.pack()
		but1.pack()
	def create_delet(self):
		self.clear()
		lab1 = tk.Label(self.fram,text='Name')
		ent1 = tk.Entry(self.fram,textvar=self.deletnamevar)
		but0 = tk.Button(self.fram,text='Delete',command=self.deletourname)
		but1 = tk.Button(self.fram,text='Back',command=self.create_main)
		lab1.grid(row=0,column=0)
		ent1.grid(row=0,column=1)
		but0.grid(row=2,column=0)
		but1.grid(row=2,column=1)
	def create_upd(self):
		self.clear()
		lab1 = tk.Label(self.fram,text='Name')
		lab2 = tk.Label(self.fram,text='Numb')
		ent1 = tk.Entry(self.fram,textvar=self.updnamevar)
		ent2 = tk.Entry(self.fram,textvar=self.updnumbvar)
		but0 = tk.Button(self.fram,text='Update',command=self.updourname)
		but1 = tk.Button(self.fram,text='Back',command=self.create_main)
		lab1.grid(row=0,column=0)
		ent1.grid(row=0,column=1)
		lab2.grid(row=1,column=0)
		ent2.grid(row=1,column=1)
		but0.grid(row=2,column=0)
		but1.grid(row=2,column=1)
	def insourname(self):
		self.cur.execute('insert into phonebook values(?,?)',(self.insnamevar.get(),self.insnumbvar.get()))
		self.db.commit()
		self.insnamevar.set('')
		self.insnumbvar.set('')
	def deletourname(self):
		self.cur.execute('delete from phonebook where name=?',(self.deletnamevar.get(),))
		self.db.commit()
		self.deletnamevar.set('')
	def updourname(self):
		self.cur.execute('update phonebook set numb=? where name=?',(self.updnumbvar.get(),self.updnamevar.get()))
		self.db.commit()
		self.updnamevar.set('')
		self.updnumbvar.set('')
GuiWithDB()
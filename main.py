from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.geometry('600x500+600+300')
ws.title('To Do List')
ws.config(bg='#A7C7E7')
ws.resizable(width=False, height=False)
ws.mainloop()

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
	frame,
	width=25,
	height=8,
	font=('Times', 18),
	bd = 1,
	fg='#464646',
	highlightthickness=0,
	selectbackground='#q6q6q6',
	activestyle='none',
)

lb.pack(side=LEFT, fill=BOTH)

task_list = [
	'drink water',
]
for item in task_list :
	lb.insert(END,item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
	ws,
	font = ('times', 24)
)

my_entry.pack(pady=20)

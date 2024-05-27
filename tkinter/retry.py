import tkinter
from tkinter import ttk

root = tkinter.Tk()
content = ttk.Frame(root)
frame = ttk.Frame(content,width =200,height = 100,borderwidth=5,relief="ridge")

onevalue = tkinter.BooleanVar(value=True)
twovalue = tkinter.BooleanVar(value=False)
threevalue = tkinter.BooleanVar(value=True)

one = ttk.Checkbutton(content,text="one",variable = onevalue,offvalue=True)
two = ttk.Checkbutton(content,text="two",variable = twovalue)
three = ttk.Checkbutton(content,text="three",variable = threevalue)
namelbl = ttk.Label(content,text="Name")
name = ttk.Entry(content)
ok = ttk.Button(content,text="Okay")
cancel = ttk.Button(content,text="Cancel",command=root.destroy)

content.grid(row=0,column=0)
frame.grid(row=0,column=0,columnspan=3,rowspan=2)
namelbl.grid(column=3,row=0,columnspan=2)
name.grid(column=3,row=1,columnspan=2)
one.grid(column=0,row=3)
two.grid(column=1,row=3)
three.grid(column=2,row=3)
ok.grid(column=3,row=3)
cancel.grid(column=4,row=3)

root.mainloop()

from tkinter import *
from tkinter import ttk
import re


root = Tk()
root.title("Hello World!")

def check_num(newval):
    return re.match('^[0-9]*$', newval) is not None and len(newval) <= 5
check_num_wrapper = (root.register(check_num), '%P')

username = StringVar()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World.", background="red").grid(row=10, column=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(row=10, column=1)
Lb2 = ttk.Label(frm, text="go in", font="Arial", foreground="RED").grid(
    column=1, row=11)
label2 = ttk.Label(text=username) 
label2.grid()
name = ttk.Entry(frm,textvariable = username,width = 8)
name.grid()
name.bind('<Return>',lambda e: label2.configure(text = username.get()))
num = StringVar()
e = ttk.Entry(root, textvariable=num, validate='key', validatecommand=check_num_wrapper)
e.grid(column=0, row=0, sticky='we')

root.mainloop()

    




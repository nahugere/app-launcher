from tkinter import *
from tkinter import filedialog
from db import Database
import pathlib
from PIL import Image, ImageTk

file_dir = str(pathlib.Path(__file__).parent.absolute())

d = Database(file_dir+"\\app.db")

root = Tk()
root.geometry("500x600")
# root.call('wm', 'iconphoto', root._w, PhotoImage(file=file_dir+"\\logo.ico"))
root.title("app launcher")

def launch():
    index = list_box.curselection()[0]
    selected_path = list_box.get(index)
    a=[selected_path.split("/")]
    path = d.pass_selected_app(a[0][0])
    path_got = path[-1][1]
    import os
    os.startfile(path_got)
    a.clear()

def add():
    filed = filedialog.askopenfilename(filetypes=(("executables","*.exe"),("all files", "*.*")))
    a=[filed.split("/")]
    if filed=="":
        pass
    else:
        d.add_app(a[0][-1], filed)
    list_it()
    a.clear()

def delete():
    index = list_box.curselection()
    selected_name = list_box.get(index)
    d.remove_app(selected_name)
    list_it()

frame = Frame(root, width=500, height=600, bg="white")
frame.pack(expand=1, fill=BOTH, side=TOP)

list_box = Listbox(frame, font=("", 15), border=0, highlightthickness=0)
list_box.pack(expand=1, fill=BOTH, side=LEFT)

scrl = Scrollbar(frame)
scrl.pack(side=RIGHT, fill=Y)

# scrlx = Scrollbar(root)
# scrlx.pack(side=TOP, anchor=N, fill=X)

list_box.config(yscrollcommand=scrl.set)#, xscrollcommand=scrlx.set)
scrl.config(command=list_box.yview)
# scrlx.config(command=list_box.xview)

btn = Button(root, text="Launch", width=300, font=("Bad Script Regular",10), bg="green", fg="white", command=launch)
btn.pack( anchor=N)

btn2 = Button(root, text="Add", width=300, font=("Bad Script Regular",10), bg="green", fg="white", command=add)
btn2.pack( anchor=S)

del_btn = Button(root, text="Delete", width=300, font=("Bad Script Regular",10), bg="green", fg="white", command=delete)
del_btn.pack(anchor=S)

def list_it():
    list_box.delete(0,END)
    apps = d.pass_apps()
    for app in apps:
        a = [app[0].split("/")]
        list_box.insert(END, a[-1][-1])
        a.clear()

list_it()

root.mainloop()

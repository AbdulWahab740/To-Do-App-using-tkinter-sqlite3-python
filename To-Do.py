import sqlite3
from tkinter import *
from tkinter.messagebox import showwarning
from datetime import datetime

conn = sqlite3.connect('data.db')
cursor  = conn.cursor()

conn.execute('''CREATE TABLE IF NOT EXISTS to_do_Data (
               Title TEXT, Task TEXT
)
''')
def add():
    new_text = entry.get() 
    name_text = name.get()

    if new_text == "":
        showwarning("Warning",'You have to write the task in case of Add text')
    elif name_text == "":
        showwarning("Warning",'You have to write the title of your To Do Task in case of Add text')
    elif new_text: 
        lbx.insert(END, new_text)
        #Insert Data
        data_insert_query = '''INSERT INTO  to_do_Data (Title, Task) VALUES (?,?)'''
        data_insert_tuple = (new_text,name_text)
        cursor.execute(data_insert_query,data_insert_tuple)
        conn.commit()
        conn.close()

root = Tk()
root.geometry("620x500")
root.title("AW's To-do App")

Label(root,text="To Do App",font=('Arial', 16 ,'bold underline'),pady=10,justify='center').pack()
name = StringVar()
dtvar = StringVar()

tit = Label(root,text="Enter the title of the task you have to do: ",font=('Arial', 10))
tit.pack(anchor='w')

ent = Entry(root,font=('Arial', 10),textvariable=name)
ent.pack(padx=100,pady=5)

dt = Label(root,text="Enter the due date of the task (Optional): (20YY-MM-DD)",font=('Arial', 10))
dt.pack(anchor='w')
entdt = Entry(root,font=('Arial', 10),textvariable=dt)
entdt.pack(padx=100,pady=5)

lbl_lbx = Label(root,text="Enter your To Do Task Here: ",font=('Arial', 10))
lbl_lbx.pack(anchor='w')
lbx =Listbox(root,height=14,width=80,justify='center')
entry = Entry(root,font=('Arial', 11),width=50)
entry.pack(pady=5)
Button(root,text="Add Text",command=add,relief = 'sunken',font="Arial 10 bold").pack(padx=5,pady=3)

lbx.pack()
lbx.insert(END)

root.mainloop()

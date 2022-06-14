import mainclasses as mc
from tkinter import *
from os import *
from tkinter import filedialog
from tkinter import ttk

window = Tk()
window.geometry('1620x1080')
window.title('Biba')

building = LabelFrame(window, text='Здание')
building.pack(expand=1, fill='both')

wallsamount = IntVar()
wallsamount.set(4)

wa = Spinbox(building, from_=3, to=20, width=8, textvariable=wallsamount)
wa.grid(column=0, row=0, padx=10, pady=5)

def wa_accept_command():
    wallsamount.set(wa.get())
wa_accept = Button(building, text='Применить', command=wa_accept_command)
wa_accept.grid(column=1, row=0)




window.mainloop()
import mainclasses
from tkinter import *
from os import *
from tkinter import filedialog

def clicked1():
    dir = filedialog.askdirectory()
    lbl.configure(text=dir)

def clicked2():
    window.quit()

window = Tk()
window.geometry('400x250')

lbl = Label(window, text='Z:/wordedit/TestDir')
lbl.grid(column=0, row=0)

btn1 = Button(window, text='Choose directory', command=clicked1)
btn1.grid(column=0, row=1)

btn2 = Button(window, text='SAVE', command=clicked2)
btn2.grid(column=0, row=2)

window.mainloop()
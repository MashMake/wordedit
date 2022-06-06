from tkinter import *

def clicked():
    res = 'Booped {0}!'.format(txt.get())
    lbl.configure(text=res)

window = Tk()
window.geometry('600x400')
window.title("Шindoш")

lbl = Label(window, text='Booped you!')
lbl.grid(column=0, row=0)

txt = Entry(window, width=10)
txt.grid(column=0, row=2)

btn = Button(window, text='Boop', command=clicked)
btn.grid(column=0, row=1)

window.mainloop()
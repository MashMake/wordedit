import mainclasses as mc
from tkinter import *
from os import *
from tkinter import filedialog
from tkinter import ttk

walls = [mc.Wall(1.5, 500, 0) for i in range(4)]

window = Tk()
window.geometry('1620x1080')
window.title('Biba')

tab_control = ttk.Notebook(window)
maintab = ttk.Frame(tab_control)




window.mainloop()
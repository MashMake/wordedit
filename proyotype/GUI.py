import mainclasses as mc
from tkinter import *

window = Tk()
window.geometry('300x250')
window.title('Choose number of walls')

building = LabelFrame(window, text='Здание')
building.pack()

wallsamount = IntVar()
wallsamount.set(4)

isAccepted = False
wlb = []
we = []

walls = [mc.Wall(1.5, 500, 0) for i in range(wallsamount.get())]
lb1 = Label(building, text='Количество стен')
lb1.grid(column=0, row=0)
wa = Spinbox(building, from_=3, to=20, width=8, textvariable=wallsamount)
wa.grid(column=1, row=0, padx=10, pady=5)

def wa_accept_command():
    global isAccepted
    if not isAccepted: return

    global walls
    global wlb
    global we
    wallsamount.set(wa.get())
    walls = [mc.Wall(1.5, 500, 0) for i in range(wallsamount.get())]
    wlb = [LabelFrame(window, text='Стена {}'.format(i + 1)) for i in range(wallsamount.get())]
    for i in range(wallsamount.get()): wlb[i].pack()
    for i in range(wallsamount.get()):
        wlbl = Label(wlb[i], text='Ширина')
        wlbl.grid(column=0, row=0)
        slbl = Label(wlb[i], text='Площадь')
        slbl.grid(column=0, row=1)
        tlbl = Label(wlb[i], text='Тип')
        tlbl.grid(column=0, row=2)
        

wa_accept = Button(building, text='Применить', command=wa_accept_command)
wa_accept.grid(column=2, row=0)




window.mainloop()

print('Введите количество стен в диапазоне от 3 до 10 включительно: ', end='')
wa = int(input())

while wa < 3 or wa > 10:
    print('Введите количество стен в диапазоне от 3 до 10 включительно: ', end='')
    wa = int(input())
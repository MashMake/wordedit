import mainclasses as mc
from tkinter import *
from os import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.ttk import Checkbutton
wa = 3

window = Tk()
window.geometry('600x650')
window.title('Walls configure')

tab_control = ttk.Notebook(window)

maintab = ttk.Frame(tab_control)
tab_control.add(maintab, text='Здание')

walltabs = []
walls = [mc.Wall(1.5, 500, 0) for i in range(wa)]
for i in range(wa):
    walltabs.append(ttk.Frame(tab_control))
    tab_control.add(walltabs[i], text='Стена {}'.format(i+1))

wlb = []
slb = []
tlb = []
for i in range(wa):
    wlb.append(Label(walltabs[i], text='Ширина'))
    wlb[i].grid(column=0, row=0)
    slb.append(Label(walltabs[i], text='Площадь'))
    slb[i].grid(column=0, row=1)
    tlb.append(Label(walltabs[i], text='Тип'))
    tlb[i].grid(column=0, row=2)

wen = []
sen = []
ten = []
for i in range(wa):
    wen.append(Entry(walltabs[i], width=10))
    wen[i].grid(column=1, row=0)
    sen.append(Entry(walltabs[i], width=10))
    sen[i].grid(column=1, row=1)
    ten.append(Entry(walltabs[i], width=10))
    ten[i].grid(column=1, row=2)

le = []
ll = []
for i in range(wa):
    ll.append(Label(walltabs[i], text='Слои (толщина теплопроводность)'))
    ll[i].grid(column=0, row=3)
    le.append(Entry(walltabs[i], width=10))
    le[i].grid(column=1, row=3)

a0 = []
a1 = []
a2 = []
a3 = []
a4 = []
a5 = []
a6 = []
for i in range(wa):
    a0.append(Checkbutton(walltabs[i], text='Гибкие связи'))
    a0[i].grid(column=0, row=4)
    a1.append(Checkbutton(walltabs[i], text='Тарельчатый анкер'))
    a1[i].grid(column=0, row=6)
    a2.append(Checkbutton(walltabs[i], text='Кронштейн'))
    a2[i].grid(column=0, row=8)
    a3.append(Checkbutton(walltabs[i], text='Сопряжение с перекрытиями и балконами'))
    a3[i].grid(column=0, row=10)
    a4.append(Checkbutton(walltabs[i], text='Стыки с оконными блоками'))
    a4[i].grid(column=0, row=14)
    a5.append(Checkbutton(walltabs[i], text='Примыкание к цокольному ограждению'))
    a5[i].grid(column=0, row=18)


a0vl = []
a0al = []
for i in range(wa):
    a0vl.append(Label(walltabs[i], text='Теплопотери'))
    a0vl[i].grid(column=0, row=5)
    a0al.append(Label(walltabs[i], text='Геом.Величина'))
    a0al[i].grid(column=2, row=5)

a0ven = []
a0aen = []
for i in range(wa):
    a0ven.append(Entry(walltabs[i], width=10))
    a0ven[i].grid(column=1, row=5)
    a0aen.append(Entry(walltabs[i], width=10))
    a0aen[i].grid(column=3, row=5)


a1vl = []
a1al = []
for i in range(wa):
    a1vl.append(Label(walltabs[i], text='Длина'))
    a1vl[i].grid(column=0, row=7)
    a1al.append(Label(walltabs[i], text='Геом.Величина'))
    a1al[i].grid(column=2, row=7)

a1ven = []
a1aen = []
for i in range(wa):
    a1ven.append(Entry(walltabs[i], width=10))
    a1ven[i].grid(column=1, row=7)
    a1aen.append(Entry(walltabs[i], width=10))
    a1aen[i].grid(column=3, row=7)


a2vl = []
a2al = []
for i in range(wa):
    a2vl.append(Label(walltabs[i], text='Теплопотери'))
    a2vl[i].grid(column=0, row=9)
    a2al.append(Label(walltabs[i], text='Геом.Величина'))
    a2al[i].grid(column=2, row=9)

a2ven = []
a2aen = []
for i in range(wa):
    a2ven.append(Entry(walltabs[i], width=10))
    a2ven[i].grid(column=1, row=9)
    a2aen.append(Entry(walltabs[i], width=10))
    a2aen[i].grid(column=3, row=9)


a3il = []
a3wl = []
a3cl = []
a3tl = []
a3pl = []
a3vl = []
for i in range(wa):
    a3il.append(Label(walltabs[i], text='Теплопроводность'))
    a3il[i].grid(column=0, row=11)
    a3wl.append(Label(walltabs[i], text='Ширина плиты'))
    a3wl[i].grid(column=2, row=11)
    a3cl.append(Label(walltabs[i], text='Термическое сопротивление'))
    a3cl[i].grid(column=0, row=12)
    a3tl.append(Label(walltabs[i], text='Тип перфорации(0,1,2)'))
    a3tl[i].grid(column=2, row=12)
    a3pl.append(Label(walltabs[i], text='Коэффициент перфорации'))
    a3pl[i].grid(column=0, row=13)
    a3vl.append(Label(walltabs[i], text='Геом.Величина'))
    a3vl[i].grid(column=2, row=13)

a3ien = []
a3wen = []
a3cen = []
a3ten = []
a3pen = []
a3ven = []
for i in range(wa):
    a3ien.append(Entry(walltabs[i], width=10))
    a3ien[i].grid(column=1, row=11)
    a3wen.append(Entry(walltabs[i], width=10))
    a3wen[i].grid(column=3, row=11)
    a3cen.append(Entry(walltabs[i], width=10))
    a3cen[i].grid(column=1, row=12)
    a3ten.append(Entry(walltabs[i], width=10))
    a3ten[i].grid(column=3, row=12)
    a3pen.append(Entry(walltabs[i], width=10))
    a3pen[i].grid(column=1, row=13)
    a3ven.append(Entry(walltabs[i], width=10))
    a3ven[i].grid(column=3, row=13)


a4il = []
a4wl = []
a4cl = []
a4tl = []
a4vl = []
for i in range(wa):
    a4il.append(Label(walltabs[i], text='Теплопроводность'))
    a4il[i].grid(column=0, row=15)
    a4wl.append(Label(walltabs[i], text='Ширина плиты'))
    a4wl[i].grid(column=2, row=15)
    a4cl.append(Label(walltabs[i], text='Термическое сопротивление'))
    a4cl[i].grid(column=0, row=16)
    a4tl.append(Label(walltabs[i], text='Тип перфорации(0,1,2)'))
    a4tl[i].grid(column=2, row=16)
    a4vl.append(Label(walltabs[i], text='Геом.Величина'))
    a4vl[i].grid(column=2, row=17)

a4ien = []
a4wen = []
a4cen = []
a4ten = []
a4ven = []
for i in range(wa):
    a4ien.append(Entry(walltabs[i], width=10))
    a4ien[i].grid(column=1, row=15)
    a4wen.append(Entry(walltabs[i], width=10))
    a4wen[i].grid(column=3, row=15)
    a4cen.append(Entry(walltabs[i], width=10))
    a4cen[i].grid(column=1, row=16)
    a4ten.append(Entry(walltabs[i], width=10))
    a4ten[i].grid(column=3, row=16)
    a4ven.append(Entry(walltabs[i], width=10))
    a4ven[i].grid(column=3, row=17)

a5rl = []
a5wl = []
a5cl = []
a5vl = []
for i in range(wa):
    a5rl.append(Label(walltabs[i], text='Сопротивление слоя на стене'))
    a5rl[i].grid(column=0, row=19)
    a5cl.append(Label(walltabs[i], text='Теплопроводность'))
    a5cl[i].grid(column=2, row=19)
    a5wl.append(Label(walltabs[i], text='Сопротивление слоя на плите'))
    a5wl[i].grid(column=0, row=20)
    a5vl.append(Label(walltabs[i], text='Геом.Величина'))
    a5vl[i].grid(column=2, row=20)

a5ren = []
a5wen = []
a5cen = []
a5ven = []
for i in range(wa):
    a5ren.append(Entry(walltabs[i], width=10))
    a5ren[i].grid(column=1, row=19)
    a5cen.append(Entry(walltabs[i], width=10))
    a5cen[i].grid(column=3, row=19)
    a5wen.append(Entry(walltabs[i], width=10))
    a5wen[i].grid(column=1, row=20)
    a5ven.append(Entry(walltabs[i], width=10))
    a5ven[i].grid(column=3, row=20)

#покрытия перекрытия: термическое из слоёв, ПРИВЕДЁННОЕ - термическое * коэф.одн, коэф.одн. вручную
#окна и двери только площадь и приведённое сопротивление вручную
#


def generate():
    window.quit()

AcceptButton = Button(maintab, text='Расчитать', command=generate)
AcceptButton.grid(column=0, row=0)




tab_control.pack(expand=1, fill='both')
window.mainloop()
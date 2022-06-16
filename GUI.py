from msilib.schema import CheckBox
import mainclasses as mc
from tkinter import *
from os import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.ttk import Checkbutton
from tkinter.ttk import Combobox
from docx import Document
from docx.shared import Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH


wa = 3

window = Tk()
window.geometry('750x550')
window.title('Walls configure')

tab_control = ttk.Notebook(window)

maintab = ttk.Frame(tab_control)
tab_control.add(maintab, text='Здание')

walltabs = []
walls = [mc.Wall(1.5, 500, 0) for i in range(wa)]
for i in range(wa):
    walltabs.append(ttk.Frame(tab_control))
    tab_control.add(walltabs[i], text='Стена {}'.format(i+1))


slb = []
tlb = []
for i in range(wa):
    slb.append(Label(walltabs[i], text='Площадь'))
    slb[i].grid(column=0, row=1)
    tlb.append(Label(walltabs[i], text='Тип'))
    tlb[i].grid(column=0, row=2)


sen = []
ten = []
for i in range(wa):
    sen.append(Entry(walltabs[i], width=10))
    sen[i].grid(column=1, row=1)
    ten.append(Combobox(walltabs[i], width=30))
    ten[i]['values'] = ('Трехслойные стены', 'СФТК', 'Системы наружной теплоизоляции')
    ten[i].grid(column=1, row=2)

a0 = []
a1 = []
a2 = []
a3 = []
a4 = []
a5 = []
a0c = []
a1c = []
a2c = []
a3c = []
a4c = []
a5c = []
for i in range(wa):
    a0c.append(IntVar())
    a0.append(Checkbutton(walltabs[i], text='Гибкие связи', variable=a0c[i]))
    a0[i].grid(column=0, row=4)
    a1c.append(IntVar())
    a1.append(Checkbutton(walltabs[i], text='Тарельчатый анкер', variable=a1c[i]))
    a1[i].grid(column=0, row=6)
    a2c.append(IntVar())
    a2.append(Checkbutton(walltabs[i], text='Кронштейн', variable=a2c[i]))
    a2[i].grid(column=0, row=8)
    a3c.append(IntVar())
    a3.append(Checkbutton(walltabs[i], text='Сопряжение с перекрытиями и балконами', variable=a3c[i]))
    a3[i].grid(column=0, row=10)
    a4c.append(IntVar())
    a4.append(Checkbutton(walltabs[i], text='Стыки с оконными блоками', variable=a4c[i]))
    a4[i].grid(column=0, row=14)
    a5c.append(IntVar())
    a5.append(Checkbutton(walltabs[i], text='Примыкание к цокольному ограждению', variable=a5c[i]))
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
    a3tl.append(Label(walltabs[i], text='Тип перфорации'))
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
    a3ten.append(Combobox(walltabs[i], width=10))
    a3ten[i]['values'] = ('нет', 'перфорация', 'НТЭ')
    a3ten[i].grid(column=3, row=12)
    a3pen.append(Combobox(walltabs[i], width=10))
    a3pen[i]['values'] = ('1/1', '1/3', '1/5')
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
    a4tl.append(Label(walltabs[i], text='Тип перфорации'))
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
    a4ten.append(Combobox(walltabs[i], width=10))
    a4ten[i]['values'] = ('нет', 'перфорация', 'НТЭ')
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


lnl = Label(maintab, text='Слои:')
lnl.grid(column=0, row=1)

l1c = IntVar()
l1l = Checkbutton(maintab, text='Слой 1', variable=l1c)
l1l.grid(column=0, row=2)
l2c = IntVar()
l2l = Checkbutton(maintab, text='Слой 2', variable=l2c)
l2l.grid(column=0, row=3)
l3c = IntVar()
l3l = Checkbutton(maintab, text='Слой 3', variable=l3c)
l3l.grid(column=0, row=4)
l4c = IntVar()
l4l = Checkbutton(maintab, text='Слой 4', variable=l4c)
l4l.grid(column=0, row=5)

l1nl = Label(maintab, text='Название')
l1nl.grid(column=1, row=2)
l2nl = Label(maintab, text='Название')
l2nl.grid(column=1, row=3)
l3nl = Label(maintab, text='Название')
l3nl.grid(column=1, row=4)
l4nl = Label(maintab, text='Название')
l4nl.grid(column=1, row=5)

l1nen = Entry(maintab, width=30)
l1nen.grid(column=2, row=2)
l2nen = Entry(maintab, width=30)
l2nen.grid(column=2, row=3)
l3nen = Entry(maintab, width=30)
l3nen.grid(column=2, row=4)
l4nen = Entry(maintab, width=30)
l4nen.grid(column=2, row=5)

l1dl = Label(maintab, text='Диаметр')
l1dl.grid(column=3, row=2)
l2dl = Label(maintab, text='Диаметр')
l2dl.grid(column=3, row=3)
l3dl = Label(maintab, text='Диаметр')
l3dl.grid(column=3, row=4)
l4dl = Label(maintab, text='Диаметр')
l4dl.grid(column=3, row=5)

l1den = Entry(maintab, width=10)
l1den.grid(column=4, row=2)
l2den = Entry(maintab, width=10)
l2den.grid(column=4, row=3)
l3den = Entry(maintab, width=10)
l3den.grid(column=4, row=4)
l4den = Entry(maintab, width=10)
l4den.grid(column=4, row=5)

l1cl = Label(maintab, text='Теплопроводность')
l1cl.grid(column=5, row=2)
l2cl = Label(maintab, text='Теплопроводность')
l2cl.grid(column=5, row=3)
l3cl = Label(maintab, text='Теплопроводность')
l3cl.grid(column=5, row=4)
l4cl = Label(maintab, text='Теплопроводность')
l4cl.grid(column=5, row=5)

l1cen = Entry(maintab, width=10)
l1cen.grid(column=6, row=2)
l2cen = Entry(maintab, width=10)
l2cen.grid(column=6, row=3)
l3cen = Entry(maintab, width=10)
l3cen.grid(column=6, row=4)
l4cen = Entry(maintab, width=10)
l4cen.grid(column=6, row=5)


popel = Label(maintab, text='Покрытия и перекрытия:')
popel.grid(column=0, row=6)

cl = Label(maintab, text='Коэф.однородности')
cl.grid(column=0, row=7)

cen = Entry(maintab, width=10)
cen.grid(column=1, row=7)


wdl = Label(maintab, text='Окна и двери:')
wdl.grid(column=0, row=8)

wdsl = Label(maintab, text='Площадь')
wdsl.grid(column=0, row=9)

wdsen = Entry(maintab, width=10)
wdsen.grid(column=1, row=9)

wdrl = Label(maintab, text='Приведённое сопротивление')
wdrl.grid(column=0, row=10)

wdren = Entry(maintab, width=10)
wdren.grid(column=1, row=10)



def generate():
    print('processing')
    doc = Document('0.docx')
    layers_table = doc.tables[0]
    if l1c.get():
        









AcceptButton = Button(maintab, text='Расчитать', command=generate)
AcceptButton.grid(column=0, row=0)



tab_control.pack(expand=1, fill='both')
window.mainloop()
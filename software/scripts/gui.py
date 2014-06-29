#!/usr/bin/env python3

from tkinter import *
from tkinter.ttk import *

from init_frequency import initFrequency
from init_frequency import clearAll
from init_frequency import pidEnable
from init_frequency import pidDisable
from init_frequency import writePid
from init_frequency import setAmpl

#Импортируем один из пакетов Matplotlib
import pylab
#Импортируем пакет со вспомогательными функциями
from matplotlib import mlab

counter = 0
is_show_graph = False

i = 0
xlist = list()
ylist = list()

#graph.ion()
pylab.ion()

#graph = pylab.figure()
#pylab.close()

def show_graph():
    global is_show_graph
    is_show_graph = not is_show_graph
    
def show_graph_fun():
    global pylab
    global counter
    global i
    global xlist
    global ylist
    
    i += 1
    xlist.append(i)

    ylist.append(counter)
    pylab.clf()
    #pylab.close()
    pylab.plot(xlist, ylist)
    pylab.draw()
    
    
def test_fun():
    
    #print(s)
    global outputSignalEntry
    #s = outputSignalEntry.insert(10, "aaa"), 
    s = outputSignalEntry.get()
    print(s)

def entry_callback(event):
    test_fun()

def timer_fun():
    global outputSignalEntry
    global counter
    global root
    counter += 1
    outputSignalEntry.delete(0, 5)
    outputSignalEntry.insert(0, str(counter)) 
    root.after(500, timer_fun)
    
    if is_show_graph:
        show_graph_fun()

def button_clicked():
    print("Старт!")
    initFrequency()
    
def button_clear():
    print("очистить")
    clearAll()

def button_startPid():
    print("вкл ПИД")
    pidEnable()

def button_stopPid():
    print("выкл ПИД")
    pidDisable()

kp = 0.05
ki = 0.05
    
def adjPid(Kp, Ki):
    global ki
    global kp
    print("kp = " + str(kp) + " ki = " + str(ki))
    kpTmp = kp * 65535
    kiTmp = ki * 65535
    writePid(Kp = int(kpTmp), Ki = int(kiTmp))
    
def button_writePid():    
    adjPid(Kp = kp, Ki = ki)

def button_KpPlus():
    global kp
    kp += 0.01
    adjPid(Kp = kp, Ki = ki)

def button_KpMinus():
    global kp
    kp -= 0.01
    adjPid(Kp = kp, Ki = ki)
    
def button_KiPlus():
    global ki
    ki += 0.01
    adjPid(Kp = kp, Ki = ki)

def button_KiMinus():
    global ki
    ki -= 0.01
    adjPid(Kp = kp, Ki = ki)

ampl = 10
def button_AmplPlus():
    global ampl
    ampl += 1
    print("ampl = " + str(ampl))
    setAmpl(ampl)
    
def button_AmplMinus():
    global ampl
    ampl -= 1
    print("ampl = " + str(ampl))
    setAmpl(ampl)
    
componentHeigth = 25
componentWidth = 120
yMargin = 10
xMargin = 10

xCoordinateSecond = componentWidth + 2*xMargin

root=Tk()
root.geometry('270x560')
root.title("AFC SMM")
# кнопка по умолчанию
button1 = Label(root, background = 'green')
#button1.pack()
button1.place(x = 10, y = yMargin, width = componentWidth, height = componentHeigth)

# кнопка с указанием родительского виджета и несколькими аргументами
button2 = Button(root, text=u"Автонастройка", command=button_clicked)
button2.place(x = componentWidth + 2*xMargin, y = yMargin, width = componentWidth, height = componentHeigth)

outpuSignalLabel = Label(root, text = "Управление")
outpuSignalLabel.place(x = xMargin, y = componentHeigth + yMargin * 2, width = componentWidth, height = componentHeigth)
outputSignalEntry = Entry(root, justify = RIGHT)
outputSignalEntry.place(x = xCoordinateSecond, y = componentHeigth + yMargin * 2, width = componentWidth, height = componentHeigth)
#outputSignalEntry.insert(10, 'adsf')

firstHarmonicLabel = Label(root, text = "Первая гармоника")
firstHarmonicLabel.place(x = xMargin, y = componentHeigth*2 + yMargin * 3, width = componentWidth, height = componentHeigth)
firstHarmonicEntry = Entry(root, justify = RIGHT)
firstHarmonicEntry.bind("<Return>", entry_callback)
firstHarmonicEntry.place(x = xCoordinateSecond, y = componentHeigth*2 + yMargin * 3, width = componentWidth, height = componentHeigth)

secondHarmonicLabel = Label(root, text = "Вторая гармоника")
secondHarmonicLabel.place(x = xMargin, y = componentHeigth*3 + yMargin * 4, width = componentWidth, height = componentHeigth)
secondHarmonicEntry = Entry(root, justify = RIGHT)
secondHarmonicEntry.place(x = xCoordinateSecond, y = componentHeigth*3 + yMargin * 4, width = componentWidth, height = componentHeigth)

separatorLabel = Label(root, background = 'black').place(x = 0, y = componentHeigth*4 + yMargin * 6, width = 270, height = 1)
#-----------------------------------------------------------------------------------------------------

componentWidthSmall = 50
xCoordinateSmall = componentWidthSmall + 2*xMargin
xCoordinateSecondSmall = 140
xCoordinateThirdSmall = xCoordinateSecondSmall + componentWidthSmall + xMargin

kpLabel = Label(root, text = "Kp")
kpLabel.place(x = xMargin, y = componentHeigth*4 + yMargin * 7, width = componentWidthSmall, height = componentHeigth)
kpEdit = Entry(root, justify = CENTER)
kpEdit.place(x = xCoordinateSmall, y = componentHeigth*4 + yMargin * 7, width = componentWidthSmall, height = componentHeigth)

kiLabel = Label(root, text = "Ki")
kiLabel.place(x = xCoordinateSecondSmall, y = componentHeigth*4 + yMargin * 7, width = componentWidthSmall, height = componentHeigth)
kiEdit = Entry(root)
kiEdit.place(x = xCoordinateThirdSmall, y = componentHeigth*4 + yMargin * 7, width = componentWidthSmall, height = componentHeigth)

amplModLabel = Label(root, text = "Амплитуда").place(x = xMargin, y = componentHeigth*5 + yMargin * 8, width = componentWidth, height = componentHeigth)
amplModEdit = Entry(root)
amplModEdit.place(x = xCoordinateSecond, y = componentHeigth*5 + yMargin * 8, width = componentWidth, height = componentHeigth)

phaseModLabel = Label(root, text = "Фаза")
phaseModLabel.place(x = xMargin, y = componentHeigth*6 + yMargin * 9, width = componentWidth, height = componentHeigth)
phaseModEdit = Entry(root)
phaseModEdit.place(x = xCoordinateSecond, y = componentHeigth*6 + yMargin * 9, width = componentWidth, height = componentHeigth)

helpButton = Button(root, text=u"Справка").place(x = xMargin, y = componentHeigth*7 + yMargin * 10, width = componentWidth, height = componentHeigth)


buttonClear = Button(root, text=u"Обнулить", command=button_clear).place(x = xMargin, y = componentHeigth*8 + yMargin * 11, width = componentWidth, height = componentHeigth)
buttonEnPid = Button(root, text=u"Вкл. ПИД", command=button_startPid).place(x = xMargin, y = componentHeigth*9 + yMargin * 12, width = componentWidth, height = componentHeigth)
buttonDisPid = Button(root, text=u"Выкл ПИД", command=button_stopPid).place(x = xMargin, y = componentHeigth*10 + yMargin * 13, width = componentWidth, height = componentHeigth)
buttonAdjPid = Button(root, text=u"Настроить ПИД", command=button_writePid).place(x = xMargin, y = componentHeigth*11 + yMargin * 14, width = componentWidth, height = componentHeigth)

buttonAdjKp1 = Button(root, text=u"Kp +", command=button_KpPlus).place(x = xMargin, y = componentHeigth*12 + yMargin * 15, width = componentWidthSmall, height = componentHeigth)
buttonAdjKp2 = Button(root, text=u"Kp -", command=button_KpMinus).place(x = xMargin*2 + componentWidthSmall, y = componentHeigth*12 + yMargin * 15, width = componentWidthSmall, height = componentHeigth)
buttonAdjKi1 = Button(root, text=u"Ki +", command=button_KiPlus).place(x = xMargin*4 + componentWidthSmall*2, y = componentHeigth*12 + yMargin * 15, width = componentWidthSmall, height = componentHeigth)
buttonAdjKi2 = Button(root, text=u"Ki -", command=button_KiMinus).place(x = xMargin*5 + componentWidthSmall*3, y = componentHeigth*12 + yMargin * 15, width = componentWidthSmall, height = componentHeigth)

buttonAdjAmpl1 = Button(root, text=u"Амплитуда +", command=button_AmplPlus).place(x = xMargin, y = componentHeigth*13 + yMargin * 16, width = componentWidth, height = componentHeigth)
buttonAdjAmpl2 = Button(root, text=u"Амплитуда -", command=button_AmplMinus).place(x = xMargin*2 + componentWidth, y = componentHeigth*13 + yMargin * 16, width = componentWidth, height = componentHeigth)

buttonAdjAmpl1 = Button(root, text=u"Тест", command=test_fun).place(x = xMargin, y = componentHeigth*14 + yMargin * 17, width = componentWidth, height = componentHeigth)
buttonAdjAmpl1 = Button(root, text=u"График", command=show_graph).place(x = xMargin*2 + componentWidth, y = componentHeigth*14 + yMargin * 17, width = componentWidth, height = componentHeigth)


root.after(1000, timer_fun)

root.mainloop()

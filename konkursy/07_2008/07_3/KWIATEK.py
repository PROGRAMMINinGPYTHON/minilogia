from turtle import *

global a
a  = 20

def KWIATEK():
    pass

def płatek():
    for i in range(5):
        fd(a)
        lt(72)

def jeden_kwiat():
    lt(72/2)
    for i in range(5):
        płatek()
        fd(a)
        rt(72)

def przejscie_w_ramce():
    fd(a)
    lt(72)
    fd(a)
    lt(72)
    fd(a)
    rt(36)
    fd(a)
    rt(72)
    fd(a)
    rt(72)
    rt(180)
    rt(72)
    fd(a)
    lt(72+36)
    fd(a)
def ramka_kwiatu():
    for i in range(2):
        jeden_kwiat()
        przejscie_w_ramce()
speed(0)
ramka_kwiatu()
done()

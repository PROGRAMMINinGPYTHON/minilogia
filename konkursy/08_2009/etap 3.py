from turtle import *
from math import *

a = 510 / 34
b = a*sqrt(3)

def skok(x, y):
    pos = position()
    new_x = pos[0] + x
    new_y = pos[1] + y
    setposition(new_x, new_y)

def romb():
    pd()
    fillcolor("darkgreen")
    begin_fill()
    rt(30)
    for i in range(2):
        fd(a)
        lt(60)
        fd(a)
        lt(120)
    lt(30)
    end_fill()
    pu()

def wzor():
    for i in range(3):
        romb()
        rt(120)

def bok(kierunek):
    if kierunek == "gora":
        znak = -1
    else:
        znak = 1
    lt(30)
    for i in range(6):
        romb()
        skok(-znak*1.5*a, -znak*b/2)
        rt(60)
        romb()
        skok(-znak*1.5*a, znak*b/2)
        lt(60)
    rt(30)
    skok(znak*18*a, 0)

def polowa(kierunek):
    if kierunek == "gora":
        znak = -1
    else:
        znak = 1
    bok(kierunek)
    skok(0, znak*b)
    lt(90)
    ilosc = 7
    for i in range(5):
        for j in range(ilosc):
            wzor()
            skok(-znak*3*a, 0)
        skok(znak*(ilosc*3*a + 1.5*a), znak*1.5*b)
        ilosc = ilosc + 1
    rt(90)

def srodek():
    for i in range(12):
        romb()
        skok(3*a, 0)
    skok(-36*a, 0)

def POSADZKA():
    polowa("gora")
    lt(90)
    srodek()
    skok(25.5 * a, -7.5 * b)
    lt(90)
    polowa("dol")

speed(0)

POSADZKA()


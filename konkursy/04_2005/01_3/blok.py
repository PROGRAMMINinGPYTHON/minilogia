from turtle import *
from random import *
import math

global a
a = 20
def BLOK(klatki,wys):
    ustawienie_się(klatki,wys)
    for i in range(klatki):
        klatka(wys)
        przejscie_do_klatki(wys)

def ustawienie_się(klatki,wys):
    setpos(-(klatki*3*4*a)/2,-(wys*4*a)/2)

def przejscie_do_klatki(wys):
    fd(12*a)
    rt(90)
    fd(a*4*wys)
    lt(90)

def klatka(wys):
    drzwi()
    for i in range(wys-1):
        piętro(wys)
        przejscie_do_piętra()

def piętro(ile):
    for i in range(3):
        kwadrat_z_oknem()

def przejscie_do_piętra():
    lt(90)
    fd(4*a)
    lt(90)
    fd(12*a)
    rt(180)

def drzwi():
    kwadrat_z_oknem()
    fillcolor("brown")
    begin_fill()
    pd()
    for i in range(4):
        fd(4*a)
        lt(90)
    end_fill()
    setheading(0)
    fd(a)
    fillcolor("grey")
    begin_fill()
    lt(90)
    fd(3*a)
    rt(90)
    fd(2*a)
    rt(90)
    fd(3*a)
    rt(90)
    fd(2*a)
    end_fill()
    setheading(0)
    fd(3*a)
    kwadrat_z_oknem()
    przejscie_do_piętra()


def okno():
    kolory = ["orange", "yellow", "red","blue","black","pink","green","yellowgreen","skyblue","grey","blue"]
    fillcolor(kolory[randrange(11)])
    begin_fill()
    pd()
    for i in range(4):
        fd(a+a)
        lt(90)
    end_fill()
    pu()

def kwadrat_z_oknem():
    fillcolor("brown")
    begin_fill()
    pd()
    for i in range(4):
        fd(4*a)
        lt(90)
    end_fill()
    lt(45)
    pu()
    fd(a*math.sqrt(2))
    rt(45)
    okno()
    setheading(0)
    fd(2*a)
    rt(45)
    fd(a*math.sqrt(2))
    lt(45)

speed(0)
BLOK(1,1)
setpos(0,0)
done()

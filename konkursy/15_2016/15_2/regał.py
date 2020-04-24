from turtle import *
from random import *

global a
a = 10


def reg(szerokość, ile):
    pu()
    setpos(-szerokość / 2 + a, -(ile * 7 * a) / 2 + 2 * a)
    pd()
    for i in range(ile):
        półka(szerokość)
        rt(90)
        pu()
        fd(a)
        rt(90)
        fd(a - 2)
        pd()
    pu()
    setpos(-szerokość / 2 + 2, -(ile * 7 * a) / 2)
    kwadrat()
    fd(szerokość - a + 1)
    kwadrat()
    setpos(szerokość / 2 + 3, (ile * 7 * a) / 2 + 2 * a)
    setheading(90)
    kwadrat()
    setheading(180)
    fd(szerokość - a + 3)
    rt(90)
    kwadrat()


def kwadrat():
    fillcolor("brown")
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    setheading(0)


def niebieska():
    kolor_ksiązki("blue",5*a)


def zielona():
    kolor_ksiązki("yellowgreen",4*a)

def czerwona():
    kolor_ksiązki("red",3*a)

def kolor_ksiązki(kol, wys):
    fillcolor(kol)
    begin_fill()
    for i in range(2):
        fd(a)
        lt(90)
        fd(wys)
        lt(90)
    end_fill()

def książka():
    księga = [niebieska, zielona, czerwona]
    kol = księga[randrange(3)]()


def deska(szer):
    color("brown")
    fillcolor("brown")
    begin_fill()
    fd(szer)
    lt(90)
    fd(a)
    lt(90)
    fd(szer)
    lt(90)
    fd(a)
    end_fill()
    color("black")


def półka(szer):
    if szer % 10 == 0:
        print("ok")
    else:
        pass
    for i in range(round((szer / 10) - 2)):
        książka()
        setheading(0)
        fd(a)
    rt(180)
    pu()
    fd(10 * (szer / 10) - 2)
    rt(270)
    fd(a)
    setheading(0)
    fd(a)
    pd()
    deska(szer)
    setheading(0)
    fd(a)
    lt(90)
    pu()
    deska(8 * a)
    setheading(90)
    fd(7 * a)
    rt(90)
    deska(szer - a)
    lt(90)
    fd(szer - 2 * a)
    rt(90)
    pd()
    width(2)
    deska(6 * a)
    width(1)
    fd(szer - a)


speed(0)
reg(600, 6)
setpos(0, 0)

done()

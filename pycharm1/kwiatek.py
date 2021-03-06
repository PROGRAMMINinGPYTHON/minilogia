from turtle import *
import math


def kwiatek():
    zielone()


def pieciokąt(bok, kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(5):
        fd(bok)
        lt(360 / 5)
    end_fill()


def zielone():
    pu()
    setpos(0, 0)
    pieciokąt(75, "darkgreen")
    for i in range(5):
        print(pos())
        przejscie_do_kolejnego_zielonego(i)
        pieciokąt(75, "darkgreen")
        pu()
        setpos(0, 0)
        setheading(0)
        pd()


def przejscie_do_kolejnego_zielonego(i):
    pu()
    for i in range(1 + i):
        fd(75)
        lt(360 / 5)
    fd(25)
    rt(180)
    for i in range(2):
        lt(360 / 5)
        fd(25)
    fd(25)
    for i in range(2):
        rt(360 / 5)
        fd(25)
    rt(180)
    fd(50)
    rt(180)
    pd()


def zolte_kolo():
    for j in range(10):
        pieciokąt(25, "yellow")
        fd(25)
        lt(360 / 5)
        fd(25)
        rt(360 / 5)
        rt(36)


def piec_zoltych_kol():
    setheading(0)
  #  zolte_kolo()
    for j in range(5):
        przejscie_do_kolejnego_zoltego_kola()
        zolte_kolo()


def przejscie_do_kolejnego_zoltego_kola():
    fd(25)
    lt(360 / 5)
    fd(75)
    rt(180)
    fd(25)
    rt(180)


speed(0)
setpos(50, 0)
piec_zoltych_kol()
zielone()
done()

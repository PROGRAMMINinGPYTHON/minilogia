from turtle import *
import math


def PIRAMIDA(ile):
    a = 600 / (ile * 9 + ile - 1)
    pu()
    setpos(-300 + 2 * a, -100)
    pd()
    for i in range(ile):
        piętro(a, ile - i)
        przejscie_do_nowego_rządku(a, ile - i)


def piętro(a, ile_teraz):
    for i in range(ile_teraz):
        kwadrat(a)
        przejscie_w_rządku(a)


def kwadrat(a):
    fillcolor("orange")
    begin_fill()
    setheading(0)
    for i in range(4):
        fd(2 * a)
        rt(90)
        fd(a)
        rt(90)
        fd(a)
        lt(135)
        fd(a * math.sqrt(2))
        lt(45)
        fd(a)
        lt(45)
        fd(a * math.sqrt(2))
        lt(135)
        fd(a)
        rt(90)
        fd(a)
        rt(90)
        fd(2 * a)
        lt(90)
    end_fill()


def przejscie_w_rządku(a):
    pu()
    fd(10 * a)
    pd()


def przejscie_do_nowego_rządku(a, ile_teraz):
    pu()
    setheading(180)
    fd(10 * a * ile_teraz)
    rt(90)
    fd(5 * a)
    rt(90)
    fd(5 * a)
    pd()


speed(0)
PIRAMIDA(5)
setpos(0, 0)
done()

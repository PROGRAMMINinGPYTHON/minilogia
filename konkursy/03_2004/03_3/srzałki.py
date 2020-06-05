from turtle import *
import math

szerokosc_obrazka = 200
def jedna_strzałka(ile):

    b = szerokosc_obrazka / ile + 1 / 2
    a = b / math.sqrt(2)
    color("yellowgreen")
    fillcolor("yellowgreen")
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    biała_strałka(ile)


def biała_strałka(ile):
    b = szerokosc_obrazka / ile + 1 / 2
    a = b / math.sqrt(2)
    color("yellowgreen")
    fillcolor("white")
    begin_fill()
    fd(a)
    lt(135)
    fd(b / 4)
    rt(90)
    fd(b / 4)
    lt(90)
    fd(b / 2)
    lt(90)
    fd(b / 4)
    rt(90)
    fd(b / 4)
    lt(135)
    fd(a)
    end_fill()


def przejscie_w_rządku(ile, i):
    b = szerokosc_obrazka / ile + 1 / 2
    a = b / math.sqrt(2)
    pu()
    fd(a)
    lt(90)
    fd(a)
    lt(90)
    if i == 1:
        fd(2 * a)
        lt(90)
        fd(2 * a)
        lt(90)
    if i == 2:
        lt(90)
        fd(a)
        rt(180)
        fd(a)
        lt(90)


def rządek(ile):
    b = szerokosc_obrazka / ile + 1 / 2
    a = b / math.sqrt(2)
    for i in range(4):
        pd()
        jedna_strzałka(ile)
        przejscie_w_rządku(ile, i)


def przejscie(ile, i):
    b = szerokosc_obrazka / ile + 1 / 2
    a = b / math.sqrt(2)
    if i == 0:
        print("dd")
    if i == 1:
        fd(2 * a)


def cały_kwadrat(ile):
    b = szerokosc_obrazka / ile + 1 / 2
    a = b / math.sqrt(2)
    for i in range(4):
        rządek(ile)
        przejscie(ile, i)


def przejscie_pomiędzy_kwadratami(ile):
    b = szerokosc_obrazka / ile + 1 / 2
    a = b / math.sqrt(2)
    setheading(-90)
    pu()
    fd(1 * b)
    lt(90)
    setheading(0)
    fd(1 * b)
    lt(45)


def STRZAŁKI(ile):
    pu()
    setpos(-szerokosc_obrazka, 0)
    pd()
    setheading(45)
    b = szerokosc_obrazka / ile + 1 / 2
    a = b / math.sqrt(2)
    for i in range(ile):
        cały_kwadrat(ile)
        przejscie_pomiędzy_kwadratami(ile)


speed(0)
STRZAŁKI(1)
pu()
setpos(0,0)
pd()
done()

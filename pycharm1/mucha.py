from turtle import *
import math

global a
a = 25


def muszka(ile):
    lewa_str(ile)


def lewa_str(ile):
    for i in range(ile):
        kształt(2 + i * 2)
        rt(90)
        fd(a * math.sqrt(2))


def prawa_str():
    pass


def kształt(ile):
    for j in range(2):
        for i in range(ile):
            pd()
            diament()
            pu()
            rt(180)
            fd(a)
            rt(90)
            fd(a)
        rt(180)
        fd(a)
        rt(180)
        for i in range(ile + 1):
            pd()
            kwadrat()
            pu()
            rt(135)
            fd(a * math.sqrt(2))
            lt(135)
        setheading(-90)
        fd(a * math.sqrt(2))
        lt(45)
        fd(a)
        lt(45)
        fd(a)
        rt(180)


def diament():
    fillcolor("skyblue")
    begin_fill()
    setheading(180)
    fd(a)
    lt(45)
    fd(a)
    lt(90)
    fd(a)
    lt(45)
    fd(a)
    lt(45)
    fd(a)
    lt(90)
    fd(a)
    end_fill()


def kwadrat():
    fillcolor("orange")
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()

def prawa_str():
    pass

def prawy_diament():
    pass

def kształt_dwa():
    pass


pu()
setpos(0,0)
speed(0)
setheaidng(0)
kształt(2)
done()
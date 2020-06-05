from turtle import *
import math
def SZAROTKI():
    Szarotka(120)
    przejscie_do_drugiej_szrotki(120)
    Szarotka(120)
    przejscie_do_trzeciej_szarotki(120)
    Szarotka(120)
    wykonczenia(120)

def wykonczenia(a):
    setheading(30)
    fd(a/3)
    lt(120)
    color("white")
    fd(a/3)

def przejscie_do_drugiej_szrotki(a):
    setheading(30)
    pu()
    fd(a)
    rt(60)
    fd(a/3)
    for i in range(3):
        lt(60)
        fd(a/3)
    rt(60)
    fd(a)

def przejscie_do_trzeciej_szarotki(a):
    setheading(120)
    pu()
    rt(180-30)
    fd(2*a)
    rt(120)
    fd(2*a/3)
    for i in range(2):
        lt(60)
        fd(a/3)
        pd()
    rt(120)
    fd(a/3)
    rt(180)

def Szarotka(a):
    sześciokąt(a)
    pu()
    rt(120)
    fd(a/2)
    lt(45)
    sześciokąt(a / 2)
    lt(60)
    pu()
    fd(a/2)
    pd()

def sześciokąt(a):
    for i in range(6):
        trójkąt(a, 60 * i)


def trójkąt(a, kąt):
    setheading(30 - (kąt))
    color("purple")
    pd()
    fd(a / 3)
    lt(60)
    fd(a / 3)
    rt(120)
    fd(a / 3)
    lt(60)
    fd(a / 3)
    rt(120)
    pu()
    fd(a)
    pd()
    rt(120)
    pu()
    fd(a)
    pd()
    rt(120)
    fillcolor("purple")
    begin_fill()
    fd(a / 3)
    rt(90)
    fd(a / 3)
    rt(135)
    fd((a / 3) * math.sqrt(2))
    end_fill()
    rt(135)
    pu()
    fd(a)
    pd()
    fillcolor("purple")
    begin_fill()
    rt(135)
    fd((a / 3) * math.sqrt(2))
    rt(135)
    fd(a / 3)
    rt(90)
    fd(a / 3)
    end_fill()


speed(0)
SZAROTKI()

done()

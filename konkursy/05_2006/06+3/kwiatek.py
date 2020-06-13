from turtle import *
from random import *

def KWIATEK():
    srodek_kwiatka()
    for i in range(6):
        pu()
        setpos(0, 0)
        pd()
        setheading(120)
        for j in range(i):
            fd(56)
            rt(60)
        gałązka()
    pu()
    setpos(56,0)
    pd()
    wykonczenie()

def gałązka():
    numery = [1,2,3,4,5,6,7,8]
    color("black")
    for i in range(numery[randrange(8)]):
        trójkąt(56-(7*i))
        przejscie(56-(7*i))

def sześciokąt(a,kolor,pen_color):
    color(pen_color)
    fillcolor(kolor)
    begin_fill()
    for i in range(6):
        fd(a)
        lt(60)
    end_fill()

def srodek_kwiatka():
    sześciokąt(56,"darkgreen","red")
    fd(56/3)
    for i in range(6):
        sześciokąt(56/3,"yellowgreen","black")
        fd(56/3)
        lt(60)
        fd(56/3)
        rt(60)
        fd(56/3)
        lt(60)
    lt(120)
    fd(56/3)
    rt(120/2)
    fd(56/3)
    rt(60)
    sześciokąt(56/3,"yellow","black")
    rt(120)
    fd(56/3)
    rt(60)
    fd(56/3)
    lt(120)
    fd(56/3)
    rt(180)

def wykonczenie():
    width(2)
    for i in range(6):
        color("red")
        fd(56)
        rt(60)

def trójkąt(a):
    fillcolor("darkgreen")
    begin_fill()
    for i in range(3):
        fd(a)
        lt(120)
    end_fill()

def przejscie(a):
    pu()
    fd(a)
    lt(120)
    fd(a)
    lt(60)
    fd((a/2)-3.5)
    rt(180)
    pd()


speed(0)
KWIATEK()
done()
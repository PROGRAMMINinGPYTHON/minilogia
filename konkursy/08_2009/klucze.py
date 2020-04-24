from turtle import *
global a
a = 25
def KLUCZE():
    pu()
    setpos(0,0)
    pd()
    polowa()
    druga_polowa()

def klucz():
    width(2)
    color("orange")
    fillcolor("yellowgreen")
    begin_fill()
    fd(8*a)
    for i in range(2):
        lt(90)
        fd(4*a)
    lt(90)
    fd(3*a)
    lt(90)
    fd(a)
    lt(90)
    for i in range(2):
        fd(2*a)
        rt(90)
    fd(2*a)
    rt(90)
    fd(7*a)
    lt(90)
    fd(a)
    end_fill()

def polowa():
    setheading(-135)
    for i in range(3):
        klucz()
        lt(90)
        fd(4*a)
        rt(90)

def druga_polowa():
    pu()
    setpos(0,0)
    pd()
    setheading(45)
    for i in range(3):
        klucz()
        lt(90)
        fd(4*a)
        rt(90)
speed(0)
KLUCZE()

pu()
color("black")
setpos(-200,-200)
setheading(0)
pd()
fd(400)
pu()
setpos(-225,-225)
pd()
setheading(0)
fd(450)

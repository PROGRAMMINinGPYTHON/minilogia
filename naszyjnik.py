from turtle import *

def NASZYJNIK(ile):
    pass
def kuleczki(x,kol):
    fillcolor(kol)
    begin_fill()
    circle(x/2)
    end_fill()

def kkulki(ile):
    for i in range(ile):
        kula()
        setheading(0)
        rt(360/12)
        fd(40)
        rt(90)
        fd(20)
        lt(90)

def kula():
    kuleczki(40,"darkblue")
    lt(90)
    pu()
    fd(40)
    pd()
    fd(40)
    rt(90)
    pd()
    kuleczki(30,"skyblue")
    rt(90)
    pu()
    fd(60)

    
speed(0)
kkulki(2)

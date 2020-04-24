from turtle import *
import math
def ZAMEK(n):
    pass


def kształt(n):
    a = 760/((n*2))
    pu()
    fillcolor("grey")
    begin_fill()
    pu()
    setpos(-760/2,-300)
    pd()
    setpos(760/2,-300)
    setheading(90)
    fd(4*a)
    lt(90)
    fd(a)
    lt(90)
    fd(a)
    rt(90)
    fd(a)
    rt(90)
    fd(a)
    lt(90)
    fd(a)
    lt(90)
    fd(a)
    rt(90)
    fd((((n*2)*a)/2))
    rt(90)
    fd(a)
    lt(90)
    fd(a)
    lt(90)
    fd(4*a)
    end_fill()

def okienka(n):
    a = 760/((n*2)+1)
    pu()
    setpos(-760/2,-300)
    pd()
    setheading(90)
    fd(a)
    pu()
    rt(90)
    fd(a)
    for i in range(n):
        pd()
        fillcolor("skyblue")
        begin_fill()
        for j in range(4):
            fd(a)
            lt(90)
        end_fill()
        setheading(45)
        fd(a*math.sqrt(2))
        lt(135)
        fd(a)
        lt(135)
        fd(a*math.sqrt(2))
        lt(45)
        pu()
        fd(a)
        




kształt(7)
okienka(7)

from turtle import *
import math
global a
a = 380/19
def MOTYW():
    pass
def klocek(kol):
    fillcolor(kol)
    begin_fill()
    fd(2*a)
    lt(90)
    fd(a)
    lt(90)
    fd(2*a)
    lt(90)
    fd(a)
    end_fill()
    lt(90)
    fd(2*a)
    
def rządek(kol,ile):
    for i in range(ile):
        klocek(kol)
    pu()
    fd(a)
    lt(90)
    pd()

def srodek():
    pu()
    setpos(0,0)
    setheading(90)
    fd(1.5*a)
    pd()
    rt(90)
    fillcolor("yellow")
    begin_fill()
    fd(1.5*a)
    rt(90)
    fd(3*a)
    rt(90)
    fd(3*a)
    rt(90)
    fd(3*a)
    rt(90)
    fd(1.5*a)
    end_fill()
    
def kwadrat(kol,jak_d):
    for i in range(4):
        rządek(kol,jak_d)
    rt(180)
#    fd(a)

def kwadraty(x):
    pu()
    setpos(-2.5*a,-2.5*a)
    pd()
    setheading(0)
    for i in range(8):
        if i%2 == 0:
            x = "green"
        else:
            x = "yellow"
        kwadrat(x,2+i)
        pu()
        lt(45)
        fd(a*math.sqrt(2))
        setheading(0)
        pd()
        




















speed(0)
srodek()
kwadraty(2)

from turtle import *
import math
def kafelek(ile):
    a = 450/ile/5
    setheading(0)
    fillcolor("brown")
    begin_fill()
    fd(3*a)
    lt(45)
    fd(a*math.sqrt(2))
    lt(45)
    fd(3*a)
    lt(45)
    fd(a*math.sqrt(2))
    lt(45)
    fd(3*a)
    lt(45)
    fd(a*math.sqrt(2))
    lt(45)
    fd(3*a)
    lt(45)
    fd(a*math.sqrt(2))
    end_fill()

def rząd(ile):
    a = 450/ile/5
    pu()
    setpos(-450/2,-450/2)
    pd()
    for j in range(ile):
        pu()
        setpos(-450/2,-450/2+5*a*j)
        pd()
        for i in range(ile):
            kafelek(ile)
            lt(45)
            fd(3*a)
            lt(45)
            fd(a*math.sqrt(2))
            rt(90)
            pu()
            fd(a*math.sqrt(2))
            lt(45)
            pd()
            
def zolty_kwadrat(ile):
    a = 450/ile/5
    fillcolor("yellow")
    begin_fill()
    pu()
    setpos(-225+a,-225+a)
    setheading(0)
    pd()
    fd((450-a)-2.5*a)
    lt(90)
    fd((450-a)-2.5*a)
    lt(90)
    fd((450-a)-2*a)
    lt(90)
    fd((450-a)-2.5*a)
    end_fill()

def posadzka(ile):
    zolty_kwadrat(ile)
    rząd(ile)
speed(0)
posadzka(20)

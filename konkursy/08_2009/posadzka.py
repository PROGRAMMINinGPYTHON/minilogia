from turtle import *
a = 450/4
import math
def POSADZKA(ile):
    kwadrat_big()
    zielone_trojkąty()
    plansza(ile)

def kwadrat_big():
    pu()
    setpos(-225,-225)
    pd()
    fillcolor("yellow")
    begin_fill()
    setheading(0)
    for i in range(4):
        fd(450)
        lt(90)
    end_fill()

def mini_kwadrat(ile):
    a =(450/2*math.sqrt(2))/ile
    setheading(-45)
    fillcolor("green")
    begin_fill()
    fd(a)
    lt(135)
    fd(a*math.sqrt(2))
    lt(135)
    fd(a)
    end_fill()
    setheading(45)
    fd(a)
    rt(90)
    fillcolor("yellow")
    begin_fill()
    fd(a)
    rt(90)
    fd(a)
    rt(135)
    fd(a*math.sqrt(2))
    end_fill()
    
def plansza(ile):
    a = (450/2*math.sqrt(2))/ile
    pu()
    setpos(-225,0)
    pd()
    for j in range(ile):
        pu()
        setpos(-225,0)
        pd()
        setheading(45)
        fd(a*j)
        rt(90)
        for i in range(ile):
            mini_kwadrat(ile)
            setheading(-45)
            rt(90)
            fd(a)
            lt(90)
            pu()
            fd(a)
            pd()

def zielone_trojkąty():
    setpos(-225,-225)
    setheading(45)
    for i in range(4):
        trojkąt()
        lt(180)
        fd(450)
        rt(135)
        
        
def trojkąt():
    fillcolor("green")
    begin_fill()
    fd(450/2*(math.sqrt(2)))
    lt(135)
    fd(450/2)
    lt(90)
    fd(450/2)
    end_fill()
speed(0)
POSADZKA(5)

from turtle import *
import math
    
def kafelek(ile):
    a = 300/ile/10
    dol_kafelka(ile)
    pu()
    lt(90)
    fd(4*a)
    lt(90)
    fd(4*a)
    gora_kafelka(ile)
    rt(90)
    pu()
    fd(4*a)
    lt(90)
    fd(4*a)
    pd()
    
def xxx(ile):
    a =300/ile/10
    fillcolor("yellow")
    begin_fill()
    pd()
    color("yellow")
    setheading(0)
    for i in range(4):
        fd(a)
        lt(45)
        fd(a*math.sqrt(2))
        rt(90)
        fd(a*math.sqrt(2))
        lt(45)
        fd(a)
        lt(90)
    end_fill()

def star(ile):
    a = 300/ile/10
    fillcolor("blue")
    begin_fill()
    color("blue")
    setheading(0)
    for i in range(4):
        fd(a)
        rt(45)
        fd(a*math.sqrt(2))
        lt(90)
        fd(a*math.sqrt(2))
        rt(45)
        fd(a)
        lt(90)
    end_fill()

def dol_kafelka(ile):
    a = 300/ile/10
    star(ile)
    setheading(0)
    pu()
    fd(4*a)
    xxx(ile)

def gora_kafelka(ile):
    a = 300/ile/10
    xxx(ile)
    pu()
    setheading(0)
    fd(4*a)
    pd()
    star(ile)

    
speed(0)
kafelek(5)

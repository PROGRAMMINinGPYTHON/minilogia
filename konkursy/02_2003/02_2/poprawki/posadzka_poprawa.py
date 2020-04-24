from turtle import *
import math
def POSADZKA(n):
    pass

def star(n):
    a = (300/n)/10
    color("blue")
    fillcolor("blue")
    begin_fill()
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

def XXX(n):
    a = (300/10)/n
    color("yellow")
    fillcolor("yellow")
    begin_fill()
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

def kafelek(n):
    a =(300/n)/10
    star(n)
    pu()
    setheading(0)
    fd(4*a)
    pd()
    XXX(n)
    setheading(90)
    pu()
    fd(4*a)
    pd()
    star(n)
    setheading(180)
    fd(4*a)
    XXX(n)
    pu()
    setheading(-90)
    fd(4*a)
    pd()
    setheading(0)

def podłoga(n):
    a = (300/n)/10
    pu()
    setpos(-n*4*a-a,-n*4*a-a)
    pd()
    color("red")
    begin_fill()
    setheading(90)
    fd(8*n*a+2*a)
    rt(90)
    fd(8*n*a+2*a)
    rt(90)
    fd(8*n*a+2*a)
    rt(90)
    fd(8*n*a+2*a)
    rt(90)
    end_fill()
    pu()
    setpos(-n*4*a,-n*4*a)
    for i in range(n):
        for j in range(n):
            kafelek(n)
            pu()
            fd(8*a)
            pd()
        pu()
        setheading(180)
        fd(8*a*n)
        setheading(90)
        fd(8*a)
speed(0)
podłoga(4)

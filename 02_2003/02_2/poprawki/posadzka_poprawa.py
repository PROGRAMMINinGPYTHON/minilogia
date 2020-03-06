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
    
speed(0)
kafelek(4)

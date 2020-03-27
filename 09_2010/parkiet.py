from turtle import *
import math
def PARKIET():
    for i in range(4):
        pass

def deska():
    a = 460/4/7
    fillcolor("darkgreen")
    begin_fill()
    fd(a)
    lt(90)
    fd(6*a)
    lt(90)
    fd(a)
    lt(90)
    fd(6*a)
    end_fill()

def kwadrat():
    a = 460/4/7
    b = 5*a-(2*(a*math.sqrt(2)))
    setheading(0)
    for i in range(4):
        deska()
        rt(180)
        fd(7*a)
        rt(180)
    fd(a)
    lt(90)
    fd(a)
    rt(90)
    fillcolor("orange")
    begin_fill()
    for i in range(4):
        fd(5*a)
        lt(90)
    end_fill()
    setheading(0)
    fillcolor("yellow")
    begin_fill()
    fd(a*math.sqrt(2))
    lt(45)
    fd((5*a*math.sqrt(2)-4*a)/2)
    lt(90)
    fd(a)
    lt(90)
    fd(((5*a*math.sqrt(2)-4*a)/2)+a)
    end_fill()
    begin_fill()
    rt(135)
    fd(a)
    rt(45)
    fd(((5*a*math.sqrt(2)-4*a)/2)+a)
    rt(90)
    fd(a)
    rt(90)
    fd(((5*a*math.sqrt(2)-4*a)/2)+2*a)
    end_fill()
    setpos(0,0)
speed(0)
kwadrat()

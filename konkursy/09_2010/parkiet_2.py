from turtle import *
import math
global a
a = 460/4/7
def PARKIET():
    pass

def kwadrat():
    pass

def deska():
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
    lt(90)
    fd(a)
    lt(90)
    fd(6*a)
    rt(90)
    
def ramka():
    for i in range(4):
        deska()
        rt(90)
    fd(a)
    fillcolor("orange")
    begin_fill()
    setheading(0)
    fd(5*a)
    lt(90)
    fd(5*a)
    lt(90)
    fd(5*a)
    lt(90)
    fd(5*a)
    end_fill()
    żółty_X()

    
ramka()

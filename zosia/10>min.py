from turtle import *
import math
global a
a = 26
def lisc(kol):
    fillcolor(kol)
    begin_fill()
    fd(a)
    rt(45)
    fd(a*math.sqrt(2))
    rt(135)
    fd(2*a)
    rt(90)
    fd(a)
    end_fill()

def glowa():
    setheading(90)
    for i in range(2):
        lisc("yellowgreen")
        lisc("orange")


def trzy(ile):
    for i in range(ile):
        setheading(90)
        fd(4*a)
        glowa()
        setheading(-90)
        fd(4*a)
        lt(90)
        fd(2*a)
        lt(90)
        fd(9*a)
        glowa()
        setheading(-90)
        fd(9*a)
        lt(90)
        fd(2*a)
        lt(90)
        fd(4*a)
        glowa()
        setheading(-90)
        fd(4*a)
        setheading(90)

def wiatraki(ile):
    trzy(ile)
speed(0)
wiatraki(5)
done()
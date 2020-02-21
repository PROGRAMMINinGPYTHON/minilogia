from turtle import *
import math
global a
a = 400/5
def POSADZKA():
    pass

def zolty():
    pass

def blue():
    setheading(0)
    color("black")
    fillcolor("skyblue")
    pd()
    begin_fill()
    fd(a)
    lt(90)
    fd(a)
    lt(90)
    fd(a)
    lt(90)
    fd(a)
    end_fill()
    setheading(0)
    lt(45)
    pu()
    fd(a/8*math.sqrt(2))
    pd()
    setheading(0)
    for j in range(3):
        setheading(0)
        for i in range(4):
            fd(a-a/(4*j+1))
            lt(90)


blue()

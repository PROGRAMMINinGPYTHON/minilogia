from turtle import *
import math
global a
a = 20
global b
b = a/2

def KOLUMNY():
    słupy()
    wykonczenie()
    podłoga_()
    dach()


def podstawa():
    pd()
    setheading(0)
    fd(42*10)
    lt(90)
    fd(a)
    lt(90)
    fd(42*10)
    lt(90)
    fd(a)
    
def podłoga_():
    pu()
    setpos(-21*10,-240)
    podstawa()
    pu()
    setpos(-21*10,80)
    podstawa()
def wykonczenie():
    pu()
    setpos(-21*10,80)
    pd()
    setheading(0)
    fd(20)
    for i in range(3):
        pd()
        rt(90)
        fd(a/2)
        lt(90)
        fd(a/2)
        rt(90)
        fd(a/2)
        lt(90)
        fd(4*a)
        lt(90)
        fd(a/2)
        rt(90)
        fd(a/2)
        lt(90)
        fd(a/2)
        rt(180)
        fd(a/2)
        rt(90)
        fd(5*a)
        rt(180)
        fd(5*a)
        lt(90)
        fd(a/2)
        rt(90)
        pu()
        fd(40)

        
    
def dach():
    pu()
    setpos(-21*10,80)
    setheading(90)
    fd(20)
    rt(45)
    pd()
    fd(42*10/2*math.sqrt(2))
    rt(90)
    fd(42*10/2*math.sqrt(2))

def słupy():
    pu()
    setpos(-19*10,-220)
    pd()
    for i in range(3):
        setheading(90)
        fd(a/2)
        rt(90)
        fd(a/2)
        lt(90)
        fd(a/2)
        rt(90)
        fd(4*a)
        rt(90)
        fd(a/2)
        lt(90)
        fd(a/2)
        rt(90)
        fd(a/2)
        rt(180)
        fd(a/2)
        lt(90)
        fd(5*a)
        setheading(45)
        pu()
        fd(a/2*math.sqrt(2))
        rt(45)
        fd(a/2)
        for i in range(7):
            pd()
            setheading(90)
            fd(13*a)
            rt(180)
            fd(13*a)
            lt(90)
            fd(a/2)
        pu()
        rt(90)
        fd(a/2)
        lt(90)
        fd(a/2)
        rt(90)
        fd(a/2)
        lt(90)
        fd(2*a)
        pd()
        
speed(0)
KOLUMNY()


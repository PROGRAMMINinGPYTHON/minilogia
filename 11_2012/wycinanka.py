from turtle import *
import math
def WYCINANKA(ile):
    a = 480/(ile+(ile-1))/5
    for i in range(ile):
        pu()
        setpos(1.5*a+(5*a*i+1),-480/2+(5*a*i+1))
        pd()
        rządek(ile)
    

def wzorek(ile):
    a = 480/(ile+(ile-1))/5
    fillcolor("darkgreen")
    begin_fill()
    for i in range(4):
        fd(2*a*math.sqrt(2))
        lt(90)
        fd(a*math.sqrt(2))
        lt(45)
        for i in range(3):
            fd(a)
            rt(90)
        lt(135)
        fd(a*math.sqrt(2))
        lt(90)
    end_fill()

def rządek(ile):
    a = 480/(ile+(ile-1))/5
    for i in range(ile):
        setheading(45)
        wzorek(ile)
        pu()
        lt(135)
        fd(3*a)
        rt(45)
        fd(2*a*math.sqrt(2))
        rt(45)
        fd(3*a)
        rt(45)
        pd()

speed(0)
WYCINANKA(4)

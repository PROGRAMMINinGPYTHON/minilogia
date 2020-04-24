from turtle import *
import math
global a
a = 50

global b
b = a*math.sqrt(2)
def GWIAZDKI():
    pass
a = 50
def pięciokąt(x):
    for i in range(5):
        fillcolor("grey")
        begin_fill()
        pd()
        setheading(99+x+(90-18)*i)
        fd(a)
        rt(135)
        fd(a*math.sqrt(2))
        rt(135)
        fd(a)
        end_fill()
    for i in range(5):
        pd()
        setheading(99+x+(90-18)*i)
        fd(a)
        rt(135)
        fd(a*math.sqrt(2))
        rt(135)
        fd(a)

def większość():
    pu()
    setpos(0,0)
    pd()
    pięciokąt(0)
    for i in range(5):
        pu()
        setpos(0,0)
        pd()
        setheading(81+(90-18)*i)
        fd(a)
        lt(18)
        fd(a)
        pięciokąt(180)
speed(0)   
większość()

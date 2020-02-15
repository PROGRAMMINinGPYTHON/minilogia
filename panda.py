from turtle import *
global a
a = 10
def głowa ():
    for i in range(12):
        fd(80)
        rt(30)
    rt(180)
    lt(30)
    fd(8*a)
    lt(30)
    fd(70)
    rt(60)
    fillcolor("black")
    begin_fill()
    for i in range(6):
        fd(4*a)
        rt(60)
    end_fill()
    setheading(60)
    fd(6*a)
    rt(30)
    fd(8*a)
    rt(30)
    fd(8*a)
    rt(30)
    fd(8*a)
    rt(30)
    fd(7*a)
    fillcolor("black")
    begin_fill()
    lt(60)
    for i in range(6):
        fd(6*a)
        lt(60)
    end_fill()
    rt(60)
    fd(2*a)

def oczy():
    setheading(180)
    pu()
    fd(4*a)
    pd()
    rt(60)
    fillcolor("black")
    begin_fill()
    for i in range(6):
        fd(4*a)
        lt(60)
    end_fill()


    
speed(0)



głowa()
oczy()

















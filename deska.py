from turtle import *
global a
a = 700/19
def PŁOT(n):
    deski(n)
    xxx(n)

def deski(n):
    wys = a*n*2
    pu()
    setpos(-700/2,-wys/2)
    setheading(180)
    fd(5*a)
    for i in range(15):
        pd()
        setheading(0)
        fillcolor("yellow")
        begin_fill()
        fd(a)
        lt(90)
        fd(wys+1*a)
        lt(90)
        fd(a)
        lt(90)
        fd(wys+1*a)
        end_fill()
        rt(180)
        fd(wys+1*a)
        fillcolor("green")
        begin_fill()
        rt(90)
        fd(a)
        lt(120)
        fd(a)
        lt(120)
        fd(a)
        end_fill()
        lt(30)
        fd(wys+1*a)
        lt(90)
        pu()
        fd(2*a)

def kwadrat():
    setheading(0)
    pd()
    fillcolor("green")
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()

def laczenie(n):
    wys = a*2*n
    for i in range(n):
        kwadrat()
        lt(90)
        fd(2*a)
        
def xxx(n):
    wys = a*2*n
    setpos(-350+1*a,-(wys/2)+1*a)
    setheading(180)
    fd(5*a)
    for i in range(14):
        laczenie(n)
        rt(180)
        pu()
        fd(n*2*a+1*a)
        lt(90)
        fd(2*a)
        lt(90)
        fd(a)
        pd()
        
    
speed(0)        
PŁOT(7)



from turtle import *

def buzia():
    setheading(0)
    pd()
    fillcolor("white")
    begin_fill()
    circle(12)
    end_fill()
    pu()
    setheading(90)
    fd(4.5*3)
    rt(90)
    fd(1.5*3)
    fillcolor("black")
    begin_fill()
    circle(3)
    end_fill()
    pu()
    rt(180)
    fd(3*3)
    rt(180)
    fillcolor("black")
    begin_fill()
    circle(3)
    end_fill()
    setheading(-90)
    pu()
    fd(3.5*3)
    lt(90)
    fd(1.5*3)
    pd()
        
    
def zielona():
    setheading(0)
    fillcolor("yellowgreen")
    begin_fill()
    fd(30)
    lt(90)
    fd(30)
    lt(90)
    fd(30)
    lt(90)
    fd(30)
    end_fill()
    lt(90)
    pu()
    fd(15)
    lt(90)
    fd(3)
    buzia()
    setheading(0)
    circle(6,90)
    setheading(90)
    pu()
    circle(2*3,180)
    pd()
    circle(2*3,90)
    
def czerwona():
    setheading(0)
    fillcolor("red")
    begin_fill()
    fd(30)
    lt(90)
    fd(30)
    lt(90)
    fd(30)
    lt(90)
    fd(30)
    end_fill()
    pu()
    setheading(0)
    fd(15)
    lt(90)
    fd(3)
    buzia()
    circle(3)
def zolta():
    setheading(0)
    fillcolor("yellow")
    begin_fill()
    fd(30)
    lt(90)
    fd(30)
    lt(90)
    fd(30)
    lt(90)
    fd(30)
    lt(90)
    end_fill()
    fd(15)
    pu()
    lt(90)
    fd(3)
    buzia()
    setheading(90)
    pu()
    fd(3)
    rt(90)
    pd()
    fd(6)
    rt(180)
    fd(12)
    rt(180)
    fd(6)

    
def schodek(n):
    for i in range(0,n):
        if i == 0:
            zielona()
        if i == 2:
            zolta()
        if i == n-1:
            czerwona()
        pu()
        rt(90)
        fd(6)
        rt(90)
        fd(15)
        lt(90)
        fd(30)
        pd()
            



def PIRAMIDA(n):
    pass
speed(0)
schodek(3)

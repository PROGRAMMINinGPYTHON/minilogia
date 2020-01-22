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

def kwadrat(kol):
    setheading(0)
    fillcolor(kol)
    begin_fill()
    fd(30)
    lt(90)
    fd(30)
    lt(90)
    fd(30)
    lt(90)
    fd(30)
    end_fill()
def zielona():
    kwadrat("green")
    setheading(0)
    fd(15)
    pu()
    lt(90)
    fd(3)
    rt(90)
    buzia()
    pu()
    circle(6,270)
    pd()
    circle(6,180)
    pu()
    circle(6,270)
    rt(90)
    fd(6)
    
def zolta():
    kwadrat("yellow")
    setheading(0)
    fd(15)
    lt(90)
    pu()
    fd(3)
    pd()
    buzia()
    lt(90)
    pu()
    fd(3)
    pd()
    rt(90)
    fd(6)
    rt(180)
    fd(12)
    rt(180)
    fd(6)
    pu()
    rt(90)
    fd(9)

def czerwony():
    kwadrat("red")
    setheading(0)
    fd(15)
    pu()
    lt(90)
    fd(3)
    buzia()
    circle(3)

def schodek(n):
    for i in range(n):

        if i == 1:
            zielona()
        if i == n:
            zolty()
        if i<1>n:
            czerwony()
        setheading(-180)
        fd(15)
        lt(90)
        fd(30)
        print("a")








    
schodek(1)

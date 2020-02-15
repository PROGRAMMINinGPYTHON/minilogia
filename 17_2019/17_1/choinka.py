from turtle import *
global a
a = 200
global b
b = 50
def ozdoba():
    fillcolor("red")
    begin_fill()
    fd(15)
    rt(90)
    fd(15)
    rt(90)
    fd(15)
    rt(90)
    fd(15)
    end_fill()

def trójkąt():
    fillcolor("darkgreen")
    color("darkgreen")
    begin_fill()
    setheading(0)
    fd(a/2)
    lt(120)
    fd(a)
    lt(120)
    fd(a)
    lt(120)
    fd(a)
    end_fill()
    rt(180)
    pu()
    fd(a+40)
    setheading(0)
    for i in range(6):
        setheading(0)
        fd(40)
        setheading(-45)
        ozdoba()

    setheading(0)
        
def choinka():
    pu()
    setpos(0,-260)
    pd()
    setheading(0)
    fillcolor("saddlebrown")
    begin_fill()
    fd(b/2)
    lt(120)
    fd(b)
    lt(120)
    fd(b)
    lt(120)
    fd(b)
    end_fill()
    setheading(120)
    fd(b)
    for i in range(3):
        trójkąt()
        pu()
        lt(120)
        fd(a)
        pd()

speed(0)
choinka()

from turtle import *
global a
a = 50
def MASKA():
    pu()
    setpos(-200,200)
    setheading(0)
    pd()
    fillcolor("black")
    begin_fill()
    fd(8*a)
    rt(90)
    fd(8*a)
    rt(90)
    fd(8*a)
    rt(90)
    fd(8*a)
    end_fill()

MASKA()
    

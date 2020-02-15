from turtle import *
from random import *

def skok(x, y):
    pu()
    fd(x)
    lt(90)
    fd(y)
    rt(90)

def trojkat():
    pd()
    kolory = ["orange", "yellow", "red"]
    color(kolory[randrange(3)])
    begin_fill()
    lt(30)
    fd(100)
    rt(120)
    fd(100)
    rt(120)
    fd(100)
    rt(150)
    end_fill()
    pu()
    

def kwiatek():
    skok(0, -100)
    color("yellow")

    begin_fill()
    pd()
    circle(100)
    pu()
    end_fill()

    skok(0,100)
    for i in range(12):
        fd(100)
        trojkat()   
        fd(-100)
        rt(30)
    


def kwiatki():
    skok(-200,0)
    kwiatek()
    skok(400,0)
    kwiatek()

kwiatki()














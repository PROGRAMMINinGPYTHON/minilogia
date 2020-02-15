from turtle import *
from random import *
setheading(90)
def trujkat(kolor):
    pd()
    rt(30)
    fd(100)
    lt(120)
    fd(100)
    lt(120)
    fd(100)
    rt(30)
    pu()
    fd(100)
    lt(180)
    rt(30)
    fd(100)
    lt(30)
    rt(30)

def kolo():
    setpos(-100,-100)
    pd()
    begin_fill()
    color("black", "blue")
    circle(50)
    end_fill()
    print("hello")
  
speed(0)    
for i in range(12):
    trujkat(10)
kolo()

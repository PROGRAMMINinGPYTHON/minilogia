from turtle import *
import math
from random import *
global a
a = 100
global c
c = 85
global b
b = c/2*math.sqrt(2)

def trojkat(kolor):
    rt(90)
    kolory = ["orange", "pink","blue","green","brown","skyblue","yellowgreen","red","#3ab333","#44d991","#333333","#11111a"]
    fillcolor(kolory[randrange(11)])
    begin_fill()
    fd(c/2)
    rt(180)
    fd(c)
    rt(180)
    fd(c)
    lt(135)
    fd(b)
    lt(90)
    fd(b)
    lt(100)
    end_fill()

def linie():
    pu()
    setpos(0,0)
    pd()
    fd(a)
    trojkat("yellow")
    
    
def KWIATEK():
    for i in range(8):
        setheading(45*i)
        linie()

setheading(90)
KWIATEK()

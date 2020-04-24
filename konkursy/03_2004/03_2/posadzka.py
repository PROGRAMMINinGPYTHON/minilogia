from turtle import *
import math
global a
a = 400/5
global b
b = a/8
def POSADZKA ():
    pu()
    setpos(-200,-200)
    pd()
    wszystko()

def kwadrat_blue():
    b = a/8
    pd()
    fillcolor("seagreen")
    begin_fill()
    setheading(0)
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    for i in range(3):
        setheading(45)
        pu()
        fd(b*math.sqrt(2))
        pd()
        rt(45)
        for j in range(4):
            fd(6*b-i*b*2)
            lt(90)
    setheading(-135)
    pu()
    fd(3*b*math.sqrt(2))
    setheading(0)
    fd(a)
    pd()
            
def yellow():
    pd()
    fillcolor("yellow")
    begin_fill()
    setheading(0)
    for i in range(5):
        fd(a)
        lt(90)
##    setheading(0)
##    fd(a)
    end_fill()
def rząd(x,y):
    for i in range(x,y):
        if i %2 == 0:
            kwadrat_blue()
        else:
            yellow()
def wszystko():#nareszcie
    for j in range(5):
        if j%2 == 1:
            x = 1
            y = 6
        else:
            x = 0
            y = 5
        rząd(x,y)
        pu()
        setheading(180)
        fd(5*a)
        rt(90)
        fd(a)
        
speed(0)
POSADZKA()



    

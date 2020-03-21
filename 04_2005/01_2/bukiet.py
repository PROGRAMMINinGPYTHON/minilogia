from turtle import *
from random import *
global a
a = 50
def kwadrat():
    kolory = ["orange", "yellow", "red","blue","skyblue","green","yellowgreen","pink","brown","grey","white","sadlebrown","black","darkgreen"]
    fillcolor(kolory[randrange(14)])
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    
def BUKIET(n):
    for i in range(n):
        setheading((360/n)*i)
        fd(3*a)
        rt(45)
        for i in range(3):
            kwadrat()
            rt(120)
        pu()
        setpos(0,0)
        pd()

BUKIET(6)

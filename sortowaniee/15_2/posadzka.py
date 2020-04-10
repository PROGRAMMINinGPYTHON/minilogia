from turtle import *
from random import *

def kwadrat(ile):
    a = 480/(ile*3)+1
    kolory = ["red","green","yellow","black","pink","skyblue","brown","yellowgreen","darkgreen","orange","grey","white","purple"]
    fillcolor(kolory[randrange(13)])
    begin_fill()
    for i in range(4):
        fd(a)
        rt(90)
    end_fill()

def rządek(ile):
    a = 480/(ile*3)+1
    for i in range(ile+1):
        kwadrat(ile)
        fd(a/2)
        lt(90)
        fd(1)
        if i > ile-1:
            color("white")
        fd(2*a)
        lt(90)
        fd(a/2)
        rt(90)
        fd(a)
        rt(90)
    color("black")

def kolumny(ile):
    a = 480/(ile*3)+1
    for i in range(ile):
        pu()
        setpos((-480/2)+1.5*a+(3*a*i),-480/2)
        setheading(0)
        pd()
        rządek(ile)

def linie(ile):
    a = 480/(ile*3)+1
    for i in range(ile):
        pu()
        setpos(480/2,(-480/2)+1.5*a+(3*a*i)-1*a)
        pd()
        setheading(90)
        pd()
        rządek(ile)

def posadzka(ile):
    linie(ile)
    kolumny(ile)
speed(0)
posadzka(3)
done()
from turtle import *
import math



def deska(kolor,n):
    color(kolor)
    a = 760/n/4
    pd()
    setheading(0)
    fillcolor(kolor)
    begin_fill()
    fd(2*a)
    lt(90)
    fd(10*a)
    lt(45)
    fd(a*math.sqrt(2))
    lt(90)
    fd(a*math.sqrt(2))
    lt(45)
    fd(10*a)
    end_fill()
def deseczki(n):
    a = 760/n/4
    for i in range(n):
        if i%2 == 0:
            kolor="green"
        else:
            kolor="red"
        deska(kolor,n)
        pu()
        setheading(0)
        fd(4*a)
    
def plotek(n):
    a = 760/n/4
    pu()
    setpos(-380,-200)
    setheading(0)
    fd(a)
    deseczki(n)
    pu()
    setpos(-380,-200)
    setheading(90)
    fd(a*2)
    setheading(0)
    pd()
    for i in range(2):
        color("red")
        fillcolor("red")
        begin_fill()
        fd(760)
        lt(90)
        fd(2*a)
        lt(90)
        fd(760)
        end_fill()
        pu()
        setheading(90)
        fd(3*a)
        rt(90)
speed (0)
plotek(19)

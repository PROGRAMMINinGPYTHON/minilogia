from turtle import *
global a
a = 20

def klocek(kol):
    fillcolor(kol)
    begin_fill()
    fd(2*a)
    lt(90)
    fd(a)
    lt(90)
    fd(2*a)
    lt(90)
    fd(a)
    end_fill()
    rt(180)
    fd(a)
    rt(90)
    fd(2*a)
    rt(90)
    fd(a)
    lt(90)
    
def MOTYW():
    srodek()
def srodek():
    setpos(-1.5*a,-1.5*a)
    setheading(0)
    fillcolor("yellow")
    begin_fill()
    fd(3*a)
    lt(90)
    fd(3*a)
    lt(90)
    fd(3*a)
    lt(90)
    fd(3*a)
    end_fill()
def pasek(ile_klockow,kol):
    for i in range(ile_klockow):
        klocek(kol)
pasek(2,"green")
srodek()

from turtle import *
global a
a = 50

def MASKA():
    pu()
    setpos(-150,150)
    pd()
    fillcolor("black")
    begin_fill()
    setheading(0)
    fd(6*a)
    rt(90)
    fd(6*a)
    rt(90)
    fd(6*a)
    rt(90)
    fd(6*a)
    end_fill()
    kwadrat()
    setheading(0)
    fd(a)
    lt(90)
    fd(0.5*a)
    rt(90)
    kwadrat()
    lt(90)
    fd(a)
    kwadrat()
    rt(180)
    fd(a)
    lt(90)
    fd(0.5*a)
    kwadrat()
    rt(180)
    fd(a)
    kwadrat()
    rt(90)
    fd(a)
    lt(90)
    fd(0.5*a)
    kwadrat()
    rt(180)
    fd(1.5*a)
    rt(90)
    fd(1.5*a)
    kwadrat()
    rt(90)
    fd(a)
    kwadrat()
    rt(180)
    fd(a)
    rt(90)
    fd(0.5*a)
    kwadrat()
    rt(180)
    fd(a)
    rt(90)
    fd(a)
    kwadrat()
    fd(0.5*a)
    lt(90)
    fd(a)
    kwadrat()
    rt(180)
    fd(a)
    kwadrat()
    fd(0.5*a)
    lt(90)
    fd(a)
    kwadrat()
    lt(90)
    fd(a)
    kwadrat()
    rt(180)
    fd(a)
    lt(90)
    fd(0.5*a)
    kwadrat()
    lt(90)
    fd(0.5*a)
    rt(90)
    fd(1.5*a)
    lt(90)
    fd(1*a)
    kwadrat()
    rt(180)
    fd(a)
    kwadrat()
    fd(0.5*a)
    lt(90)
    fd(a)
    kwadrat()
    
def kwadrat():
    fillcolor("white")
    begin_fill()
    setheading(90)
    fd(a)
    rt(90)
    fd(a)
    rt(90)
    fd(a)
    rt(90)
    fd(a)
    end_fill()

def dol_maski():
    pu()
    setpos(-150,-200)
    pd()
    kwadrat()
    rt(180)
    fd(a)
    lt(90)
    fd(0.5*a)
    kwadrat()
    lt(90)
    fd(a)
    kwadrat()
    rt(180)
    fd(a)
    lt(90)
    fd(0.5*a)
    kwadrat()
    rt(180)
    fd(a)
    kwadrat()
    lt(90)
    fd(a)
    rt(90)
    fd(0.5*a)
    kwadrat()
    rt(180)
    fd(a)
    lt(90)
    fd(a)
    rt(90)
    fd(0.5*a)
    rt(90)
    fd(0.5*a)
    kwadrat()
    setheading(90)
    fd(a)
    kwadrat()
    rt(180)
    fd(a)
    rt(90)
    fd(0.5*a)
    kwadrat()

def l_strona_maski():
    pu()
    setpos(-200,-150)
    pd()
    kwadrat()
    rt(90)
    fd(a)
    lt(90)
    fd(0.5*a)
    kwadrat()
    rt(180)
    fd(a)
    kwadrat()
    rt(90)
    fd(a)
    lt(90)
    fd(0.5*a)
    kwadrat()
    setheading(90)
    fd(a)
    kwadrat()
    setheading(180)
    fd(a)
    lt(90)
    fd(0.5*a)
    kwadrat()
    kwadrat()
    pu()
    setheading(90)
    fd(1.5*a)
    rt(90)
    fd(0.5*a)
    kwadrat()
    setheading(0)
    fd(a)
    pd()
    kwadrat()
    fd(a)
    kwadrat()
    rt(90)
    fd(a)
    rt(90)
    fd(0.5*a)
    kwadrat()

def srodek():
    pu()
    setpos(0,0)
    pd()
    fillcolor("grey")
    begin_fill()
    setheading(90)
    fd(2*a)
    rt(90)
    fd(2*a)
    rt(90)
    fd(2*a)
    rt(90)
    fd(2*a)
    end_fill()
    setheading(0)
    pu()
    setpos(0,0)
    setheading(90)
    fillcolor("grey")
    begin_fill()
    pd()
    fd(2*a)
    lt(90)
    fd(2*a)
    lt(90)
    fd(2*a)
    lt(90)
    fd(2*a)
    end_fill()
    pu()
    setpos(0,0)
    fillcolor("white")
    begin_fill()
    pd()
    fd(1*a)
    rt(90)
    fd(2*a)
    rt(90)
    fd(2*a)
    rt(90)
    fd(2*a)
    rt(90)
    fd(2*a)
    end_fill()
speed(0)
MASKA()
dol_maski()
l_strona_maski()
srodek()

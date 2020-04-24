from turtle import *

def przekreconyKwadrat(x, y, a, kolor):
    pu()
    setpos(x,y)
    pd()
    fillcolor(kolor)
    begin_fill()
    setpos(x+a, y+a)
    setpos(x, y+2*a)
    setpos(x-a, y+a)
    setpos(x,y)
    
    end_fill()

def malyKwadrat(x, y, a):
    pu()
    setpos(x, y)
    pd()
    setpos(x + 4*a, y)
    setpos(x + 4*a, y+4*a)
    setpos(x, y+4*a)
    setpos(x,y)

    przekreconyKwadrat(x+a, y, a, "skyblue")
    przekreconyKwadrat(x+3*a, y, a, "skyblue")
    przekreconyKwadrat(x+a, y+2*a, a, "skyblue")
    przekreconyKwadrat(x+3*a, y+2*a, a, "skyblue")
    przekreconyKwadrat(x+2*a, y+a, a, "yellowgreen")


def boczki(x, y, angle,a):
    pu()
    #width(3)
    setpos(x,y)
    pd()
    setheading(angle)
    fd(8*a)
    lt(90)
    begin_fill()
    color("black", "yellowgreen")
    fd(4*a)
    lt(90)
    fd(8*a)
    lt(90)
    fd(4*a)
    lt(90)
    fd(2*a)
    lt(90)
    fd(2*a)
    rt(90)
    fd(4*a)
    rt(90)
    fd(2*a)
    lt(90)
    fd(4*a)
    end_fill()

    

def motyw(n):
    a = n/16
    x = -8*a
    y = -8*a
    malyKwadrat(x, y, a)
    malyKwadrat(x+12*a, y, a)
    malyKwadrat(x, y+12*a, a)
    malyKwadrat(x + 12*a, y+12*a, a)
    malyKwadrat(x + 4*a, y+ 4*a, a*2)
    boczki(x+4*a, y, 0,a)
    boczki(x+16*a, y+4*a, 90, a)
    boczki(x+12*a, y+16*a, 180, a)
    boczki(x, y+12*a, 270, a)

speed(0)
motyw(400)
pu()
setpos(0,0)

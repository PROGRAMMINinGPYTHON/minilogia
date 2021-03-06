from turtle import *

def DYWAN(n):
    a = 400/((n*2*2)+3)
    pu()
    szary_kwadrat(n)
    setpos(-200,-200)
    fillcolor("orange")
    begin_fill()
    setheading(0)
    for i in range(4):
        fd(400)
        lt(90)
    end_fill()
    paski(n,-1.5*a,-1.5*a)
    setheading(90)
    paski(n,1.5*a,-1.5*a)
    setheading(180)
    paski(n,1.5*a,1.5*a)
    setheading(-90)
    paski(n,-1.5*a,1.5*a)
    minus(n)
    srodek(n)
def paski(n,x,y):
    a = 400/((n*2*2)+3)
    pu()
    setpos(x,y)
    pd()
    for i in range(n):
        fillcolor("grey")
        begin_fill()
        color("grey")
        fd(3*a+(2*a*i))
        rt(90)
        fd(a)
        rt(90)
        fd(3*a+(2*a*i))
        rt(90)
        fd(a)
        end_fill()
        przejscie(n)

def przejscie(n):
    a = 400/((n*2*2)+3)
    pu()
    rt(180)
    fd(a)
    rt(90)
    fd(a)
    lt(90)
    fd(1*a)
    lt(90)

def minus(n):
    a = 400/((n*2*2)+3)
    pu()
    setpos(-200,-0.5*a)
    fillcolor("grey")
    begin_fill()
    setheading(0)
    fd(400)
    lt(90)
    fd(a)
    lt(90)
    fd(400)
    lt(90)
    fd(a)
    end_fill()

def srodek(n):
    a = 400/((n*2*2)+3)
    pu()
    setpos(-0.5*a,-200)
    fillcolor("grey")
    begin_fill()
    setheading(90)
    fd(400)
    rt(90)
    fd(a)
    rt(90)
    fd(400)
    rt(90)
    fd(a)
    end_fill()


def szary_kwadrat(n):
    a = 400/((n*2*2)+3)
    setpos(-200-a,-200-a)
    pd()
    setheading(0)
    color("grey")
    fillcolor("grey")
    begin_fill()
    for i in range(4):
        fd(400+2*a)
        lt(90)
    end_fill()

speed(0)        
DYWAN(7)

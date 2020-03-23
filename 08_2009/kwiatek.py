from turtle import *

def KWIATEK(ile):
    y = 180/ile*2+1
    pu()
    setpos(200,0)
    pd()
    setheading(0+y)
    for i in range(ile*2+1):
        pu()
        setpos(0,-100)
        pd()
        if i%2 == 0:
            romb_zolty(ile,i)
        else:
            romb_zielony(ile,i)


def romb_zielony(ile,j):
    y = 180/(ile*2+1)
    x = (360-2*y)/2
    color("black")
    width(1)
    fillcolor("darkgreen")
    begin_fill()
    setheading(0+y+(y*j))
    forwardy(100,x,y)
    end_fill()
    rt(180)
    fd(100)
    rt(180+x)
    fd(100)
    rt(90+y/2)
    fillcolor("yellow")
    begin_fill()
    circle(12.5)
    end_fill()


def romb_zolty(ile,j):
    y = 180/(ile*2+1)
    x = (360-(2*y))/2
    color("black")
    width(1)
    fillcolor("orange")
    begin_fill()
    setheading(0+y+(y*j))
    forwardy(200,x,y)
    end_fill()
    print(x)
    print(y)

def forwardy(a,x,y):
    fd(a)
    lt(180+x)
    fd(a)
    lt(180+y)
    fd(a)
    lt(180+x)
    fd(a)
speed(0)
KWIATEK(2)


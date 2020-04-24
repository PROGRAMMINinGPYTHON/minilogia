from turtle import *
a = 20

def skok():
    pu()
    rt(180)
    fd(a)
    lt(90)
    fd(2*a)

def pietro(ilosc):
    pd()
    fillcolor("green")
    begin_fill()
    setheading(270)
    fd(2*a)
    setheading(0)
    fd(a)
    for i in range(ilosc):
        setheading(90)
        fd(a)
        setheading(0)
        fd(a)
        setheading(-90)
        fd(a)
        setheading(0)
        fd(a)
    setheading(90)
    fd(2*a)
    setheading(180)
    fd(ilosc*a*2+1*a)
    end_fill()

def PAŁAC(lp):
    pu()
    setpos(-(lp*2+1)*a/2, -lp*a + 2*a)
    for i in range(lp):
        pietro(lp-1*i)
        skok()
        
speed(0)
PAŁAC(5)
setpos(0,0)
    

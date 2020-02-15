from turtle import *
global a
a = 210
def XXL_gowinko():
    pu()
    setpos(0,0)
    setheading(-180)
    fd(a)
    rt(120)
    fillcolor("grey")
    begin_fill()
    pd()
    for i in range(6):
        fd(a)
        rt(60)
    end_fill()
    
def gowinko ():
    for i in range(6):
        pu()
        setpos(0,0)
        setheading(60*i)
        pu()
        fd(a/3)
        pd()
        rt(120)
        fillcolor("white")
        begin_fill()
        fd(a/3)
        lt(60)
        fd(a/3)
        lt(60)
        fd(a/3)
        lt(60)
        fd(a/3)
        lt(60)
        fd(a/3)
        lt(60)
        fd(a/3)
        end_fill()
        pu()
        fd(a/3)
        end_fill()
def gowinko_XS():
    pass

def KWIATEK():
    XXL_gowinko()
    gowinko()
KWIATEK()


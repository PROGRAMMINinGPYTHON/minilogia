from turtle import *
global a
a = 10

def glowa():
    setheading(90)
    for i in range(12):
##        fd(80)
        rt(30)
        fd(8*a)
##    setpos(0,0)

    
def uszy():
    setpos(0,0)
    setheading(90)
    fd(8*a)
    rt(30)
    begin_fill()
    fillcolor("black")
    fd(12*a)
    lt(45)
    fd(8*a)
    lt(45)
    fd(8*a)
    lt(45)
    fd(8*a)
    lt(45)
    fd(8*a)
    lt(45)
    fd(8*a)
    lt(45)
    fd(8*a)
    lt(45)
    fd(8*a)
    lt(45)
    end_fill()
    pu()
    setpos(0,0)
    pd()
    setheading(90)
    fd(8*a)
    rt(30)
    fd(16*a)
    rt(30)
    fd(16*a)
    rt(30)
    fd(16*a)
    rt(30)
    fd(16*a)
    rt(30)
    fd(12*a)
    fillcolor("black")
    begin_fill()
    lt(45)
    fd(8*a)
    lt(45)
    fd(8*a)
    lt(45)
    fd(8*a)
    lt(45)
    fd(8*a)
    lt(45)
    fd(8*a)
    lt(45)
    fd(8*a)
    lt(45)
    fd(8*a)
    lt(45)
    fd(8*a)
    end_fill()
    


    
def panda():
    glowa()
    uszy()

panda()

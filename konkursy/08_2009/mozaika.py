from turtle import *
a = 20
def one_mozaika(kolor):
    fillcolor(kolor)
    begin_fill()
    fd(a)
    lt(45)
    fd(a/2)
    lt(90)
    fd(a/2)
    lt(45)
    fd(a)
    lt(45)
    fd(a/2)
    lt(90)
    fd(a/2)
    end_fill()

def kwadrat(x):
    pd()
    one_mozaika("yellow")
    pu()
    lt(180)
    fd(a/2)
    pd()
    rt(90)
    fd(a/2)
    lt(45)
    one_mozaika("yellowgreen")
    lt(45)
    fd(a)
    rt(90)
    one_mozaika("yellow")
    lt(45)
    pu()
    fd(a)
    rt(90)
    pd()
    one_mozaika("yellowgreen")
    pu()
    lt(45)
    fd(a)
    lt(45)
    fd(a)
    lt(45)
    
def rzadek(ile):
    for i in range(ile):
        kwadrat(1*ile)

def mozaika(ile):
    for i in range(ile):
        rzadek(ile)
        setpos(0,0)
        for k in range(i+1):
            pu()
            setheading(135)
            fd(a)
            rt(45)
            fd(a)
            rt(45)
            fd(a/2)
            rt(90)
            fd(a/2)
            lt(45)

        
speed(0)
mozaika(7)



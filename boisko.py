from turtle import *

def WINOGRONO(bok):
    pass
def xxx(a):
    fillcolor("purple")
    begin_fill()
    setheading(90)
    for i in range(6):
        fd(a)
        rt(360/6)
    end_fill()
    rt(120)
    fd(a)
    lt(60)
    fd(a)

def VIdoOGONA(a):
    setheading(90)
    fillcolor("green")
    begin_fill()
    for i in range(6):
        fd(a/2)
        rt(60)
    end_fill()
        
def ogonek(a):
    pu()
    setpos(0,0)
    pd()
    setheading(90)
    fd(a)
    rt(60)
    fd(a)
    lt(60)
    fd(a)
    rt(60)
    fd(a)
    rt(60)
    fd(a)
    lt(60)
    fd(a)
    rt(60)
    fd(a/2)
    for i in range(2):
        VIdoOGONA(a)
        pu()
        fd(a/2)
        lt(60)
        fd(a/2)
        pd()
    for i in range(3):
        VIdoOGONA(a)
        pu()
        fd(a/2)
        rt(60)
        fd(a/2)
        pd()
def rządek(ile,a):
    for i in range(ile):
        xxx(a)
        
def górny_rząd(a):
    pu()
    setpos(0,0)
    pd()
    setheading(90)
    fd(a)
    rt(60)
    fd(a)
    pd()
    for i in range(4):
        xxx(a)
        
def owocki(a):
    for i in range(5):
        rządek(5-i,a)
        pu()
        rt(180)
        fd(a)
        rt(60)
        for j in range(4-i):
            fd(a)
            lt(60)
            fd(a)
            rt(60)
        rt(120)
        fd(a)
        rt(120)
        fd(a)
        rt(60)
        fd(a)
        pd()
    pu()

def ogon(a):
    pu()
    setpos(0,0)
    pd()
    rt(120)
    fd(a)
    rt(60)
    fd(a)
    rt(60)
    fd(a)
    lt(60)
    fd(a)
    rt(60)
    fd(a)



speed(0)
owocki(35)
górny_rząd(35)
ogonek(35)
pu()
setpos(0,0)


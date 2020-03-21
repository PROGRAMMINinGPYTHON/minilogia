from turtle import *
global a
a = 10
def kwadrat(kol):
    fillcolor(kol)
    begin_fill()
    for i in range(4):
        fd(a)
        rt(90)
    end_fill()
    
def łopata_a():
    rt(90)
    fd(40)
    rt(90)
    fd(30)
    rt(90)
    fd(30)
    rt(90)
    fd(20)
    rt(90)
    fd(10)
    kwadrat("green")

def łopata_b():
    pu()
    rt(180)
    fd(4*a)
    lt(90)
    fd(a)
    rt(90)
    pd()
    kwadrat("red")
    rt(90)
    fd(a)
    rt(90)
    fd(a)
    rt(90)
    fd(2*a)
    rt(90)
    fd(30)
    rt(90)
    fd(30)
    rt(90)
    fd(40)

def łopata():
    fd(300)
    łopata_a()
    łopata_b()
    
def WACHLARZ(n):
    for i in range(n):
        pu()
        setpos(0,0)
        pd()
        setheading(180/(n-1)*i)
        łopata()
        
speed(0)
WACHLARZ(4)


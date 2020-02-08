from turtle import *
global a
a = 30

def trójkąt():
    fillcolor("green")
    begin_fill()
    for i in range(3):
        pd()
        fd(30)
        lt(120)
    end_fill()

def szesc():
    for i in range(6):
        pd()
        setheading(0-60*i)
        fd(a)
        lt(300)
        trójkąt()
        setheading(0-60*i)
        fd(2*a)
        rt(60)
  
def szesciokąt():
    for i in range(6):
        fd(3*a)
        rt(360/6)

def gwiazdka():
    setheading(0)
    fillcolor("green")
    begin_fill()
    lt(60)
    fd(a)
    rt(120)
    fd(a)
    setheading(0)
    fd(a)
    rt(120)
    fd(a)
    lt(60)
    fd(a)
    rt(120)
    fd(a)
    lt(60)
    fd(a)
    rt(120)
    fd(a)
    lt(60)
    fd(a)
    rt(120)
    fd(a)
    lt(60)
    fd(a)
    setheading(0)
    fd(a)
    end_fill()
    
def komplet():
    szesciokąt()
    szesc()
    pu()
    setheading(-60)
    fd(2*a)
    pd()
    gwiazdka()
    pu()
    setheading(120)
    fd(2*a)

def rząd():
    komplet()
    setheading(0)
    fd(3*a)
    lt(60)
    fd(3*a)
    komplet()
    setheading(0)
    pu()
    fd(3*a)
    rt(60)
    fd(3*a)
    komplet()

def dwa_rzędy():
    rząd()
    lt(120)
    fd(3*a)
    rt(60)
    fd(3*a)
    lt(60)
    fd(3*a)
    rt(60)
    fd(3*a)
    rząd()
    
def ostatni_komplet():
    pu()
    setpos(-250,200)
    pd()
    dwa_rzędy()
    setheading(-120)
    fd(3*a)
    rt(60)
    fd(3*a)
    komplet()

def wzorek():
    ostatni_komplet()

    
speed(0)
wzorek()


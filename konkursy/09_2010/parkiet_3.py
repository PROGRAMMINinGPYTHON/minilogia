from turtle import *
import math
global a
a = 460/4/7
def PARKIET():
    pass

def kwadrat():
    pass

def deska():
    fillcolor("darkgreen")
    begin_fill()
    fd(a)
    lt(90)
    fd(6*a)
    lt(90)
    fd(a)
    lt(90)
    fd(6*a)
    end_fill()
    lt(90)
    fd(a)
    lt(90)
    fd(6*a)
    rt(90)
    
def ramka():
    for i in range(4):
        deska()
        rt(90)
    fd(a)
    fillcolor("orange")
    begin_fill()
    setheading(0)
    fd(5*a)
    lt(90)
    fd(5*a)
    lt(90)
    fd(5*a)
    lt(90)
    fd(5*a)
    end_fill()

def rama():
    for i in range(1):
        setpos(-7*a*2,-7*a*2)
        pd()
        for j in range(4):
            ramka()
            pu()
            lt(270)
            fd(a)
            rt(90)
            fd(7*a)
            rt(90)
            fd(a)
            lt(180)
            fd(a)
            rt(180)
            pd()        
    for i in range(1):
        pu()
        setpos(115.00,-7*a*2)
        pd()
        for j in range(4):
            ramka()
            pu()
            lt(270)
            fd(a)
            rt(90)
            fd(7*a)
            rt(90)
            fd(a)
            lt(180)
            fd(a)
            rt(180)
            pd()

def duzy_kwadrat():
    pu()
    setpos(-7*a,-8*a)
    pd()
    duza_deska()
    lt(90)
    fd(2*a)
    lt(90)
    fd(2*a)
    rt(180)
    duza_deska()
    rt(90)
    fd(10*a)
    lt(90)
    fd(2*a)
    rt(90)
    fd(2*a)
    rt(180)
    duza_deska()
    rt(180)
    fd(14*a)
    rt(180)
    duza_deska()
    lt(135)
    pu()
    fd(2*a*(math.sqrt(2)))
    pd()
    fillcolor("orange")
    begin_fill()
    rt(45)
    for i in range(4):
        fd(10*a)
        lt(90)
    end_fill()
        
def duza_deska():
    fillcolor("darkgreen")
    begin_fill()
    fd(2*a)
    lt(90)
    fd(12*a)
    lt(90)
    fd(2*a)
    lt(90)
    fd(12*a)
    end_fill()

def dolny_rząd():
    pu()
    setpos(-7*a,-7*2*a)
    pd()
    

def gorny_rząd():
    pass

def obrazek():
    pass
speed(0)
pu()
setpos(-7*a*2,-7*a*2)
pd()
rama()
duzy_kwadrat()

dolny_rząd()

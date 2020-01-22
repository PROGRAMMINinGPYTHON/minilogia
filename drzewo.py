from turtle import *
import math 
global a
a =16
def p_strona(n):
    for i in range(n):
        cool(1)
def l_strona(n):
    for i in range(n):
        cool(1)
        setheading(135)
        fd(4*a*math.sqrt(2))
        setheading(0)
        fd(a)
        pd()
def DRZEWO(n):
    pu()
    setpos(0,-200)
    pd()
    p_strona(n)
    pu()
    setpos(0,-200)
    pd()
    l_strona(n)

def kwadrat(x):
    setheading(0)
    fillcolor(x)
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
def cool(x):
    czastka_a("skyblue")
    czastka_b("skyblue")

def czastka_b(x):
    setheading(0)
    pu()
    fd(2*a)
    pd()
    for i in range(2):
        kwadrat(x)
        pu()
        fd(1.5*a)
        pd()
    pu()
    rt(180)
    fd(2.25*a)
    setheading(-90)
    fd(a)
    for i in range(2):
        pd()
        kwadrat(x)
        pu()
        rt(180)
        fd(a)
        lt(90)
        fd(a)

              
def czastka_a(x):
    kwadrat(x)
    setheading(90)
    fd(a)
    lt(90)
    fd(0.75*a)
    for i in  range(2):
        pd()
        kwadrat(x)
        setheading(90)
        fd(a)
        lt(90)
        pu()
        fd(a)
    rt(180)
    fd(0.25*a)
    pd()
    kwadrat(x)
    fd(1.5*a)
    kwadrat(x)
    
speed(0)   
l_strona(4)
pu()
setpos(0,0)
p_strona(4)


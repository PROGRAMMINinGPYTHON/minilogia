from turtle import *
import math
global a
a = 20
global b
b = a*math.sqrt(2)
global c
c = a+a+b
global d
d = b*math.sqrt(2)
def srodek():
    color("orange")
    pu()
    setpos(0,0)
    pd()
    setheading(90)
    fd(c/2)
    rt(90)
    fd(c/2)
    fillcolor("orange")
    begin_fill()
    setheading(-90)
    fd(c)
    rt(90)
    fd(c)
    rt(90)
    fd(c)
    rt(90)
    fd(c)
    end_fill()
    pu()
    setpos(0,0)

def dwa_trojkąty(i):
    color("orange")
    pu()
    setpos(0,0)
    pd()
    setheading(90*i)
    fd(c/2)
    rt(90)
    trójkąt()
    pu()
    setpos(0,0)
    pd()
    setheading(45+90*i)
    fd((c/2*math.sqrt(2))-b/2)
    rt(90)
    trójkąt()
    
def białe_trojkąty():
    for i in range(4):
        color("orange")
        dwa_trojkąty(i)
        
def trójkąt():
    color("black")
    fillcolor("white")
    begin_fill()
    fd(b/2)
    lt(135)
    fd(a)
    lt(90)
    fd(a)
    lt(135)
    fd(b/2)
    end_fill()
    color("orange")

def gwiazda():
    for i in range(4):
        pu()
        setpos(0,0)
        color("black")
        setheading(90*i)
        fd(c/2)
        lt(90)
        fd(b/2)
        rt(135)
        fd(a)
        fillcolor("orange")
        pd()
        begin_fill()
        lt(90)
        fd(a+b)
        lt(135)
        fd(a+b)
        lt(90)
        fd(a)
        end_fill()
        lt(45)
        fd(a)
        begin_fill()
        fd(a+b)
        rt(135)
        fd(a+b)
        rt(90)
        fd(a)
        rt(45)
        fd(b)
        end_fill()

def duzy_kwadrat_prawa_str():
    pu()
    setpos(a+b+(c/2),a+b +(c/2))
    pd()
    setheading(-90)
    color("black")
    fillcolor("yellow")
    begin_fill()
    fd(a+b)
    rt(135)
    fd((a+b)*math.sqrt(2))
    rt(135)
    fd(a+b)
    end_fill()
    pu()
    setpos(a+b+(c/2),-(a+b)-(c/2))
    pd()
    setheading(90)
    fillcolor("yellow")
    begin_fill()
    fd(a+b)
    lt(135)
    fd((a+b)*math.sqrt(2))
    lt(135)
    fd(a+b)
    end_fill()

def duzy_kwadrat_lewa_str():
    pu()
    color("black")
    setpos(-(a+b)-c/2,-(a+b)-c/2)
    pd()
    setheading(90)
    fillcolor("yellow")
    begin_fill()
    fd(a+b)
    rt(135)
    fd((a+b)*math.sqrt(2))
    rt(135)
    fd(a+b)
    end_fill()
    setpos(-(a+b)-c/2,(a+b)+c/2)
    setheading(0)
    pd()
    fillcolor("yellow")
    begin_fill()
    fd(a+b)
    rt(135)
    fd((a+b)*math.sqrt(2))
    rt(135)
    fd(a+b)
    end_fill()

def ramka():
    for i in range(8):
        pu()
        setpos(0,0)
        setheading(45*i)
        fd((c/2)*math.sqrt(2)+(a+b)*math.sqrt(2))
        pd()
        rt(135)
        fillcolor("orange")
        begin_fill()
        fd(a+b)
        lt(45)
        fd(a+b)
        lt(90)
        fd(a)
        lt(45)
        fd(b*math.sqrt(2))
        lt(45)
        fd(b*math.sqrt(2))
        end_fill()
        lt(45)
        fd(a)
        lt(90)
        fd(a+b)
        fillcolor("yellow")
        begin_fill()
        fd((a+b)*math.sqrt(2))
        lt(135)
        fd(a+b)
        lt(90)
        fd(a+b)
        end_fill()
    pu()
    setpos(0,0)
def trojkąciki():
    for i in range(8):
        pu()
        setheading(45*i)
        color("black")
        fd((c/2)*math.sqrt(2)+(a+b)*math.sqrt(2))
        fillcolor("white")
        pd()
        begin_fill()
        rt(45)
        fd(a)
        lt(135)
        fd(b)
        lt(135)
        fd(a)
        end_fill()
        pu()
        setpos(0,0)

def zolte_trojkąty():
    for i in range(8):
        pu()
        setpos(0,0)
        setheading(45*i)
        fd((c/2)*math.sqrt(2)+(a+b)*math.sqrt(2))
        rt(45)
        fd(a)
        fillcolor("yellow")
        begin_fill()
        pd()
        fd(b)
        rt(90)
        fd(b)
        rt(135)
        fd(b*math.sqrt(2))
        end_fill()
        fd(b)
        rt(45)
        fillcolor("yellow")
        begin_fill()
        fd(b)
        lt(90)
        fd(b)
        lt(135)
        fd(b*math.sqrt(2))
        end_fill()
        
speed(0)    
srodek()
białe_trojkąty()    
gwiazda()
duzy_kwadrat_prawa_str()
duzy_kwadrat_lewa_str()
ramka()    
trojkąciki()
zolte_trojkąty()

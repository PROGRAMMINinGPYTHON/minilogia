from turtle import *
global a
a = 20
global g
g = "yellowgreen"
def kwadrat():
    fillcolor(g)
    begin_fill()
    fd(a)
    rt(90)
    fd(a)
    rt(90)
    fd(a)
    rt(90)
    fd(a)
    end_fill()
def podstawa():
    setpos(0,0)
    kwadrat()
    kwadrat()
    kwadrat()
    kwadrat()
    rt(90)
    fd(a)
    lt(90)
    fd(a)
    kwadrat()
    rt(180)
    fd(a)
    lt(90)
    kwadrat()
    rt(180)
    fd(a)
    lt(90)
    fd(1*a)
    kwadrat()
    rt(180)
    fd(a)
    lt(90)
    fd(a)
    kwadrat()
podstawa()
def rang():
    kwadrat()
    rt(90)
    fd(a)

    
rang()
    
def MUSZKA(n):
    for i in range(n-1):
        rang()
    rt(90)
    fd(a)
    lt(90)
#    fd(a)
    kwadrat()
    speed(0)
MUSZKA(10)

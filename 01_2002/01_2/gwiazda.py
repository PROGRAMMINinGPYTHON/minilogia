from turtle import *
global a
a = 120/3
def kwadrat_z_czer_trojkątem(x):
    pu()
    setpos(0,0)
    setheading(x)
    fd(a)
    pd()
    fillcolor("red")
    begin_fill()
    lt(120)
    fd(a)
    rt(120)
    fd(a)
    rt(120)
    fd(a)
    rt(120)
    end_fill()
    fd(2*a)
    rt(90)
    fd(3*a)
    rt(90)
    fd(3*a)
    rt(90)
    fd(3*a)
    rt(90)
    fd(3*a)
    
def GWIAZDKA():
    for i in range(6):
        kwadrat_z_czer_trojkątem(60*i)
        pu()
        setpos(0,0)

GWIAZDKA()

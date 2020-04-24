from turtle import *
global a
a = 80
def KWIATEK():
    pass
def dupa():
    pu()
    setheading(90)
    fd(a)
    pd()
    color("red")
    for i in range(8):
        circle(a/2)
        rt(360/8)
def liscie_do_podtarcia_tylka():
    setpos(0,-a)
    pd()
    color("green")
    for i in range(2):
        setheading(150)
        for i in range(5):
            fd(a)
            rt(180)
            fd(a)
            rt(180)
            rt(180/6)
        lt(90)
        fd(a)
    pu()
liscie_do_podtarcia_tylka()    
dupa()

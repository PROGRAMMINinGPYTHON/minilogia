from turtle import *

def SZTANGA(ile):
    color("blue")
    strona(ile, -1, rt, lt)
    kij(250)
    strona(ile, 1, lt, rt)
    
    
def kij(a):
    pu()
    setpos(-300,0)
    pd()
    width(10)
    
    setheading(0)
    fd(600)
    width(1)

def strona(ile, znak, skret1, skret2):
    pu()
    a = 250
    setpos(znak*290,0)
    setheading(90)
    pd()
    a = a-20*ile
    width(10)
    for i in range(ile):
        fd(a/2)
        rt(180)
        fd(a)
        pu()
        rt(180)
        fd(a/2)
        skret1(90)
        fd(20)
        skret2(90)
        pd()
        a = a+20

speed(0)
SZTANGA(12)

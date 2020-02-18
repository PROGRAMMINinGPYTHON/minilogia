from turtle import *

def SZTANGA(n):
    kij(n,250)
def kij(ile,a):
    pu()
    setpos(-300,0)
    pd()
    width(10)
    color("blue")
    setheading(0)
    fd(600)
    width(1)
    pu()
    l_strona(ile)
    p_strona(ile)
def l_strona(ile):
    a = 250
    setpos(-290,0)
    setheading(90)
    pd()
    a=a-20*ile
    for i in range(ile):
        width(10)
        fd(a/2)
        rt(180)
        fd(a)
        pu()
        rt(180)
        fd(a/2)
        rt(90)
        fd(20)
        lt(90)
        pd()
        a = a+20
    pu()

def p_strona(ile):
    a = 250
    setpos(290,0)
    pd()
    a = a-20*ile
    for i in range(ile):
        width(10)
        setheading(90)
        fd(a/2)
        rt(180)
        fd(a)
        pu()
        rt(180)
        fd(a/2)
        lt(90)
        fd(20)
        rt(90)
        pd()
        a = a+20
speed(0)
SZTANGA(12)

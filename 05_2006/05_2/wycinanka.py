from turtle import *
import math

def WYCINANKA(ile):
    setheading(60)
    gorny_rządek(ile)
    srokowy_rządek(ile)
    dolny_rządek(ile)


def trapez(ile):
    a = 700/ile/2
    fd(a)
    rt(60)
    fd(a)
    rt(60)
    fd(a)
    rt(120)
    fd(2*a)

def czubek_trapezu(ile):
    a = 700/ile/2
    rt(120)
    fd(a)
    rt(15)
    fd(a/math.sqrt(2))
    rt(90)
    fd(a/math.sqrt(2))
    rt(90)
    fd(a/math.sqrt(2))
    rt(90)
    fd(a/math.sqrt(2))
    lt(45)
    lt(60)
    fd(a)
    rt(180+60)

def gorny_rządek(ile):
    a = 700/ile/2
    pu()
    setpos(-350,a/2)
    pd()
    for i in range(ile):
        figura(ile)
        setheading(60)

def srodkowy_rządek_a(ile):
    a = 700/ile/2
    pu()
    setpos(-350,a/2)
    pd()
    for i in range(ile*2):
        setheading(-45)
        fd(a/math.sqrt(2))
        lt(90)
        fd(a/math.sqrt(2))

def srodkowy_rządek_b(ile):
    a = 700/ile/2
    pu()
    setpos(-350,-a/2)
    pd()
    for i in range(ile*2):
        setheading(45)
        fd(a/math.sqrt(2))
        rt(90)
        fd(a/math.sqrt(2))
def dolne_trojkąty(ile):
    a = 700/ile/2
    lt(45)
    fd(a/math.sqrt(2))
    rt(90)
    fd(a/math.sqrt(2))
    lt(90)
    fd(a/math.sqrt(2))
    rt(90)
    fd(a/math.sqrt(2))

def figura(ile):
    a = 700/ile/2
    trapez(ile)
    czubek_trapezu(ile)
    dolne_trojkąty(ile)

def srokowy_rządek(ile):
    srodkowy_rządek_a(ile)
    srodkowy_rządek_b(ile)

def dolny_rządek(ile):
    a = 700/ile/2
    pu()
    setpos(350,-a/2)
    pd()
    for i in range(ile):
        setheading(0)
        rt(120)
        figura(ile)
        
speed(0)
WYCINANKA(9)

from turtle import *
import math
def kafelek_kwadrat_zolty(ile):
    a = 480/ile
    fillcolor("yellow")
    begin_fill()
    for i in range(4):
        pd()
        fd(a)
        lt(90)
    end_fill()

def kafelek_lewa_str(ile):
    a= 480/ile
    setheading(45)
    b = (a*math.sqrt(2))/6
    fd(b)
    lt(45)
    czerwony_kwadrat(ile)
    fd(b)
    lt(45)
    romb(ile)
    fd(b/math.sqrt(2))
    rt(45)
    fd(b)
    rt(90)
    romb(ile)

def romb(ile):
    a = 480/ile
    b = (a*math.sqrt(2))/6
    fillcolor("red")
    begin_fill()
    for i in range(2):
        fd(b)
        rt(135)
        fd(b)
        rt(45)
    end_fill()

def czerwony_kwadrat(ile):
    a= 480/ile
    b = (a*math.sqrt(2))/6
    fillcolor("red")
    begin_fill()
    for i in range(4):
        fd(b)
        rt(90)
    end_fill()

def kafelek(ile):
    kafelek_kwadrat_zolty(ile)
    kafelek_lewa_str(ile)

def rządek(ile):
    for i in range(ile):
        kafelek(ile)

def wyszystko(ile):
    for i in range(ile):
        rządek(ile)

def posadzka(ile):
    wszystko(ile)

speed(0)
setpos(-480/2,-480/2)
kafelek(1)
done()
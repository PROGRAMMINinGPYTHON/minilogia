from turtle import *
import math
global a
a = 10
def literka_T():
    fillcolor("darkgreen")
    begin_fill()
    fd(a)
    lt(90)
    fd(a)
    rt(90)
    fd(a)
    lt(90)
    fd(a)
    lt(90)
    fd(3*a)
    lt(90)
    fd(a)
    lt(90)
    fd(a)
    rt(90)
    fd(a)
    end_fill()
    lt(90)

def tetki(ile):
    pass

def rządek(ile, poczatkowy_kąt):
    setheading(poczatkowy_kąt)
    for i in range((ile*2)-1):
        if i %2  == 1:
            setheading(90+poczatkowy_kąt)
            fd(2*a)
            setheading(0+poczatkowy_kąt)
        else:
            setheading(-90+poczatkowy_kąt)
            fd(2*a)
        setheading(0+poczatkowy_kąt)
        rt(180*(i%2))
        literka_T()
        setheading(0+poczatkowy_kąt)
        if i %2 == 0:
            fd(4*a)
        else:
            fd(2*a)

        rt(180)
    fd(1*a)

def tetki_dla_jeden():
    for i in range(2):
        pd()
        literka_T()
        rt(90)
        fd(a)
        lt(90)
        fd(a)
        rt(180)
    for i in range(2):
        fd(a)
        rt(90)
        literka_T()
        fd(a)
        rt(90)
    lt(135)
    pu()
    fd(4*a*math.sqrt(2))
speed(0)


def ramka(ile):
    for i in range(4):
        rządek(ile, -90 * i)
    setheading(180)
    # fd(2*a)
    # rt(45)
    setheading(180)
    fd(2*a)
    rt(45)
    fd(1*a*math.sqrt(2))
    setheading(90)
    fd(2*a)

ramka(1)

ramka(2`)


done()
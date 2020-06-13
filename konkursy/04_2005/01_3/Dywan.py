from turtle import *
import math
global a
a = 10
def dywanik(szer,wys):
    print("szer: ", szer)
    if szer%2 == 1:
        szer = szer+1
    print("szer: ", szer)

    for i in range(wys):
        rządek(szer)
        przejscie(szer,i)
        print(szer)
    #wykonczenie(szer,wys)

def DYWAN(szer,wys):
    pu()
    setpos(-300,-300)
    pd
    dywanik(szer,wys)
    wykonczenie(szer,wys)


def wykonczenie(szer,wys):
    if szer %2 == 1:
        pu()
        setpos(-300,-300)
        setheading(0)
        fd((szer)*a*8)
        fd(1)
        fillcolor("white")
        begin_fill()
        lt(90)
        fd(wys*a*4*2)
        rt(90)
        fd(8*a)
        rt(90)
        fd(wys*a*4*2)
        rt(90)
        fd(8*a)
        end_fill()
        rt(180)
        pd()
        color("white")
        fd(8*a)

def przejscie(szer,i):
    if i % 2 == 0:
        lt(90)
        fd(8*2*a)
        lt(90)
    else:
        rt(180)

def kawałek():
    fillcolor("darkgreen")
    begin_fill()
    for i in range(4):
        fd(8*a)
        lt(90)
    end_fill()
    fd(3*a)
    lt(135)
    pasek()
    rt(180)
    fd(4*a)
    gruby_pasek()
    rt(180)
    fd(a)
    lt(90)
    fd(8*a)
    lt(90)
    fd(3*a)
    lt(135)
    pasek()
    rt(180)
    fd(4*a)
    gruby_pasek()

def gruby_pasek():
    fillcolor("white")
    begin_fill()
    lt(135)
    fd(3*a*math.sqrt(2))
    rt(45)
    fd(a)
    rt(90)
    fd(a)
    rt(45)
    fd(3*a*math.sqrt(2))
    rt(45)
    fd(a)
    rt(90)
    fd(a)
    end_fill()

def pasek():
    fillcolor("white")
    begin_fill()
    fd(3*a*math.sqrt(2))
    rt(45)
    fd(a)
    rt(135)
    fd(4*a*math.sqrt(2))
    rt(135)
    fd(a)
    end_fill()

def rządek(szer):
    for i in range(szer):
        pd()
        kawałek()
        pu()
        if i % 2 == 0:
            fd(15*a)
            rt(90)
            fd(8*a)
            rt(180)
        else:
            rt(180)
            fd(a)
            lt(90)
            fd(8*a)


speed(0)
DYWAN(3,3)

pd()
done()



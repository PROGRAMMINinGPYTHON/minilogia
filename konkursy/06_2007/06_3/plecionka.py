from turtle import *
import math

global a
a = 20

def PLECIONKA(ile):
    zielone_tło(ile)
    białe_kwadraty(ile)
    wykonczenie(ile)
    koniec()

def kwadrat():
    color("black")
    fillcolor("white")
    begin_fill()
    setheading(45)
    for i in range(4):
        fd(4*a*math.sqrt(2))
        rt(90)
    rt(45)
    color("white")
    fd(a-1)
    pencolor("black")
    rt(45)
    fd(3*a*math.sqrt(2))
    lt(90)
    fd(3*a*math.sqrt(2))
    lt(90)
    fd(3*a*math.sqrt(2))
    lt(90)
    fd(3*a*math.sqrt(2))
    rt(45)
    pu()
    fd(a)
    end_fill()

def białe_kwadraty(ile):
    setpos(-ile*2*a,0)
    for i in range(ile):
        pd()
        kwadrat()
        rt(180)
        pu()
        fd(2*a)

def zielone_tło(ile):
    szer = ile*4*a
    wys = 8*a
    pu()
    setpos(-szer/2,-wys/2)
    pd()
    fillcolor("yellowgreen")
    begin_fill()
    setheading(0)
    fd(szer)
    lt(90)
    fd(wys)
    lt(90)
    fd(szer)
    lt(90)
    fd(wys)
    end_fill()

def wykonczenie(ile):
    setpos(-ile*2*a,-80)
    setheading(0)
    fd(4*a-1)
    for i in range(ile):
        lt(45)
        color("black")
        pd()
        fillcolor("white")
        begin_fill()
        fd(4*a*math.sqrt(2))
        lt(135)
        pu()
        fd(a)
        pd()
        lt(45)
        pd()
        fd(3*a*math.sqrt(2))
        lt(45)
        pu()
        fd(a)
        pd()
        lt(90)
        fd(2*a-1)
        end_fill()

def koniec():
    setheading(0)
    pu()
    fd(2*a)
    lt(90)
    color("black")
    fillcolor("white")
    begin_fill()
    pd()
    fd(160)
    pu()
    rt(90)
    fd(1000)
    rt(90)
    fd(160)
    rt(90)
    fd(1000)
    end_fill()
    rt(180)
    setheading(0)
    color("white")
    pd()
    fd(1000)


speed(0)
PLECIONKA(15)
done()
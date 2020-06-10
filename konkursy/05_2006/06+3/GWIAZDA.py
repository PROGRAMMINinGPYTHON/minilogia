from turtle import *
import math

def GWIAZDA(bok):
    bok = bok/2
    for i in range(6):
        pu()
        setpos(0,0)
        setheading(90+(60*i))
        fd(bok)
        rt(210)
        pd()
        figurka(bok)

def cosiek(bok):
    lt(90)
    for i in range(2):
        pd()
        trójkąt_niebieski(bok)
        pu()
        fd(bok/2)
        lt(90)
        fd(bok/2)
        lt(90)
    lt(45)
    fd(bok/4/math.sqrt(2))
    lt(45)
    pd()
    trójkąt_zółty(bok)
    rt(45)
    fd(bok/2/math.sqrt(2))
    rt(135)
    trójkąt_zółty(bok)
    rt(45)
    fd((bok/4/math.sqrt(2))*3)


def trójkąt_niebieski(bok):
    trójkąt(bok/2,bok/2/math.sqrt(2),"skyblue")

def trójkąt_zółty(bok):
    trójkąt(bok/4,bok/4/math.sqrt(2),"yellow")


def trójkąt(bok_a,bok_b,kolor):
    fillcolor(kolor)
    begin_fill()
    fd(bok_a)
    lt(135)
    fd(bok_b)
    lt(90)
    fd(bok_b)
    lt(135)
    end_fill()

def figurka(bok):
    cosiek(bok)
    lt(135)
    fd(bok/2)
    lt(90)
    rt(180)
    cosiek(bok)
    pu()
    rt(135)
    fd(bok/2)
    lt(90)
    fd(bok/4)
    rt(90)
    fd(bok/2)
    rt(270)
    pd()
    cosiek(bok)

speed(0)
GWIAZDA(350)
done()
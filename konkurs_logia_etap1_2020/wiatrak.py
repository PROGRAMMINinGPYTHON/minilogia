from turtle import *
import math

a = 25
b = 12.5


def wiatrak():
    czerwone_lopaty()
    zielone_lopaty()


def czerwone_lopaty():
    for i in range(6):
        setheading(90 - 60 * i)
        czerwona_lodyga()
        pu()
        setpos(0, 0)
        pd()


def zielone_lopaty():
    for i in range(6):
        setheading(120 - 60 * i)
        zielona_lodyga()
        pu()
        setpos(0, 0)
        pd()


def czerwona_lodyga():
    fd(5 * a)
    lt(180)
    trojkat("red", 1 * a)
    rt(90)
    trojkat("red", 2 * a)
    lt(90)
    fd(5 * a)
    rt(180)
    trojkat("red", 3 * a)


def zielona_lodyga():
    fd(5*b)
    lt(90)
    trojkat("darkgreen",1*b)
    rt(90)
    trojkat("darkgreen",2*b)
    rt(180)
    fd(5*b)
    lt(90)
    trojkat("darkgreen",3*b)


def trojkat(kolor, bok):
    fillcolor(kolor)
    begin_fill()
    fd(bok)
    lt(135)
    fd(bok * math.sqrt(2))
    lt(135)
    fd(bok)
    end_fill()


wiatrak()

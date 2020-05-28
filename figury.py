from turtle import *

def kwadrat(bok,kolor_pisaka,kolor_wypełnienia):
    fillcolor(kolor_wypełnienia)
    begin_fill()
    color(kolor_pisaka)
    for i in range(4):
        fd(bok)
        lt(90)
    end_fill()

def trójkąt():
    pass

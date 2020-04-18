from turtle import *
import math
global a
a = 26
global b
b = a*math.sqrt(2)

def głowa_wiatraka():
    lt(90)
    lisc("yellowgreen")
    lisc("orange")
    lisc("yellowgreen")
    lisc("orange")

def lisc(kolor):
    fillcolor(kolor)
    begin_fill()
    fd(a)
    rt(45)
    fd(b)
    rt(45+90)
    fd(2*a)
    rt(90)
    fd(a)
    end_fill()


def kwiatek():
    pass


def łodyga(jak_dluga):
    pass


def trzy_kwiatki():
    pass


def wiatraki(ile):
    pass

głowa_wiatraka()
speed(1)
done()
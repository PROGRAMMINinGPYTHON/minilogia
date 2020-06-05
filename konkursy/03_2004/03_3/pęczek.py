from turtle import *
import math
global a
a = 20
def PĘCZEK(ileW,ileSz):
    for i in range(ileSz):
        setheading((360/ileSz)*i)
        rt(180)
        pu()
        fd(a/2/math.sqrt(2))
        pd()
        rt(180)
        jeden_patyk(ileW)
        pu()
        setpos(0,0)
        pd()

def jeden_patyk(ileW):
    color("red")
    for i in range(ileW+1):
        # przejscie()
        kwadraty_na_patyku(ileW,i)
        przejscie()
    rt(180)
    color("white")
    fd(a-0.5)

def kwadrat(ileW):
    rt(45)
    color("red")
    for i in range(4):
        pd()
        fd(a/math.sqrt(2))
        lt(90)

def kwadraty_na_patyku(ileW,j):
    for i in range(j):
        kwadrat(ileW)
        pu()
        fd(a/math.sqrt(2))
        lt(90)
        fd(a/math.sqrt(2))
        lt(135)
        fd(a/2/math.sqrt(2))
        lt(180)
        pd()



def przejscie():
    pu()
    fd(a/2/math.sqrt(2))
    pd()
    fd(a)

speed(0)
PĘCZEK(1,4)
setpos(0,0)
color("black")
done()
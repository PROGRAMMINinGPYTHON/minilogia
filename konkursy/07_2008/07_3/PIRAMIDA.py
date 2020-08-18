from turtle import *
import math
def klocek(kolor,szer):
    a = 500/(szer*2+1)/3
    fillcolor(kolor)
    begin_fill()
    fd(a/2)
    rt(45)
    fd(a*math.sqrt(2))
    lt(90)
    fd(a*math.sqrt(2))
    rt(45)
    fd(a/2)
    lt(90)
    fd(a)
    lt(90)
    fd(a)
    rt(90)
    fd(a/2)
    lt(90)
    fd(a)
    lt(90)
    fd(a/2)
    rt(90)
    fd(a)
    lt(90)
    fd(a)
    end_fill()

def piętro(szer,j):
    a = 500/(szer*2+1)/3
    for i in range(szer-j):
        klocek("yellowgreen",szer)
        przejscie_do_czerwonego(szer)
        klocek("red",szer)
        przejscie_do_zielonego(szer)
    klocek("yellowgreen",szer)

def przejscie_do_zielonego(szer):
    a = 500/(szer*2+1)/3
    lt(90)
    fd(a/2)
    rt(45)
    fd(a*math.sqrt(2))
    lt(90)
    fd(a*math.sqrt(2))
    rt(135)
    fd(a)
    lt(90)

def przejscie_do_czerwonego(szer):
    a = 500/(szer*2+1)/3
    setheading(0)
    fd(a/2)
    rt(45)
    fd(a*math.sqrt(2))
    lt(90)
    fd(a*math.sqrt(2))
    rt(45)
    fd(a/2)
    lt(90)
    fd(a)
    lt(90)
    fd(a/2)
    rt(180)


def PIRAMIDA(ile):
    a = 500/(ile*2+1)/3
    pu()
    setpos(-250,0)
    pd()
    for i in range(ile):
        piętro(ile,i)
        pu()
        print(heading())
        setheading(90)
        fd(3.5*a)
        lt(90)
        fd(5*a*(ile-i)-1-2.5*a)
        rt(180)
        pd()


speed(0)
PIRAMIDA(2)
done()
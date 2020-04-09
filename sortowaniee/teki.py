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

def rządek_literek(ile_T,ile,x):
    for i in range(ile+(ile-1)):
        if i == ile+1:
            break
        rt(180)
        pd()
        literka_T()
        pu()
        setheading(x)
        fd(2*a)
        if i %2 == 0:
            rt(90)
            fd(2*a)
            lt(270)
        else:
            fd(2*a)
            lt(90)
            fd(2*a)
            rt(90)
    rt(180)
    fd((ile-1)*2*3*a)
    fd(4*a)
    literka_T()
def tetki(ile):
    pass

rządek_literek(4
               ,4,0)
done()
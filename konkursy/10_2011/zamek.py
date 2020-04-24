from turtle import *

def ZAMEK(n):
    pass

def kształt(n):
    a = 760/((n*2)+1)
    pu()
    setpos(-760/2,-250)
    print(760/2)
    setheading(0)
    pd()
    fillcolor("grey")
    begin_fill()
    fd(760)
    lt(90)
    fd(4*a)
    for i in range(2):
        lt(90)
        fd(a)
        lt(90)
        fd(a)
        rt(90)
        fd(a)
        if i == 0:
            rt(90)
            fd(a)
    fd((n*a*2)-a)
    rt(90)
    fd(a)
    lt(90)
    fd(a)
    lt(90)
    fd(4*a)
    end_fill()

kształt(9)




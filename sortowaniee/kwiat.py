from turtle import *

global a
a = 8
def kwiat():
    platek(0,19*a)
    platek(0,0)
    platek(0,-19*a)
    platek(131.64,76.00)
    platek(131.64,-76)
    platek(-131.64,-76)
    platek(-131.64,76)


def platek(x, y):
    pu()
    setpos(x, y)
    for i in range(6):
        setheading(90 + 60 * i)
        pu()
        fd(a)
        rt(60)
        fd(4 * a)
        lt(60)
        pd()
        listek()
        pu()
        setpos(x, y)
        pd()


def listek():
    fillcolor("yellow")
    begin_fill()
    fd(4 * a)
    lt(60)
    fd(4 * a)
    lt(60)
    fd(4 * a)
    lt(120)
    fd(4 * a)
    rt(60)
    fd(4 * a)
    lt(120)
    fd(4 * a)
    end_fill()

speed(0)
kwiat()
done()

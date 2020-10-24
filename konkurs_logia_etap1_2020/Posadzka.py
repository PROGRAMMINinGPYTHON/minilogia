from turtle import *

global a
a = 24


def posadzka(n):
    for i in range(int(n / 2)):
        pu()
        setpos(-350, -280 + 66.29999999999998 * (i + 1))
        rzadek(n)
        setheading(90)
        for j in range(1 + i):
            setpos(-350, -280 + (66.29999999999998 * (j + 1)))
            setheading(0)


def rzadek(n):
    for i in range(int((n / 2)) + 1):
        pd()
        kwadrat_duzy()
        pu()
        rt(30)
        fd(a)
        lt(90)
        fd(a)
        rt(120)
        fd(a)
        lt(90)
        fd(a)
        rt(30)


def kwadrat():
    begin_fill()
    fillcolor("yellow")
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()


def kwadrat_duzy():
    for i in range(2):
        rt(30)
        kwadrat()
        lt(90)
        fd(a)
        rt(30)
        kwadrat()
        lt(90)
        fd(a)
        lt(60)

posadzka(6)

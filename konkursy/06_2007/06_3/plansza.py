from turtle import *


def PLANSZA(n):
    a = 400 / n / 6
    pu()
    setpos(-200, -200)
    pd()
    czarny_kwadrat()
    for i in range(n):
        setpos(-200, -200 + 2 * a + 6 * a * i)
        rządek_czerwony(n)

    for i in range(n):
        setpos(-200, -200 + 3 * a + 6 * a * i)
        rządek_zielony(n)


def HHH(kolor, n):
    color(kolor)
    a = 400 / n / 6
    fillcolor(kolor)
    begin_fill()
    setheading(0)
    fd(a)
    lt(90)
    fd(a)
    rt(90)
    fd(a)
    rt(90)
    fd(a)
    lt(90)
    fd(a)
    lt(90)
    fd(3 * a)
    lt(90)
    fd(a)
    lt(90)
    fd(a)
    rt(90)
    fd(a)
    rt(90)
    fd(a)
    lt(90)
    fd(a)
    lt(90)
    fd(3 * a)
    end_fill()


def kwadracik(n, kolor):
    a = 400 / n / 6
    color("red")
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()


def rządek_czerwony(n):
    a = 400 / n / 6
    print(a)
    rt(90)
    setheading(-90)
    fd(a)
    lt(90)
    kwadracik(n, 'red')

    for i in range(n - 1):
        setheading(0)
        pu()
        fd(2 * a)
        pd()
        kwadracik(n, 'red')
        pu()
        fd(a)
        rt(90)
        fd(a)
        lt(90)
        pd()
        HHH("red", n)
        lt(90)
        pu()
        fd(3 * a)
        lt(90)
        fd(a)
        rt(90)
        kwadracik(n, 'red')
    setheading(0)
    fd(2 * a)
    kwadracik(n, 'red')
    rt(90)
    fd(1 * a)
    lt(90)
    fd(a)
    HHH("red", n)


def rządek_zielony(n):
    a = 400 / n / 6
    HHH("darkgreen", n)
    lt(90)
    pu()
    fd(3 * a)
    lt(90)
    fd(a)
    rt(90)
    kwadracik(n, "darkgreen")
    fd(2 * a)
    for i in range(n - 1):
        kwadracik(n, "darkgreen")
        setheading(0)
        fd(a)
        rt(90)
        fd(a)
        lt(90)
        HHH("darkgreen", n)
        lt(90)
        pu()
        fd(3 * a)
        lt(90)
        fd(a)
        rt(90)
        kwadracik(n, "darkgreen")
        fd(2 * a)
        kwadracik(n, "darkgreen")


def czarny_kwadrat():
    fillcolor("black")
    begin_fill()
    for i in range(4):
        fd(401)
        lt(90)
    end_fill()


speed(0)
PLANSZA(2)
done()

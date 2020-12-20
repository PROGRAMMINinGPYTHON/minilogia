from turtle import *

def gwiazdy(k):
    o = 560 / len(k)
    rzadek(k, o)
    for i in range(3):
        for p in range(len(k) - i):
            rzadek(k, 0)


def gwiazda_klasyczna(kolor, a):
    pd()
    fillcolor(kolor)
    begin_fill()
    setheading(0)
    for i in range(6):
        fd(a)
        lt(60)
        fd(a)
        rt(120)
    end_fill()
    return "" + kolor + " " + str(a)


def gwiazda_z_dziorka(kolor, a):
    gwiazda_klasyczna(kolor, a)
    pu()
    fd(1.5 * a)
    rt(120)
    fd(a / 2)
    rt(60)
    fd(a / 2)
    rt(180)
    pd()
    gwiazda_klasyczna("white", a / 2)
    pu()
    fd(a / 2)
    lt(60)
    fd(a / 2)
    lt(120)
    fd(a + a / 2)
    pd()
    rt(180)


def przejscie(a):
    pu()
    fd(a)
    lt(60)
    fd(a)
    rt(120)
    fd(a)
    lt(60)
    fd(a)
    pd()


def jaka_gwiazda(ma_czy_nie):
    pass


def rzadek(j, g):
    j = str(j)
    j = list(j)
    print(j)
    x = [lambda: gwiazda_klasyczna("green", g)
        , lambda: gwiazda_z_dziorka("green", g)
        , lambda: gwiazda_klasyczna("red", g),
         lambda: gwiazda_z_dziorka("red", g),
         # lambda: gwiazda_klasyczna("green", g),
         # lambda: gwiazda_z_dziorka("green", g),
         # lambda: gwiazda_klasyczna("red", g),
         # lambda: gwiazda_z_dziorka("red", g),
         # lambda: gwiazda_klasyczna("green", g),
         # lambda: gwiazda_z_dziorka("green", g)
         ]
    pu()

    setpos(-560 / 2, 0)
    g = 560 / len(j) / 3
    setheading(60)
    fd(5 * g)
    setheading(-180)
    fd(2.5 * g)
    pd()
    for q in range(3):
        for i in range(len(j) - q):
            x[int(j[i])%4]()
            przejscie(g)
        rt(180)
        pu()
        fd(3 * g * (len(j) - 1 - q))
        lt(60)
        fd(g)
        lt(60)
        fd(3 * g)
        rt(120)
        fd(1 * g)
        rt(180)
        pd()


speed(0)
rzadek(2490, 20)
setpos(-560/2,0)
setheading(0)
fd(560)
done()

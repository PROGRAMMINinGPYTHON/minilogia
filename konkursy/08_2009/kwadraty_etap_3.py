from turtle import *


def KWADRATY(n):
    pass


def kwadrat(n, kolor):
    a = 480 / (n * 2 + 3 + 4)
    color("yellow")
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()


def teleport(n):
    pu()
    setpos(-240, -240)
    pd()


def czarna_siatka_tło(n):
    a = 480 / (n * 2 + 3 + 4)
    teleport(n)
    fillcolor("black")
    color("black")
    begin_fill()
    setheading(0)
    for i in range(4):
        fd(480)
        lt(90)
    end_fill()


def czarna_siatka_linie(n):
    a = 480 / (n * 2 + 3 + 4)
    teleport(n)
    pu()
    for j in range(2):
        for i in range(n * 2 + 3 + 4):
            teleport(n)
            setheading(0 + (90 * j))
            fd(a * i)
            if j == 0:
                lt(90)
            else:
                rt(90)
            pd()
            color("yellow")
            fd(480)


def czarna_siatka_full(n):
    a = 480 / (n * 2 + 3 + 4)
    czarna_siatka_tło(n)
    czarna_siatka_linie(n)


def rządek(n, ile, kolor):
    a = 480 / (n * 2 + 3 + 4)
    for i in range(ile):
        kwadrat(n, kolor)
        fd(a)


def przejscie(n, i):
    a = 480 / (n * 2 + 3 + 4)
    pu()
    lt(90)
    fd(a)
    lt(90)
    fd(a * n - a * i - a - i * a)
    rt(180)
    pd()


def piramida(n, kolor):
    a = 480 / (n * 2 + 3 + 4)
    for i in range(n - 1):
        rządek(n, n - 2 * i, kolor)
        przejscie(n, i)

###################################################do poprawy!

def kwadracik(n):
    a = 480 / (n * 2 + 3 + 4)
    setpos(0,0)
    for i in range(4):
        fd(a+n*a)
        rt(180)
        piramida(n,"red")
        setpos(0,0)
        for j in range(i):
            fd(n*a+2*a)
            rt(90)





speed(0)
kwadracik(9)
done()

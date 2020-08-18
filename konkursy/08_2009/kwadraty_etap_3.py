from turtle import *
import math


def KWADRATY(n):
    a = 480 / (n * 2 + 3 + 4)
    czarna_siatka_full(n)
    zielone_1(n)
    czerwone_2(n)
    zielone_2(n)
    czerwone_1(n)


def przejscie_x(n,i):
    pu()
    setpos(0, 0)
    setheading(135 + 90 * i)

def czerwone_1(n):
    a = 480 / (n * 2 + 3 + 4)
    for i in range(4):
        przejscie_x(n,i)
        fd(480/2*math.sqrt(2))
        rt(135)
        fd(a)
        rt(90)
        fd(2*a)
        pd()
        piramida(n,"red")

def zielone_2(n):
    a = 480 / (n * 2 + 3 + 4)
    for i in range(4):
        pu()
        setpos(0, 0)
        setheading(45 - 90 * i)
        fd(480 / 2 * math.sqrt(2))
        rt(180)
        fd(480 / 4 * math.sqrt(2))
        fd(a / 4 * math.sqrt(2))
        lt(45)
        fd((n + 1) / 2 * a)
        fd(a / 2)
        rt(90)
        fd((n / 2) * a)
        rt(180)
        pd()
        fd(n*a+a)
        lt(90)
        fd(a)
        piramida(n, "yellowgreen")


def zielone_1(n):
    a = 480 / (n * 2 + 3 + 4)
    for i in range(4):
        przejscie_x(n, i)
        fd(480 / 2 * math.sqrt(2))
        rt(135)
        fd(a)
        rt(90)
        fd(2 * a)
        fd(n*a+a)
        lt(90)
        fd(a)
        pd()
        piramida(n, "yellowgreen")


def czerwone_2(n):
    a = 480 / (n * 2 + 3 + 4)
    for i in range(4):
        pu()
        setpos(0,0)
        setheading(45-90*i)
        fd(480/2*math.sqrt(2))
        rt(180)
        fd(480/4*math.sqrt(2))
        fd(a/4*math.sqrt(2))
        lt(45)
        fd((n+1)/2*a)
        fd(a/2)
        rt(90)
        fd((n/2)*a)
        rt(180)
        pd()
        print(heading())
        piramida(n,"red")

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




speed(0)
KWADRATY(3)
done()

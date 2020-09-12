from turtle import *


def ziarno(n, kierunek):
    a = 250 / n / 2
    color("black")
    fillcolor("yellow")
    begin_fill()
    setheading(kierunek)
    for i in range(2):
        fd(a)
        rt(45)
        fd(2 * a)
        rt(45)
        fd(a)
        rt(90)
    end_fill()


def przejscie_w_rządku(n):
    a = 250 / n / 2
    setheading(0)
    fd(2 * a)


def łodyga(n):
    rządek(n, 90)
    pu()
    setpos(0, 0)
    pd()
    rządek(n, -0)


def rządek(n, kierunek):
    a = 250 / n / 2
    for i in range(n):
        ziarno(n, kierunek)
        przejscie_w_rządku(n)


def kreska():
    pu()
    setpos(-250,0)
    setheading(0)
    pd()
    fd(250)

def ziarno_poziome(n):
    ziarno(n, 45)
    kreska()


# -----------------------
def kls(n):
    łodyga(n)
    ziarno_poziome(n)


speed(0)
kls(10)
done()

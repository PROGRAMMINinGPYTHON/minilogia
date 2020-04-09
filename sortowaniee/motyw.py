from turtle import *


def prostokąt(ile):
    a = 450 / ile / 6
    fillcolor("skyblue")
    begin_fill()
    setheading(0)
    for i in range(2):
        fd(4 * a)
        lt(90)
        fd(6 * a)
        lt(90)
    end_fill()
    zolte_kwadraty(ile)
    białe_pole(ile)


def zolte_kwadraty(ile):
    a = 450 / ile / 6
    setheading(0)
    zółty_kwadrat(ile)
    setheading(0)
    fd(3 * a)
    zółty_kwadrat(ile)
    setheading(90)
    pu()
    fd(5 * a)
    pd()
    rt(90)
    zółty_kwadrat(ile)
    setheading(180)
    pu()
    fd(3 * a)
    rt(180)
    pd()
    zółty_kwadrat(ile)


def białe_pole(ile):
    a = 450 / ile / 6
    pu()
    fd(a)
    rt(90)
    fd(a)
    lt(90)
    fillcolor("white")
    begin_fill()
    pd()
    for i in range(2):
        fd(2 * a)
        rt(90)
        fd(2 * a)
        rt(90)
    end_fill()


def prawa_str(ile):
    a = 450 / ile / 6
    pu()
    setpos(-2 * a, (3 * a * ile) - (6 * a))
    pd()
    for i in range(ile):
        for j in range(ile - i):
            prostokąt(ile)
            przejście_w_rządku(ile)
            pd()
        przejscie_DO_nowego_rzędu(ile, i)


def lewa_str(ile):
    a = 450 / 6 / ile
    pu()
    setpos(-2 * a, 3 * a * ile - (6 * a))
    pd()
    for i in range(ile):
        for i in range(ile - i):
            prostokąt(ile)
            przejście_w_rządku(ile)
            pd()
        pu()
        setheading(180)
        fd(4 * a)
        rt(90)
        fd(6 * a * i + 1 + 3 * a)
        pd()

def zółty_kwadrat(ile):
    a = 450 / ile / 6
    fillcolor("yellow")
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()


def przejście_w_rządku(ile):
    a = 450 / ile / 6
    pu()
    setheading(-90)
    fd(10 * a)
    rt(90)
    fd(a)
    rt(180)


def przejscie_DO_nowego_rzędu(ile, i):
    a = 450 / ile / 6
    setheading(0)
    pu()
    fd(4 * a)
    lt(90)
    fd(6 * a * (ile - i - 1))
    fd(3 * a)
    pd()


def motyw(ile):
    lewa_str(ile)
    prawa_str(ile)
speed(0)
motyw(4)

done()

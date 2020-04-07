from turtle import *

global a
a = 100


def czworokąt(kąt_a, kąt_b, kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(2):
        fd(a)
        rt(kąt_a)
        fd(a)
        rt(kąt_b)
    end_fill()


def dojscie():
    setheading(0)
    fd(a)
    rt(60)
    fd(a)

def marihuaina():
    pu()
    setpos(0,200)
    dojscie()
    pd()
    for i in range(5):
        czworokąt(30, 150, "darkgreen")
        rt(30)


def zielone_romby():
    pu()
    setpos(0, 200)
    for i in range(4):
        pu()
        setpos(0, 200)
        dojscie()
        setheading(210-60 + 30 * i)
        fd(a)
        lt(30)
        fd(a)
        lt(90)
        pd()
        lt(60)
        pd()
        czworokąt(120, 60, "yellowgreen")


def zolte_kwadraty():
    for i in range(3):
        pu()
        setpos(0,200)
        dojscie()
        setheading(210-60+30*i)
        fd(a)
        for i in range(2):
            lt(30)
            fd(a)
        lt(120)
        pd()
        czworokąt(90,90,"yellow")



def pomaranczowe_romby():
    pu()
    for i in range(2):
        setpos(0, 200)

        dojscie()
        setheading(210-60+30*i)
        for i in range(4):
            fd(a)
            lt(30)
        lt(60)
        pd()
        czworokąt(60,120,"orange")
        pu()

def czerwony_romb():
    rt(60)
    pd()
    czworokąt(150,30,"red")

speed(0)
marihuaina()
zielone_romby()
zolte_kwadraty()
pomaranczowe_romby()
czerwony_romb()
pu()

done()

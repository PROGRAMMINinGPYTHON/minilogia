from turtle import *


def koduj(napis):
    a = 760 / len(napis) / 2
    setpos(-760 / 2, -13 * a / 2)
    napis = list(napis)
    for i in range(len(napis)):
        jedna_litera(napis[i],a)
        if ord(napis[i])-97<13:
            rt(90)
        pu()
        fd(2*a)
        pd()
def jedna_litera(litera, a):
    lt(90)
    pozycja = pos()
    for i in range(13):
        kwadrat("white", a)
        fd(a)
    setpos(pozycja)
    rt(90)
    fd(a)
    lt(90)
    for i in range(13):
        kwadrat("white", a)
        fd(a)
    pu()
    setpos(pozycja)
    pd()
    print(ord('a'))
    if ord(litera) - 97 > 13:
        x = 1
    else:
        x = 0
    if x == 0:
        y = ord(litera) - 97
    else:
        y = 25 - (ord(litera) - 97)
    setheading(90)
    fd(a * y)
    if x == 1:
        rt(90)
        kwadrat("orange", a)
    else:
        kwadrat("orange", a)
    pu()
    setpos(pozycja)
    pd()


def kwadrat(kolor, a):
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()

speed(0)

koduj('abcdmwxyz')
done()

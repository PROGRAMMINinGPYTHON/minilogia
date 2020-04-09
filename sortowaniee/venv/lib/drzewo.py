from turtle import *


def drzewo(ile_gałęzi):
    setpos(0, -300)
    setheading(90)
    color("green")
    for i in range(ile_gałęzi):
        kierunek_rys(i)
        gałąź(ile_gałęzi - i)
        przejscie_do_kolejnej_gałęzi(i, ile_gałęzi)

    if ile_gałęzi % 2 == 0:
        gorna_gałązka_prawa()
        gorna_gałązka_lewa()
    else:
        gorna_gałązka_lewa()
        gorna_gałązka_prawa()


def przejscie_do_kolejnej_gałęzi(ktora_gałąz, ile_wszystkich_gał):
    rt(180)
    fd(20 * ile_wszystkich_gał - (20 * ktora_gałąz))
    setheading(90)
    fd(60)


def kierunek_rys(ktora_gałąź):
    if ktora_gałąź % 2 == 0:
        lt(60)
    else:
        rt(60)


def gorna_gałązka_prawa():
    lt(60)
    fd(20)
    rt(180)
    fd(20)
    setheading(90)
    fd(60)


def gorna_gałązka_lewa():
    rt(60)
    fd(20)
    rt(180)
    fd(20)
    setheading(90)
    fd(60)


def gałąź(ile):
    for i in range(ile):
        fd(20)
        lt(45)
        for k in range(2):
            fd(15)
            rt(30)
            lisc()
            lt(210)
            fd(15)
            rt(45 + 180)
            rt(60)
        rt(60)
        rt(135)


def lisc():
    fillcolor("green")
    begin_fill()
    for j in range(3):
        fd(15)
        lt(120)
    end_fill()


speed(0)
drzewo(9)
done()

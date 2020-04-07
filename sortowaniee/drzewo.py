from turtle import *



def drzewo(ile):
    setpos(0,-250)
    setheading(90)
    color("green")
    for i in range(ile):
        if i % 2 == 0:
            lt(60)
        else:
            rt(60)
        gałąź(ile - i)
        rt(180)
        fd(20 * ile - (20 * i))
        setheading(90)
        fd(60)
    for l in range(1):
        if ile% 2 == 0:
            gorna_gałązka_a()
            gorna_gałązka_b()
        else:
            gorna_gałązka_b()
            gorna_gałązka_a()


def gorna_gałązka_a():
    lt(60)
    fd(20)
    rt(180)
    fd(20)
    setheading(90)
    fd(60)


def gorna_gałązka_b():
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
            fillcolor("green")
            begin_fill()
            for j in range(3):
                fd(15)
                lt(120)
            end_fill()
            lt(210)
            fd(15)
            rt(45 + 180)
            rt(60)
        rt(60)
        rt(135)


speed(0)
drzewo(9)
done()

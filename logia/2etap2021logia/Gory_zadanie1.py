from turtle import *
import math


def schemat(lista):
    for i in range(len(lista)):
        if i == len(lista) - 1:
            x = lista[0]
        else:
            x = lista[i + 1]
        wieza_kwadratow(lista[i])
        if lista[i] > lista[i - 1] and x < lista[i]:
            trojkat_rownoboczny()
        if x > lista[i] and lista[i - 1] <= lista[i]:
            trojkat_prostokatny()
        if lista[i] < x and lista[i] < lista[i - 1]:
            wyciety_kwadrat()
        if lista[i - 1] > lista[i] and x <= lista[i]:
            trojkat_prostokatny_dwa()
        pu()
        setpos(0, 0)
        pd()
        setheading(0)
        fd(50 * i)
        fd(50)


def kwadrat():
    a = 50
    fillcolor("darkgreen")
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()


def wieza_kwadratow(wys):
    a = 50
    for i in range(wys):
        kwadrat()
        lt(90)
        fd(a)
        rt(90)


def trojkat_rownoboczny():
    a = 50
    fillcolor("grey")
    begin_fill()
    for i in range(3):
        fd(a)
        lt(120)
    end_fill()


def wyciety_kwadrat():
    a = 50
    fillcolor("grey")
    begin_fill()
    fd(a)
    lt(90)
    fd(a)
    lt(150)
    fd(a)
    rt(120)
    fd(a)
    lt(150)
    fd(a)
    end_fill()


def trojkat_prostokatny():
    fillcolor("grey")
    a = 50
    begin_fill()
    fd(a)
    lt(90)
    fd(a)
    lt(135)
    fd(a * math.sqrt(2))
    end_fill()


def trojkat_prostokatny_dwa():
    a = 50
    fillcolor("grey")
    begin_fill()
    fd(a)
    lt(135)
    fd(a * math.sqrt(2))
    lt(135)
    fd(a)
    end_fill()

speed(0)
schemat([7,3,3,5,4,7,4,3,9,5,9,4,3,8,6,9,9,9,9,8])
done()
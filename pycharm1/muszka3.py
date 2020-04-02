from turtle import *
import math

global a
a = 7


def figura(ile, jak_wys, left_or_right):
    niebieski(jak_wys)
    lt(135)
    if left_or_right == left:
        left(jak_wys)
    else:
        prawe(jak_wys)


def left(jak_wys):
    for i in range(jak_wys):
        pd()
        kwadrat()
        lt(90)
        fd(a)
        lt(90)
        fd(a)
        rt(180)
        pd()
        kwadrat()


def prawe(jak_wys):
    rt(135)
    fd(a)
    rt(45)
    fd(a)
    lt(90)
    for i in range(jak_wys + 1):
        pd()
        kwadrat()
        pu()
        rt(180)
        fd(a)
        lt(90)
        fd(a)
        lt(90)


def niebieski(jak_wys):
    for i in range(jak_wys):
        pd()
        fillcolor("skyblue")
        begin_fill()
        fd(a)
        lt(45)
        fd(a)
        lt(90)
        fd(a)
        lt(45)
        fd(a)
        lt(45)
        fd(a)
        lt(90)
        fd(a)
        lt(45)
        end_fill()
        pu()
        rt(180)
        rt(45)
        fd(a)
        rt(90)
        fd(a)
        rt(45)


def kwadrat():
    fillcolor("orange")
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()


def kolumny_left(ile, jak_wys):
    for i in range(2):
        pd()
        figura(ile, jak_wys, left)
        pu()
        lt(90)
        fd(a)
        rt(90)
        fd(a)
        lt(45)
        fd(a)
        rt(180)


def kolumny_right(ile, jak_wys):
    for i in range(2):
        pd()
        figura(ile, jak_wys, right)
        pu()
        setheading(45)
        fd(a)
        lt(45)
        fd(a * math.sqrt(2))
        rt(90)


# def right_side(ile, jak_wys):
#     for i in range(ile):
#         kolumny_right(ile, jak_wys + (2 * i))
#         rt(90)
#         fd(a * math.sqrt(2))
#         lt(90)
#
#
# def left_side(ile, jak_wys):
#     for i in range(ile):
#         kolumny_left(ile, jak_wys + (2 * i))
#         rt(90)
#         fd(a * math.sqrt(2))
#         lt(90)


def side(ile, jak_wys, left_or_right):
    for i in range(ile):
        if left_or_right == "left":
            kolumny_left(ile, jak_wys + (2 * i))
        else:
            kolumny_right(ile, jak_wys +(2*i))
        rt(90)
        fd(a * math.sqrt(2))
        lt(90)


def muszka(ile):
    setpos(-a / 2 - (a / 2) * math.sqrt(2), -a * math.sqrt(2))
    side(ile, 2,"left")
    pu()
    setpos((a / 2) * math.sqrt(2), -a * math.sqrt(2))
    setheading(0)
    fd(2 * a)
    side(ile, 2,"right")
    pu()
    setpos(0, 0)
    setheading(-45)
    fd(a)
    lt(90)
    pd()
    kwadrat()
    fd(a)
    rt(90)
    fd(a)
    lt(90)
    kwadrat()


speed(0)
muszka(2)
done()

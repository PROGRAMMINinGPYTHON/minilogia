from turtle import *
global a
a = 20
def pryk():
    fd(4*a)
    rt(90)
    fd(a)
    rt(90)
    fd(4*a)
    lt(90)
    fd(a)
    lt(90)
    fd(4*a)
    rt(90)
    fd(a)
    rt(90)
    fd(4*a)
    lt(90)
    fd(a)
    lt(90)
    fd(4*a)
def nie_wiem():
    for i in range(3):
        if i ==1:
            x = a
        if i == 0:
            x = a
        if i == 2:
            x = 0
        lt(90)
        pryk()
        rt(90)
        fd(a)
        pryk()
        fd(x)
def ZYGZAK():
    pass

nie_wiem()

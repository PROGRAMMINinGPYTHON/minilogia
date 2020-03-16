from turtle import *
def KWIATEK(ile):
    pd()
    color("darkgreen")
    for i in range(ile):
        setheading(360/ile*i)
        for j in range(20):
            fd(30+8*j)
            rt(180)
            fd(30+8*j)
            rt(180)
            rt(360/ile/20)
speed(0)
platek(3)

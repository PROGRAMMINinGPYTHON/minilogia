from turtle import *

def BUKIET(ile,d):
    for j in range(ile):
        setheading((360/ile)*j)
        kwiatek(d)
        pu()
        setpos(0,0)
        pd()

def kwiatek(d):
    fd(200)
    rt(60)
    for i in range(60):
        a = 80-(d*i)
        if a<10:
            break
        fd(a)
        rt(60)
        print(a)
speed(0)
BUKIET(6,1)

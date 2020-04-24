from turtle import *
global a
a = 448/16
def BLOK():
    bez_przejsc()
    przejscie(448/16)


def klatka():
    for i in range(3):
        okno()
        setheading(180)
        pu()
        fd(2*a)
        fd(a/4)
        rt(90)
        fd(0.75*a)
        pd()
        if i== 1:
            setheading(0)
            pu()
            fd(a/2)
            rt(270)
            pd()
    for i in range(1):
        pu()
        rt(90)
        fd(0.5*a)
        lt(90)
        pd()
        okno()
    rt(180)
    pu()
    fd(1.75*a)
    rt(90)
    fd(0.75*a)
    pd()
    okno()

def bez_przejsc():
    for i in range(4):
        pu()
        setpos(-11*a+(6*a*i),-8*a+4*a)
        pd()
        klatka()


def okno():
    a = 448/16
    for i in range(3):
        for j in range(4):
            rt(90)
            for k in range(4):
                kwadrat(a)
                lt(90)
                fd(a)
                rt(90)
        fd(a)
        rt(90)
        fd(3*a)
        rt(180)
        a = a/2
    fillcolor("darkblue")
    begin_fill()
    a = 448/16
    for i in range(4):
        fd(a/2)
        rt(90)
    end_fill()
        
def kwadrat(a):
    fillcolor("orange")
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()

def przejscie(a):
    for i in range(3):
        pu()
        setpos(-7*a+(6*a*i),-5*a)
        pd()
        for i in range(3):
            setheading(0)
            fd(a)
            lt(90)
            kwadrat(a)
            rt(90)
            fd(a)
            lt(90)
            kwadrat(a)
            fd(a)
            fillcolor("darkblue")
            begin_fill()
            for i in range(4):
                fd(2*a)
                lt(90)
            end_fill()
            setheading(90)
            fd(2*a)
            lt(90)
            fd(2*a)
        setheading(0)
        fd(a)
        lt(90)
        kwadrat(a)
        rt(90)
        fd(a)
        lt(90)
        kwadrat(a)
        
speed(0)
BLOK()



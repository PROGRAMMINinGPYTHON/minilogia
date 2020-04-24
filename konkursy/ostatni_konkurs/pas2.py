from turtle import *
global a
a = 8
def sześciokąt(kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(6):
        fd(a)
        lt(360/6)
    end_fill()

def segment_srodek(ile):
    for j in range(ile):
        for i in range(ile):
            sześciokąt("orange")
            fd(a)
            lt(60)
            fd(a)
            lt(60)
            fd(a)
            lt(60)
            fd(a)
            rt(180)
        rt(120)
        pu()
        for i in range(ile):
            fd(a)
            lt(60)
            fd(a)
            rt(60)
        lt(120)
        fd(a)
        rt(60)
        fd(a)
        lt(60)
        pd()


def ramka_segmentu(ile):
    rt(60)
    fd(16)
    lt(120)
    for d in range(2):
        for j in range(2):
            for i in range(ile+2):
                sześciokąt("darkgreen")
                fd(a)
                lt(60)
                fd(a)
                lt(60)
                fd(a)
                lt(60)
                fd(a)
                rt(180)
            rt(120)
            fd(a)
            lt(60)
        fd(a)
        lt(60)
        fd(a)
        lt(60)
        fd(a)
        rt(180)
        rt(60)
        fd(a)
        setheading(150)
        fd(a)
        rt(180)
        rt(120)
        rt(180)
        fd(a)
        rt(180)
def segment(ile):
    segment_srodek(ile)
    ramka_segmentu(ile)

def pas(ile_segmentów,jak_duze):
    setpos(-500,0)
    for i in range(ile_segmentów):
        segment(jak_duze)
        setheading(90)
        fd(a)
        rt(60)
        for j in range(jak_duze):
            fd(a)
            lt(60)
            fd(a)
            rt(60)
        fd(a)
        rt(60)
        fd(a)
        setheading(-90)
        fd(8)
        setheading(330)

speed(0)
rt(30)
pas(1,1)
done()

from turtle import *
global a
a = 22
def pieciokąt():
    fillcolor("skyblue")
    begin_fill()
    for i in range(5):
        fd(a)
        rt(360/5)
    end_fill()

def koło():
    for i in range(10):
        pieciokąt()
        for i in range(2):
            fd(a)
            rt(360/5)
        rt(180)
        rt(360/5)

def kwiat():
    pu()
    setpos(100,50)
    pd()
    setheading(180-90)
    for i in range(10):
        pd()
        koło()
        for j in range(4):
            pu()
            fd(a)
            lt(360/10)
        lt(360/5)
        lt(180)

speed(0)
kwiat()
done()
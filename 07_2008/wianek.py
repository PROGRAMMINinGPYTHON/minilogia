from turtle import *
global a
a = 70
def WIANEK():
    wianek_start()



def kwadrat():
    fillcolor("skyblue")
    begin_fill()
    for i in range(4):
        fd(a)
        rt(90)
    end_fill()

def romb_zolty():
    fillcolor("yellow")
    begin_fill()
    for i in range(2):
        fd(a)
        lt(180)
        rt(150)
        fd(a)
        lt(180)
        rt(30)
    end_fill()

def romb_zielony():
    fillcolor("yellowgreen")
    begin_fill()
    for i in range(2):
        fd(a)
        rt(180+120)
        fd(a)
        rt(180+60)
    end_fill()

def wianek_start():
    for i in range(6):
        setheading(60)
        rt(60*i)
        pu()
        fd(a)
        pd()
        setheading(180)
        rt(60*i)
        fd(a)
        rt(180)
        romb_zolty()
        lt(30)
        romb_zielony()
        fd(a)
        lt(60)
        kwadrat()
        pu()
        setpos(0,0)
        pd()
WIANEK()



from turtle import *
global a
a = 40

def powrot():
    for i in range(2):
        setheading(135)
        fd(a)
        lt(45)
        fd(a)
        
def KWADRATY():
    for i in range(5):
        if i%2 == 0:
            rząd_a()
            powrot()
        else:
            rząd_b()
            rt(180)
            fd(a)
            rt(90)
            powrot()
            setheading(-90)
            fd(a)

def rząd_a():
    for i in range(2):    
        setheading(90)
        kwadrat()
        setheading(0)
        fd(a)
        lt(90)
        romb()
        rt(180)
        fd(a)
    setheading(90)
    kwadrat()

def rząd_b():
    for i in range(2):
        setheading(0)
        romb()
        setheading(0)
        fd(a)
        rt(135)
        fd(a)
        rt(180)
        kwadrat()
        setheading(-45)
        fd(a)
        lt(90)
        fd(a)
    rt(45)
    romb()

def romb():
    color("black")
    fd(a)
    rt(135)
    fd(a)
    rt(180)
    lt(135)
    fd(a)
    rt(135)
    fd(a)
    
def kwadrat():
    color("black")
    fillcolor("grey")
    begin_fill()
    for i in range(4):
        fd(a)
        rt(90)
    end_fill()

speed(0)
KWADRATY()

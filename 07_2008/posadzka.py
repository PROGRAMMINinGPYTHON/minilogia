from turtle import *

def POSADZKA(n):
    a = 400/n/4
    pu()
    setpos(-200,-200)
    pd()
    for j in range(n):
        pu()
        setpos(-200,-200+4*a*j)
        pd()
        for i in range(n):
            if(j+i)%2 == 0:
                kafelek(n,"skyblue")
            else:
                kafelek(n,"orange")

def rząd(n):
    a = 400/4/n
    for i in range(n):
        if x+i/2 == 0:
            kol = "skyblue"
        else:
            kol = "orange"
        kafelek(n,kol)
            
def kafelek_1(n,kol):
    a = 400/n/4
    pd()
    kwadrat(n,kol,a)
    setheading(0)
    pu()
    fd(3*a)
    pd()
    kwadrat(n,kol,a)
    fd(a)
    lt(90)
    pu()
    fd(3*a)
    lt(90)
    fd(a)
    rt(90)
    pd()

def kafelek_2(n,kol):
    a = 400/n/4
    kwadrat(n,kol,a)
    pu()
    rt(180)
    fd(3*a)
    rt(90)
    kwadrat(n,kol,a)
    fd(a)
    rt(90)
    fd(2*a)
    kwadrat(n,kol,2*a)

def kafelek(n,kol):
    a = 400/n/4
    kafelek_1(n,kol)
    kafelek_2(n,kol)
    rt(90)
    fd(a)
    lt(90)
    fd(3*a)
    
def kwadrat(n,kol,bok):
    a = 400/n/4
    fillcolor(kol)
    begin_fill()
    color(kol)
    setheading(0)
    for i in range(4):
        fd(bok)
        lt(90)
    end_fill()

speed(0)
POSADZKA(15)


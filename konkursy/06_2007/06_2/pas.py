from turtle import *

def rząd(n):
    a = 700/n/4
    kolek(n)
    setheading(0)
    pu()
    fd(4*a)
    pd()

def PAS(n):
    pas_gora(n)
    pas_dol(n)
    
def pas_dol(n):
    a = 700/n/4
    for j in range(3):
        pu()
        setpos(-350-2*a,(7.5*a)-4*a*j)
        pd()
        for i in range(n):
            rząd(n)

def pas_gora(n):
    a = 700/n/4
    for j in range(3):
        pu()
        setpos(-350,6.5*a-4*a*j)
        pd()
        for i in range(n):
            rząd(n)
def kolek(n):
    fillcolor("grey")
    begin_fill()
    kolek_cz_1(n)
    kolek_cz_2(n)
    end_fill()
def kolek_cz_1(n):
    a = 700/n/4
    setheading(0)
    fd(3*a)
    rt(90)
    fd(a)
    rt(90)
    fd(a)
    lt(90)
    fd(a)
    lt(90)
    fd(a)
    rt(90)
    fd(a)
    rt(90)
    fd(a)
    lt(90)

def kolek_cz_2(n):
    a = 700/n/4
    fd(a)
    rt(90)
    fd(a)
    rt(90)
    fd(a)
    lt(90)
    fd(a)
    rt(90)
    fd(a)
    rt(90)
    fd(a)
    lt(90)
    fd(a)
    lt(90)
    fd(a)
    rt(90)
    fd(a)
    
speed(0)
PAS(7)

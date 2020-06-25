from turtle import *
import  math

def PASEK(n):
    a = 700 / (6 + n * 10)
    przejscie_pasek_jeden(n)
    pd()
    diament(n)
    przejscie_pasek_dwa(n)
    pd()
    rządek(n)
    koniec(n)
    pd()
    diament(n)

def przejscie_pasek_jeden(n):
    a = 700 / (6 + n * 10)
    pu()
    setpos(-350,-100)
    setheading(0)
    fd(a)
    rt(90)
    fd(a)
    lt(135)

def przejscie_pasek_dwa(n):
    a = 700 / (6 + n * 10)
    setheading(45)
    pu()
    fd(2*a*math.sqrt(2))
    rt(135)
    fd(2*a)
    lt(90)
    fd(8*a)

def diament(n):
    a = 700/(6+n*10)
    fillcolor("yellowgreen")
    begin_fill()
    fd(2*a*math.sqrt(2))
    lt(90)
    fd(2*a*math.sqrt(2))
    lt(90)
    fd(a*math.sqrt(2))
    lt(45)
    fd(2*a)
    lt(45)
    fd(a*math.sqrt(2))
    end_fill()

def portal(n):
    a = 700/(6+n*10)
    for i in range(2):
        lt(45)
        diament(n)
        lt(90)
        fd(2*a*math.sqrt(2))
        lt(90)
        fd(2*a*math.sqrt(2))
        rt(45)
        fd(2*a)
        lt(45)
        fd(a*math.sqrt(2))
        lt(90)
        diament(n)
        lt(90)
        fd(a*4*math.sqrt(2))
        lt(180)
        diament(n)
        rt(180)
        fd(a*math.sqrt(2))
        lt(90)
        diament(n)
        lt(45)

def przejscie(n):
    a = 700/(6+n*10)
    setheading(0)
    fd(10*a)

def rządek(n):
    for i in range(n):
        portal(n)
        pu()
        przejscie(n)
        pd()

def koniec(n):
    a = 700/(6+n*10)
    rt(180)
    pu()
    fd(6*a)
    rt(90)
    fd(4*a)
    lt(135)
speed(0)
PASEK(2)
done()
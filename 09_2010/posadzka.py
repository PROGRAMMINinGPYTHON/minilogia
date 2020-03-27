from turtle import *
import math
def POSADZKA(n):
    a = 460/n/3/2
    for i in range(n):
        pu()
        setpos(-230,-230+(6*a*i))
        pd()
        double_shit(n)      

    
def double_shit(n):
    a = 460/n/3/2
    rządek_2(n)
    pu()
    dojscie(n)
    lt(90)
    fd(2*a)
    lt(90)
    fd(6*a*n)
    for i in range(n*3):
        gora(n)
def dojscie(n):
    a = 460/n/3/2
    lt(90)
    fd(2*a)
    lt(90)
    fd(6*a*n)
    rząd(n)    

    
def kafelek_1(n):
    a = 460/n/4/3
    pd()
    polowa_1(n,"purple","yellow")
    polowa_1(n,"yellow","purple")

def rząd(n):
    for i in range(n*3):
        kafelek_1(n)
    
def polowa_1(n,kol,kol_2):
    a = 460/n/4/3
    setheading(0)
    color(kol)
    fillcolor(kol)
    begin_fill()
    fd(2*a)
    lt(90)
    fd(4*a)
    lt(90)
    fd(2*a)
    lt(90)
    fd(4*a)
    end_fill()
    rt(180)
    fd(2*a)
    rt(135)
    fillcolor(kol_2)
    begin_fill()
    color(kol_2)
    for i in range(4):
        fd(a*math.sqrt(2))
        lt(90)
    end_fill()
    przejscie(n)

def przejscie(n):
    a = 460/n/3/2/2
    setheading(-90)
    fd(2*a)
    lt(90)
    pu()
    fd(2*a)

def dolny_i_gorny_rząd(n,x):
    a = 460/n/3/2
    setheading(0)
    color("purple")
    fillcolor("purple")
    begin_fill()
    for i in range(4):
        fd(2*a)
        lt(90)
    end_fill()
    setheading(x-90)
    fd(a)
    lt(90)
    color("yellow")
    fillcolor("yellow")
    begin_fill()
    fd(a)
    rt(90)
    fd(a)
    rt(90)
    fd(a)
    rt(135)
    fd((a/2)*math.sqrt(2))
    lt(90)
    fd((a/2)*math.sqrt(2))
    end_fill()
    setheading(x)
    fd(a)
    rt(45)

def dodatek(n):
    a = 460/n/3/2
    fillcolor("yellow")
    begin_fill()
    fd((a/2)*math.sqrt(2))
    lt(90)
    fd((a/2)*math.sqrt(2))
    lt(45)
    fd(a)
    lt(90)
    fd(a)
    lt(45)
    fd((a/2)*math.sqrt(2))
    lt(90)
    fd((a/2)*math.sqrt(2))
    end_fill()
    setheading(-90)
    fd(a)
    lt(90)
    fd(a)

def gora(n):
    a = 460/n/3/2
    fillcolor("purple")
    begin_fill()
    setheading(90)
    for i in range(4):
        fd(2*a)
        rt(90)
    end_fill()
    setheading(90)
    fillcolor("yellow")
    begin_fill()
    fd(a)
    rt(45)
    fd((a/2)*math.sqrt(2))
    rt(90)
    fd(a*math.sqrt(2))
    rt(90)
    fd((a/2)*math.sqrt(2))
    rt(45)
    fd(a)
    end_fill()
    rt(180)
    fd(2*a)
    lt(90)
    fd(a)
    setheading(0)
    rt(180)
    fd(a)
    rt(180)
    fillcolor("yellow")
    begin_fill()
    fd(a)
    lt(90)
    fd(a)
    lt(135)
    fd((a/2)*math.sqrt(2))
    rt(90)
    fd((a/2)*math.sqrt(2))
    lt(135)
    fd(a)
    lt(90)
    fd(a)
    end_fill()
    setheading(-90)
    fd(a)
        
def rządek_2(n):
    for i in range(n*3):
        dolny_i_gorny_rząd(n,90)
        dodatek(n)
speed(0)        
POSADZKA(2)      




    

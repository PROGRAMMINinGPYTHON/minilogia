from turtle import *
global c
c = 35
global a
a = 2*c
global b
b = 10
speed(0)
def sciana(x,y):
    pu()
    setpos(x,y)
    setheading(90)
    pd()
    fd(a)
    rt(90)
    fd(2*a)
    rt(90)
    fd(2*a)
    rt(90)
    fd(a*2)
    rt(90)
    fd(1*a)

def oczko(x,y):
    setpos(x,y)
    fd(b)
    rt(90)
    fillcolor("black")
    begin_fill()
    pd()
    fd(b)
    rt(90)
    fd(2*b)
    rt(90)
    fd(2*b)
    rt(90)
    fd(2*b)
    rt(90)
    fd(b)
    end_fill()

def aaa ():
    sciana(0,0)
    pu()
    oczko(a,0)

def bbb ():
    sciana(-2*a,0)
    pu()
    oczko(-3*c,-c)
    pu()
    oczko(-3*c,c)
    pu()
    oczko(-c,c)
    pu()
    oczko(-c,-c)
def ccc():
    sciana(-8*c,0)
    pu()
    oczko(-7*c,-c)
    pu()
    oczko(-7*c,c)
    pu()
    oczko(-5*c,c)
    pu()
    oczko(-5*c,-c)
    pu()
    oczko(-6*c,c)
    pu()
    oczko(-6*c,-c)
def ddd():
    sciana(4*c,0)
    pu()
    oczko(6*c,0)
    pu()
    oczko(5*c,-c)
    pu()
    oczko(7*c,c)
def eee():
    sciana(0,4*c)
    pu()
    oczko(2*c,4*c)
    pu()
    oczko(c,3*c)
    pu()
    oczko(c,5*c)
    pu()
    oczko(3*c,3*c)
    pu()
    oczko(3*c,5*c)
def fff():
    sciana(0,-4*c)
    pu()
    oczko(c,-3*c)
    pu()
    oczko(3*c,-5*c)
    
   
def KOSTKA():
    aaa()
    pu()
    bbb()
    pu()
    ccc()
    pu()
    ddd()
    eee()
    fff()
KOSTKA()   

    

from turtle import *
global a
a = 20
def LABIRYNT(n):
    slimak(n)
    ramka(n)

def slimak_rt(n,x):
    setheading(x)
    for i in range(n):
        fd((n*2)*a-(2*a*i))
        rt(90)
        fd((n*2)*a-(2*a*i))
        rt(90)
        fd(((n*2*a)-(2*a))-(2*a*i))
        if i == n-1:
            pu()
        rt(90)
        fd(2*a)
        lt(90)
        fd(a)
        rt(90)
        fd((n*2*a-(3*a))-2*a*i)
        rt(90)

def slimak_lt(n,x):
    setheading(x)
    for i in range(n):
        fd((n*2)*a-(2*a*i))
        lt(90)
        fd((n*2)*a-(2*a*i))
        lt(90)
        fd(((n*2*a)-(2*a))-(2*a*i))
        if i == n-1:
            pu()  
        lt(90)
        fd(2*a)
        rt(90)
        fd(a)
        lt(90)
        fd((n*2*a-(3*a))-2*a*i)
        lt(90)

def slimak(n):
    pu()
    setpos(-(a/2),(n*2)*a+a/2)
    pd()
    slimak_rt(n,-90)
    pu()
    setpos((a/2),(n*2)*a+a/2)
    pd()
    slimak_lt(n,-90)
    pu()
    setpos(-(a/2),-((n*2)*a+a/2))
    pd()
    slimak_lt(n,90)
    pu()
    setpos((a/2),-((n*2)*a+a/2))
    pd()
    slimak_rt(n,90)

def ramka(n):
    pu()
    setpos(0,0)
    setheading(-90)
    fd((n*2)*a+a/2)
    pd()
    setheading(0)
    for i in range(2):
        fd(((((n*2*a)+a/2))-1*a)*1)
        lt(90)
        fd(a)
        rt(90)
        fd(2*a)
        lt(90)
        fd(((((n*2*a)+a/2))-1*a)*2)
        lt(90)
        fd(2*a)
        rt(90)
        fd(a)
        lt(90)
        fd(((((n*2*a)+a/2))-1*a)*1)
    
    
    


speed(0)
LABIRYNT(3)

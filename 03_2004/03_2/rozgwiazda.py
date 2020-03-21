from turtle import *
def ROZGWIAZDA(n):
    zegarek(n)

def trojkat(kolor,n):
    a =100/n
    fillcolor(kolor)
    begin_fill()
    for i in range(3):
        fd(a)
        lt(120)
    end_fill()

def gwiazda(n):
    a = 100/n
    for i in range(6):
        setheading(30+60*i)
        trojkat("green",n)
    for i in range(6):
        setheading(90+60*i)
        fd(a)
        rt(120)
        trojkat("yellow",n)
        rt(60)
        fd(a)
        
def zegarek(ile):
    a = 100/ile
    for i in range(6):
        pu()
        setpos(0,0)
        pd()
        setheading(90+60*i)
        for j in range(ile+1):
            gwiazda(ile)
            setheading(90+60*i)
            pu()
            fd(3*a)
            pd()
speed(0)
ROZGWIAZDA(10)


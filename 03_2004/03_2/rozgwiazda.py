from turtle import *

def ROZGWIAZDA(n):
    pass

def trojkat(kolor):
    a = 50
    fillcolor(kolor)
    begin_fill()
    for i in range(3):
        fd(a)
        lt(120)
    end_fill()

def gwiazda():
    for i in range(6):
        setheading(90+60*i)
        trojkat("yellowbrown")
        
def zegarek():
    for i in range(6):
        pu()
        setpos(0,0)
        setheading(90+60*i)

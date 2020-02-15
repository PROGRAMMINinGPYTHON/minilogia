from turtle import *
from random import *

def losowyKolor():
    kolory = ["#ffffff", "#222222", "#333333", "#444444", "#aaaaaa", "#123456"]
    return kolory[randrange(len(kolory))]
    

global a
a = 100
def lopata():
    fd(2*a)
    rt(90)
    begin_fill()
    fillcolor(losowyKolor())
    fd(a/2)
    lt(90)
    fd(a)
    lt(90)
    fd(a)
    lt(90)
    fd(a)
    lt(90)
    fd(a)
    end_fill()
    pu()
    setpos(0,0)
    
def Wiatraki(n):
    for i in range(n):
        setheading(360/n*i)
        pd()
        lopata()

speed(0)        
Wiatraki(10)
    

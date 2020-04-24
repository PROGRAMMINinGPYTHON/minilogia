from turtle import *

def NASZYJNIK(ile):
    for i in range(ile):
        kulki(0+i*360/ile)
        rt(360/ile)
        fd(40)
        

def kulki(kierunek):
    setheading(kierunek)
    rt(90)
    circle(20)
    lt(90)
    fd(55)
    rt(90)
    circle(15)
    rt(90)
    fd(60)
speed(0)    
NASZYJNIK(5)

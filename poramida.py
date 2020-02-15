from turtle import *
import math
a = 20
def skok(ile):
    pu()
    setheading(180)
    fd(40*ile)
    setheading(90)
    fd(20)
    rt(30)
    fd(40)
    pd()
    
def figura ():
    fillcolor("darkgreen")
    color("darkgreen")
    begin_fill()
    setheading(0)
    pd()
    fd(2*a)
    lt(90)
    fd(a)
    lt(30)
    fd(2*a)
    lt(120)
    fd(a*2)
    lt(30)
    fd(a)
    lt(90)
    fd(a)
    end_fill()
    setheading(0)
    fd(a)
def rządek(ile):
    for i in range(ile):
        pd()
        figura()
def piramida(ile):
    setpos(-(2*ile*a)/2,-(1+math.sqrt(3)))
    pd()
    for i in range(ile):
        rządek(ile-i)
        skok(ile-i)
        
piramida(2)
setpos(0,0)
fillcolor("black")
begin_fill()
#circle(10)
end_fill()

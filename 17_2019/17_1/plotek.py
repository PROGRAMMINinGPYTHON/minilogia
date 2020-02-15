from turtle import *
import math
def deska(kolor,n):
    a = 760/n/4
    fillcolor(kolor)
    begin_fill()
    setheading(0)
    fd(2*a)
    lt(90)
    fd(10*a)
    lt(45)
    fd(a*math.sqrt(2))
    lt(90)
    fd(a*math.sqrt(2))
    lt(45)
    fd(10*a)
    end_fill()
    
def deski(n):
    a = 760/n/4
    for i in range(n):
        if i == 0:
            kol ="green"
            
        if i == 1:
            kol = "red"
            
        if i == 2:
            kol = "green"
            
        if i ==3:
            kol ="red"
            
        if i == 4:
            kol = "green"
            
        if i == 5:
            kol = "red"
            
        if i ==6:
            kol ="green"
            
        if i == 7:
            kol ="red"
            
        if i == 8:
            kol ="green"

        if i ==9:
            kol ="red"
            
        if i == 10:
            kol ="green"
            
        if i == 11:
            kol ="red"
               
        if i == 12:
            kol ="green"

        if i ==13:
            kol ="red"
            
        if i == 14:
            kol ="green"

        if i == 15:
            kol ="red"

        if i == 16:
            kol = "green"
            
        if i ==17:
            kol ="red"
            
        if i == 18:
            kol = "green"
            
        if i == 19:
            kol = "red"
            
        if i ==20:
            kol ="green"
            
        if i == 21:
            kol ="red"
            
        if i == 22:
            kol ="green"

        if i ==23:
            kol ="red"
            
        if i == 24:
            kol ="green"
            
        if i == 25:
            kol ="red"
               
        if i == 26:
            kol ="green"

        if i ==27:
            kol ="red"
            
        if i == 28:
            kol ="green"
            
        if i == 29:
            kol ="red"

        if i == 30:
            kol ="green"
        deska(kol,n)
        pu()
        setheading(0)
        fd(a*4)
        pd()
        
def plot(n):
    a = 760/n/4
##    for i in range(int(n/2)):
    for i in range(1):
        deski(n)

def plotek(n):
    a = 760/n/4
    pu()
    setpos(-380,-200)
    setheading(0)
    fd(a)
    pd()
    plot(n)
    end_fill()
    pu()
    setpos(-380,-200)
    setheading(90)
    fd(a)
    rt(90)
    pd()
    fillcolor("red")
    begin_fill()
    color("red")
    fd(760)
    lt(90)
    fd(2*a)
    lt(90)
    fd(760)
    lt(90)
    fd(2*a)
    end_fill()
    pu()
    setpos(-380,-200)
    setheading(90)
    fd(7*a)
    pd()
    rt(90)
    pd()
    fillcolor("red")
    color("red")
    begin_fill()
    fd(760)
    lt(90)
    fd(2*a)
    lt(90)
    fd(760)
    lt(90)
    fd(2*a)
    end_fill()
speed(0)
plotek(10)



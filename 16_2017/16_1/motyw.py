from turtle import *
global a
a = 420/28
print(a)
def motyw():
    pass

def kwadrat_mini():
    fillcolor("yellow")
    begin_fill()
    setheading(0)
    fd(a)
    lt(90)
    fd(a)
    lt(90)
    fd(a)
    lt(90)
    fd(a)
    end_fill()
    setheading(0)
def kwadrat_xxl():
    fillcolor("darkgreen")
    begin_fill()
    setheading(0)
    fd(2*a)
    lt(90)
    fd(2*a)
    lt(90)
    fd(2*a)
    lt(90)
    fd(2*a)
    end_fill()

def zielone_pole():

    setpos(-6.5*a,-6.5*a)
    for j in range(7):
        pu()
        setpos(-6.5*a,-6.5*a+2*a*j)
        pd()
        for i in range(7):
            kwadrat_xxl()
            setheading(0)
            fd(2*a)


zielone_pole()
            

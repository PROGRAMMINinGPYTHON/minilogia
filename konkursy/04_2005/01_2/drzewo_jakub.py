from turtle import *
from random import *

global a
global b
global x
global y

def podstawa():
    global a,b,x,y
    pu()
    setpos(x, y)
    pd()
    fillcolor("black")
    begin_fill()
    setpos(x+2*a, y)
    setpos(x+2*a, y+b)
    setpos(x,y+b)
    setpos(x,y)
    end_fill()
    pu()
    setpos(x-b, y+b)
    begin_fill()
    setpos(x+2*a+b, y+b)
    setpos(x+2*a+b, y+b+a)
    setpos(x-b, y+b+a)
    setpos(x-b, y+b)
    end_fill()
    
def praweL(x,y, wys, kolor):
    pu()
    setpos(x,y)
    pd()
    color(kolor, kolor)
    begin_fill()
    setpos(x, y+wys)
    setpos(x+wys, y+wys)
    setpos(x+wys, y+wys-a)
    setpos(x+a, y+wys-a)
    setpos(x+a, y)
    setpos(x,y)
    end_fill()

def leweL(x,y, wys, kolor):
    pu()
    setpos(x,y)
    pd()
    color(kolor, kolor)
    begin_fill()
    setpos(x, y+wys)
    setpos(x-wys, y+wys)
    setpos(x-wys, y+wys-a)
    setpos(x-a, y+wys-a)
    setpos(x-a, y)
    setpos(x,y)
    end_fill()    

def prawyLisc(x,y):
    global a
    praweL(x,y,4*a, "black")
    praweL(x+a,y,3*a, "green")
    praweL(x+2*a, y, 2*a, "red")
    praweL(x+3*a, y, a, "yellow")

def lewyLisc(x,y):
    global a
    leweL(x,y,4*a, "black")
    leweL(x-a,y,3*a, "green")
    leweL(x-2*a, y, 2*a, "red")
    leweL(x-3*a, y, a, "yellow")    

def wierzcholek(y):
    prawyLisc(x+a,y)

def galazP(y, dl):
    for i in range(dl):
        prawyLisc(x+a + i*4*a, y)

def galazL(y, dl):
    for i in range(dl):
        lewyLisc(x+a - i*4*a, y)        

def DRZEWO(ile, dl):
    global a,b,x,y
    a = 100/(ile+2)
    b = 3*a
    x = -a
    y = -200
    podstawa()

    for i in range(ile):
        if i%2==0:
            galazP(y+(i+1)*4*a, 1)
            galazL(y+(i+1)*4*a, randrange(2, dl+1))
        else:
            galazP(y+(i+1)*4*a, randrange(2, dl+1))
            galazL(y+(i+1)*4*a, 1)
    wierzcholek(y+b+a+ile*4*a)

DRZEWO(5, 6)
    

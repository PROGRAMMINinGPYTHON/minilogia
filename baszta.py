from turtle import *

def baszta (a,x,y):
    pu()
    setpos(x,y)
    pd()
    begin_fill()
    fillcolor("brown")
    setpos(x+5*a,y)
    setpos(x+5*a,y+1*a)
    setpos(x+4*a,y+1*a)
    setpos(x+4*a,y+8*a)
    setpos(x+5*a,y+8*a)
    setpos(x+5*a,y+10*a)
    setpos(x+4*a,y+10*a)
    setpos(x+4*a,y+9*a)
    setpos(x+3*a,y+9*a)
    setpos(x+3*a,y+10*a)
    setpos(x+2*a,y+10*a)
    setpos(x+2*a,y+9*a)
    setpos(x+1*a,y+9*a)
    setpos(x+1*a,y+9*a)
    setpos(x+1*a,y+10*a)
    setpos(x,y+10*a)
    setpos(x,y+8*a)
    setpos(x+1*a,y+8*a)
    setpos(x+1*a,y+1*a)
    setpos(x,y+1*a)
    setpos(x,y)
    end_fill()
    
    
#baszta(10,0,0)

def baszty(ile):
    wysokosc = 405
    a = 45
    x = 0
    y = 0

    for i in range(ile):
        baszta(a, x, y)
        wysokosc = 9*a
        x = x + 6*a
        y = y + a
        a = (wysokosc -  3*a) // 9
        print("a: ", a, " i: ", i)
        

speed(0)
baszty(12)
pu()
setpos(0, 0)

    
    


from turtle import *

def kwadrat(x, y, a, kolor):
    pu()
    setpos(x, y)
    pd()
    color("black", kolor)
    begin_fill()

    setpos(x+a, y)
    setpos(x+a, y+a)
    setpos(x, y+a)
    setpos(x,y)

    end_fill()
    

def SZACH(n):
    bok = 400
    a = bok / n

    przelacznik = 1

    poczX = -bok/2
    poczY = -bok/2

    for y in range(n):
        for x in range(n):
            if (przelacznik % 2 ==0):
                kwadrat(poczX + x*a, poczY + y*a, a, "white")
            else:
                kwadrat(poczX + x*a, poczY + y*a, a, "blue")
            przelacznik = przelacznik + 1

        przelacznik = przelacznik + 1
            
                    

SZACH(4)

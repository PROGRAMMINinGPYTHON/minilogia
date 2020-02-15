from turtle import *

kratka = 30

startx = -1
starty = -7

def prostokat(x, y, a, b, kolor):
    pu()
    setposition((x + startx) * kratka, (y + starty) * kratka)
    color(kolor)
    fillcolor(kolor)
    pd()
    begin_fill()
    seth(0)
    fd(a * kratka)
    lt(90)
    fd(b * kratka)
    lt(90)
    fd(a * kratka)
    lt(90)
    fd(b * kratka)
    end_fill()
    pu()

def robot():
#    setposition(-1 * kratka, -7 * kratka)
    lewa_noga()
    prawa_noga()
    tulow()
    lewa_reka()
    prawa_reka()
    glowa()

def lewa_noga():
    print("lewa_noga")
    prostokat(0, 0, 2, 1, "green")
    prostokat(0, 1, 1, 5, "orange")

def prawa_noga():
    print("prawa_noga")
    prostokat(4, 2, 2, 1, "green")
    prostokat(4, 3, 1, 3, "orange")
    prostokat(2, 5, 2, 1, "orange")
    
def tulow():
    print("tulow")
    prostokat(0, 6, 3, 5, "orange")
    

def lewa_reka():
    print("lewa_reka")
    prostokat(-3, 10, 3, 1, "orange")
    prostokat(-3, 8, 1, 2, "orange")
    prostokat(-3, 7, 1, 1, "green")

def prawa_reka():
    print("prawa_reka")
    prostokat(3, 10, 3, 1, "orange")
    prostokat(5, 11, 1, 2, "orange")
    prostokat(5, 13, 1, 1, "green")
    

def glowa():
    print("glowa")
    prostokat(0, 12, 3, 3, "orange")
    prostokat(1, 11, 1, 1, "orange")
    prostokat(3, 13, 1, 1, "green")

robot()

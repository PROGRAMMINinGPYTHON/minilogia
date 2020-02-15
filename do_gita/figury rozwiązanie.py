from turtle import *


kratka = 10

def czworokat(a):
    pu()
    setpos(-a, 0)
    pd()
    setpos(0, 2*a)
    setpos(4*a, 0)
    setpos(0, -3*a)
    setpos(-a, 0)

    
def rysuj_czworokaty():
   # for kaczka in range(1, 5):
   #    czworokat(kaczka*kratka)
   czworokat(1*kratka)
   czworokat(2*kratka)
   czworokat(3*kratka)
   czworokat(4*kratka)

def rysuj_gwiazdki():
    pozycje = ((2,8), (11, 3), (-7, 6), (-9, 5), (-8, -5), (-7, -10))
    for pozycja in pozycje:
        gwiazdka(pozycja[0]*kratka, pozycja[1]*kratka)
        
##    gwiazdka(2*kratka, 8*kratka)
##    gwiazdka(11*kratka, 3*kratka)
##    gwiazdka(-7*kratka, 6*kratka)
##    gwiazdka(-9*kratka, 5*kratka)
##    gwiazdka(-8*kratka, -5*kratka)
##    gwiazdka(-7*kratka, -10*kratka)

def gwiazdka(x, y):
    pu()
    setpos(x, y)
    pd()
    setpos(x+2*kratka, y)
    setpos(x+4*kratka, y-1*kratka)
    setpos(x+1*kratka, y+4*kratka)
    setpos(x, y)

rysuj_czworokaty()
rysuj_gwiazdki()

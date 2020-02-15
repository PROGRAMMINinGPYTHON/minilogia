from turtle import *
a=20
##def linia(x,y):
##    print("p")
##    setposition(x+10*a,y)
##    setposition(x+10*a,y+1*a)
##    setposition(x+9*a,y+1*a)
##    setposition(x+9*a,y)
##linia(1,1)   
speed(20)
def rysujPogrubione(rozmiar, kratka):
    pu()
    poczatkowaGrubosc = width()
    width(50)
    setpos(0, -rozmiar*kratka)
    pd()
    setpos(0, rozmiar*kratka)
    pu()
    setpos(-rozmiar*kratka, 0)
    pd()
    setpos(rozmiar*kratka, 0)
    width(poczatkowaGrubosc)

def rysujPionowe(rozmiar, kratka): 
    
    for x in range(-rozmiar, rozmiar):
        pu()
        setpos(x*kratka, -rozmiar*kratka)
        pd()
        setpos(x*kratka, rozmiar*kratka)
        
rysujPionowe(30,900)
rysujPogrubione(190,910)
##def rysujPoziome(rozmiar, kratka):
##    print("todo")
##    for x in range (-rozmiar,rozmiar):
##        pu()
##        setpos(-rozmiar,-rozmiar)
##        pd()
##        setpos(-rozmiar,-rozmiar)
##
##def rysujCienkie(rozmiar, kratka):
##    rysujPionowe(rozmiar, kratka)
##    rysujPoziome(rozmiar, kratka)
##
##def rysujUklad(wielkosc, kratka):
##    rysujPogrubione(wielkosc, kratka)
##    rysujCienkie(wielkosc, kratka)
##
##
##rysujUklad(20, 20)


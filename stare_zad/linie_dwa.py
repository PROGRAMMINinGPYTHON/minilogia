from turtle import *

def l_pionowe(ilosc,odle,wys):
    width(1)
    for i in range(-ilosc,ilosc):
        pu()
        setpos(odle*i,-wys)
        pd()
        setpos(odle*i,wys)
        pu()

def l_poziome(ilosc,odle,dlug):
    width(1)
    for z in range(-ilosc,ilosc):
        pu()
        setpos(-dlug,odle*z)
        pd()
        setpos(dlug,odle*z)

def l_gruba(grubosc,dlugosc):
    pu()
    width(grubosc)
    setpos(-dlugosc,0)
    pd()
    setpos(dlugosc,0)
    pu()
    setpos(0,-dlugosc)
    pd()
    setpos(0,dlugosc)
    
speed(0)
def rysuj_uklad(odleglosc,ilosc,grubosc):
    ilosc*odleglosc=dlugosc
    l_gruba(grubosc,dlugosc)
    l_pionowe(ilosc,odleglosc,dlugosc)
    l_poziome(ilosc,odleglosc,dlugosc)

rysuj_uklad(5,5,5)

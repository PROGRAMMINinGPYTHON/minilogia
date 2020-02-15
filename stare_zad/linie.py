from turtle import *
def l_pionowe(ilosc,odleg):
    for i in range (-ilosc+1,ilosc):
        pu()
        setpos(i*odleg,-odleg*ilosc)
        pd()
        setpos(i*odleg,odleg*ilosc)
def l_poziome(ilosc,odleg):
    for i in range(-ilosc+1,ilosc):
        pu()
        setpos(-odleg*ilosc,i*odleg)
        pd()
        setpos(odleg*ilosc,i*odleg)

def l_grube(szer,dlug):
    width(szer)
    pu()
    setpos(0,0)
    setpos(dlug,0)
    pd()
    setpos(-dlug,0)
    setpos(0,0)
    setpos(0,dlug)
    setpos(0,-dlug)
    
        
def rys_uklad(szer,ilosc,odleg):
    l_poziome(ilosc,odleg)
    l_pionowe(ilosc,odleg)
    l_grube(szer,ilosc*odleg)
speed(0)        
rys_uklad(3,5,40)

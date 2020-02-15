from turtle import *
global kratka
kratka= 20
def figura(kratka):
    pu()
    setposition(-1*kratka,+0)
    pd()
    setpos(0-0,+2*kratka)
    setpos(+4*kratka,0)
    setpos(0+0,-3*kratka)
    setpos(-1*kratka,0+0)
    pu()
figura(kratka)
figura(2*kratka)
figura(3*kratka)
pu
figura(4*kratka)
pu()

def gwiazdka(x,y):
    pu()
    setpos(x-2*kratka,y)
    pd()
    setpos(x-1*kratka,y+4*kratka)
    setpos(x+2*kratka,y-1*kratka)
    setpos(x,y)
    setpos(x-2*kratka,y)
    pu()
gwiazdka(4*kratka,8*kratka)
gwiazdka(13*kratka,3*kratka)
gwiazdka(-5*kratka,6*kratka)
gwiazdka(-7*kratka,5*kratka)
gwiazdka(-6*kratka,-5*kratka)
gwiazdka(-5*kratka,-10*kratka)

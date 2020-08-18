from turtle import *
import math
def ośmiokąt(jak_duży):
    fillcolor("white")
    begin_fill()
    for i in range(8):
        fd(jak_duży)
        rt(45)
        print(pos())
    end_fill()

def przejscie(jak_duzy_osmiokąt):
    pu()
    fd(jak_duzy_osmiokąt/2)
    rt(45)
    fd(jak_duzy_osmiokąt/2)
    lt(90)
    fd(jak_duzy_osmiokąt/2)
    rt(45)
    pd()

def zielony_kwadrat():
    pass

def rządek(jak_długi,jak_duży_osmiokąt):
    for i in range(jak_długi):
        ośmiokąt(jak_duży_osmiokąt)
        przejscie(jak_duży_osmiokąt)

def rama(jak_duża,jak_duzy_osmiokąt):
    for i in range(1):
        rządek(jak_duża,jak_duzy_osmiokąt)
        rt(180)
        fd(2*jak_duzy_osmiokąt)
speed(0)
ośmiokąt(64)
done()

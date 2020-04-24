from turtle import *
import math
def gowno(kolor_gowna,ile):
    a = 500/(ile+1)
    fillcolor(kolor_gowna)
    begin_fill()
    fd(a)
    lt(135)
    fd(a/2*math.sqrt(2))
    lt(90)
    fd(a/2*math.sqrt(2))
    end_fill()
    lt(135)
    fd(a)

def papier_toaletowy(ile_rolek_XD):
    a = 500/(ile_rolek_XD+1)
    pu()
    setpos(-250,-150)
    pd()
    setheading(0)
    fillcolor("yellow")
    begin_fill()
    pu()
    fd(2*a)
    lt(90)
    fd(a)
    lt(90)
    fd(2*a)
    lt(90)
    fd(a)
    pd()
    end_fill()
    
def sraka_na_papierze_toaletowym(ile_SRAKI):
    a = 500/(ile_SRAKI+1)
    print(a)
    pu()
    setpos(-250,-150)
    pd()
    setheading(0)
    for i in range(ile_SRAKI):
        gowno("orange",ile_SRAKI)
    lt(90)
    fd(a)
    lt(90)
    for i in range(ile_SRAKI):
        gowno("orange",ile_SRAKI)
    lt(90)
    fd(a)
    
def KORONA(ile):
    podarty_papier_toaletowy_na_gorze_rysunku(ile)
    #papier_toaletowy(ile)
    sraka_na_papierze_toaletowym(ile)
    wystający_kibel(ile)
    spłukanie_kibla(ile)

def wystający_kibel(jak_wielka_SRAKA):
    pu()
    setpos(-250,-150)
    pd()
    setheading(90)
    gowno("yellowgreen",jak_wielka_SRAKA)

def podarty_papier_toaletowy_na_gorze_rysunku(jak_duzo_SRAJTAŚEMKI):
    a = 500/(jak_duzo_SRAJTAŚEMKI+1)
    pu()
    setpos(-250,-150)
    pd()
    setheading(90)
    fillcolor("yellow")
    begin_fill()
    fd(300)
    rt(135)
    for i in range(jak_duzo_SRAJTAŚEMKI):
        pd()
        fd(a/math.sqrt(2))
        lt(90)
        fd(a/math.sqrt(2))
        rt(90)
    rt(45)
    fd(300)
    rt(90)
    fd(350)
    end_fill()

def spłukanie_kibla(x):
    a = 500/(x+1)
    rt(90)
    fd(x*a)
    rt(90)
    gowno("yellowgreen",x)
    
speed(0)
KORONA(5)


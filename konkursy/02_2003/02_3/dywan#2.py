from turtle import *
import math
global a
a = 320/18



def ramka_dół():
    pu()
    setpos(-26*a/2,-320/2)
    pd()
    setheading(0)
    fillcolor("skyblue")
    begin_fill()
    color("skyblue")
    for i in range(2):
        fd(26*a)
        lt(90)
        fd(a)
        lt(90)
    end_fill()

def ramka_lewy_bok():
    pu()
    setpos(-26*a/2,-320/2)
    pd()
    setheading(90)
    fillcolor("skyblue")
    begin_fill()
    color("skyblue")
    for i in range(2):
        fd(320)
        rt(90)
        fd(a)
        rt(90)
    end_fill()

def ramka_góra():
    pu()
    setpos(-26*a/2,160)
    pd()
    fillcolor("skyblue")
    begin_fill()
    color("skyblue")
    setheading(0)
    for i in range(2):
        fd(26*a)
        rt(90)
        fd(a)
        rt(90)
    end_fill()

def ramka_prawa_strona():
    pu()
    setpos(26*a/2,160)
    pd()
    fillcolor("skyblue")
    begin_fill()
    color("skyblue")
    setheading(270)
    for i in range(2):
        fd(320)
        rt(90)
        fd(a)
        rt(90)
    end_fill()

def ramka():
    ramka_dół()
    ramka_góra()
    ramka_lewy_bok()
    ramka_prawa_strona()

def srodkowy_krzyz():
    pu()
    setpos(0,0)
    setheading(180)
    fd(1.5*a)
    pd()
    color("yellow")
    lt(90)
    fd(0.5*a)
    fillcolor("yellow")
    begin_fill()
    lt(90)
    fd(a)
    rt(90)
    fd(a)
    lt(90)
    fd(a)
    lt(90)
    fd(a)
    rt(90)
    fd(a)
    lt(90)
    fd(a)
    lt(90)
    fd(a)
    rt(90)
    fd(a)
    lt(90)
    fd(a)
    lt(90)
    fd(a)
    rt(90)
    fd(a)
    end_fill()

def kwadrat_najmniejszy(kolor):
    fillcolor(kolor)
    begin_fill()
    color(kolor)
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()

def ramka_srodkowego_kwadratu():
    pu()
    setpos(-6*a,-6*a)
    pd()
    fillcolor("skyblue")
    begin_fill()
    color("skyblue")
    setheading(90)
    for i in range(4):
        fd(12*a)
        rt(90)
    setheading(90)
    fd(0.5*a)
    setheading(0)
    fd(0.5*a)
    for i in range(4):
        fd(11*a)
        lt(90)
    end_fill()

def zółte_tło_srodkowego_kwadratu():
    pu()
    setpos(-6*a,-6*a)
    pd()
    setheading(0)
    fillcolor("yellow")
    begin_fill()
    for i in range(4):
        fd(12*a)
        lt(90)
    end_fill()

def środkowy_kwadrat():
    zółte_tło_srodkowego_kwadratu()
    srodkowy_krzyz()
    pu()
    setpos(2.5*a,0.5*a)
    romby()

def żółte_tło():
    pu()
    setpos(-26*a/2+a,-320/2+a)
    pd()
    fillcolor("yellow")
    color("yellow")
    begin_fill()
    setheading(0)
    fd(26*a-(2*a))
    lt(90)
    fd(320-2*a)
    lt(90)
    fd(26*a-(2*a))
    end_fill()

def romby():
    for i in range(4):
        if i%2 == 0:
            x="skyblue"
        else:
            x = "blue"
        romb_z_rządków(i+3,x)
        lt(180)
        pu()
        fd(a)
        rt(180)
        pd()

def srodek_kwadratu():
    pu()
    setpos(0,0)

def romb_z_rządków(ile,kol):
    for i in range(4):
        rządek(ile,kol)
        lt(180)
        fd(a)
        rt(270)

def rządek(ile,kol):
    for i in range(ile):
        kwadrat_najmniejszy(kol)
        fd(a)
        lt(90)
        pu()
        fd(a)
        rt(90)
        pd()

def szlaczek_częsc_ręczna_początek():
        fillcolor("darkblue")
        begin_fill()
        color("darkblue")
        setheading(45)
        fd(2*a*math.sqrt(2))
        rt(135)
        fd(4*a)
        rt(135)
        fd(2*a*math.sqrt(2))
        end_fill()
        rt(135)
        fd(2*a)

def szlaczek_częsc_automatyczna():
    for i in range(5):
        fillcolor("darkblue")
        begin_fill()
        rt(45)
        fd(2*a*math.sqrt(2))
        lt(90)
        fd(2*a*math.sqrt(2))
        lt(45)
        fd(2*a)
        lt(135)
        fd(2*a*math.sqrt(2))
        rt(90)
        fd(2*a*math.sqrt(2))
        lt(135)
        fd(2*a)
        end_fill()
        przejscie()
        rt(45)

def szlaczek_część_ręczna_koniec():
    fillcolor("darkblue")
    begin_fill()
    color("darkblue")
    lt(90)
    fd(2*a)
    rt(135)
    fd(2*a*math.sqrt(2))
    rt(90)
    fd(2*a*math.sqrt(2))
    rt(135)
    fd(2*a)
    end_fill()

def szlaczek_gorny():
    szlaczek_częsc_ręczna_początek()
    szlaczek_częsc_automatyczna()
    szlaczek_część_ręczna_koniec()

def przejscie():
    lt(45)
    fd(2*a*math.sqrt(2))
    lt(90)
    fd(2*a*math.sqrt(2))

def szlaczki_gora():
    for i in range(2):
        pu()
        setpos(-13*a+a,(320/2)-3*a-(4*a*i))
        pd()
        szlaczek_gorny()

def szlaczek_dolny():
    pu()
    szlaczek_dół_recznie()
    for i in range(5):
        szlaczek_dół_automotycznie()
    setheading(90)
    szlaczek_doł_koniec()

def szlaczek_doł_koniec():
    setheading(90)
    pd()
    fillcolor("darkblue")
    color("darkblue")
    begin_fill()
    fd(2*a)
    rt(135)
    fd(2*a*math.sqrt(2))
    rt(90)
    fd(2*a*math.sqrt(2))
    rt(135)
    fd(2*a)
    end_fill()

def szlaczki_dolne():
    for i in range(2):
        pu()
        setpos(-12*a,-160+3*a+(4*a*i))
        pd()
        szlaczek_dolny()

def szlaczek_dół_recznie():
    fillcolor("darkblue")
    color("darkblue")
    begin_fill()
    setheading(45)
    fd(2*a*math.sqrt(2))
    rt(135)
    fd(4*a)
    rt(135)
    fd(2*a*math.sqrt(2))
    rt(135)
    pu()
    fd(2*a)
    end_fill()
    lt(45)

def szlaczek_dół_automotycznie():
    fillcolor("darkblue")
    begin_fill()
    color("darkblue")
    fd(2*a*math.sqrt(2))
    rt(90)
    fd(2*a*math.sqrt(2))
    rt(45)
    fd(2*a)
    rt(135)
    fd(2*a*math.sqrt(2))
    lt(90)
    fd(2*a*math.sqrt(2))
    rt(135)
    fd(2*a)
    end_fill()
    pu()
    setheading(0)
    fd(4*a)
    lt(45)

def szlaczki_wszystkie():
    szlaczki_gora()
    szlaczki_dolne()

def DYWAN():
    ramka()
    żółte_tło()
    szlaczki_wszystkie()
    środkowy_kwadrat()
    ramka_srodkowego_kwadratu()


speed(0)
DYWAN()
pu()
setpos(0,0)
done()

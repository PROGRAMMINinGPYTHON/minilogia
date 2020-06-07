from turtle import *
global a
a = 20

def płatek(kol):
    fillcolor(kol)
    begin_fill()
    fd(2*a)
    lt(60)
    fd(a)
    lt(60)
    fd(a)
    lt(60)
    fd(a)
    lt(60)
    fd(2*a)
    end_fill()

def kwiatek(kol_1,kol_2):
    for i in range(6):
        setheading(90-(60*i))
        if i%2 == 0:
            kol = kol_1
            płatek(kol)
        else:
            kol = kol_2
            płatek(kol)

def przejscie_do_niebieskiego_i_zielonego():
    pu()
    setpos(0,0)
    fd(2*a)
    rt(60)
    fd(a)
    lt(60)
    fd(2*a)

def zielony_kwiatek():
    kwiatek("darkgreen","yellowgreen")

def zółty_kwiatek():
    kwiatek("yellow","orange")

def niebieski_kwiatek():
    kwiatek("skyblue","darkblue")

def niebieskie_i_zielone():
    pu()
    setpos(0,0)
    for i in range(6):
        setheading(90-(60*i))
        przejscie_do_niebieskiego_i_zielonego()
        pd()
        if i%2 == 0:
            zielony_kwiatek()
        else:
            niebieski_kwiatek()

def zółte():
    pu()
    setpos(0,0)
    pd()
    zółty_kwiatek()
    pu()

def BUKIET():
    niebieskie_i_zielone()
    zółte()

speed(0)
BUKIET()
setpos(0,0)
done()
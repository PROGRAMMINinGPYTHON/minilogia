from turtle import *

a = 26



def s_gora(x, y):
    penup()
    setposition(x     * a, y     * a)
    fillcolor("green")
    pendown()
    begin_fill()
    setposition((x+1) * a, (y)   * a)
    setposition((x+1) * a, (y+2) * a)
    setposition((x)   * a, (y+1) * a)
    setposition((x) * a, (y) * a)
    end_fill()
    pendown()

def narusujStrzalkeWdol(x, y):
    penup()
    setposition(x     * a, y     * a)
    fillcolor("green")
    pendown()
    begin_fill()
    setposition((x+1)* a, (y+1)*a)
    setposition((x+1)*a, (y+2) *a)
    setposition(x * a, (y+2) * a)
    setposition(x*a, y*a)
    end_fill()
    pendown()

def wiatraki(ile):
    for x in range(ile):
        trzy_wiatraki(x * 4)

def trzy_wiatraki(pozycja_duzego):
    wiatrak(pozycja_duzego - 2, 3)
    wiatrak(pozycja_duzego, 8)
    wiatrak(pozycja_duzego + 2, 3)

def wiatrak(x, wysokosc):
    lodyga(x, wysokosc)
    s_gora(x, wysokosc + 1)
    narusujStrzalkeWdol(x-1, wysokosc-1)
    narusujStrzalkeWlewo(x, wysokosc+1)
    narusujStrzalkeWprawo(x,wysokosc)



def lodyga(x, wysokosc):
    penup()
    setposition(x*a ,0)
    pendown()
    setposition(x * a, wysokosc * a)
    penup()
    
def narusujStrzalkeWlewo(x, y):
    penup()
    setposition(x     * a, y     * a)
    fillcolor("orange")
    pendown()
    begin_fill()
    setposition((x-1)* a, y*a)
    setposition((x-2) * a, (y+1) *a)
    setposition (x * a, (y+1) * a)
    setposition(x*a, y*a)
    end_fill()
    pendown()

def narusujStrzalkeWprawo(x, y):
    penup()
    setposition(x     * a, y     * a)
    fillcolor("orange")
    pendown()
    begin_fill()
    setposition(x* a, (y+1)*a)
    setposition((x+1) * a, (y+1) *a)
    setposition ((x +2)* a, y * a)
    setposition(x*a, y*a)
    end_fill()
    pendown()

    
speed(1)
wiatraki(2)

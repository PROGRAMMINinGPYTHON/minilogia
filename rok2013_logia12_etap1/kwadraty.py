from turtle import *
import math

def kwadraty(jak_wielkie):
    a = jak_wielkie/11
    print(a)

def kwadrat(kol,jak_w):
    a  = jak_w/11
    setheading(0)
    fillcolor(kol)
    begin_fill()
    fd(a)
    rt(90)
    fd(a)
    rt(90)
    fd(a)
    rt(90)
    fd(a)
    end_fill()

def rząd(jak_w):
    a = jak_w/11
    for i in range(7):
        kwadrat("red",jak_w)
        pu()
        setheading(90)
        fd(a)
        pd()

def srodek_mini(jak_w):
    a = jak_w/11
    pu()
    setpos(0,0)
    setheading(135)
    fd(a/2*math.sqrt(2))
    pd()
    kwadrat("red",jak_w)
    pu()
    lt(45)
    fd(a*math.sqrt(2))
    pd()
    kwadrat("skyblue",jak_w)
    pu()
    setheading(-45)
    fd(2*a*math.sqrt(2))
    pd()
    kwadrat("skyblue",jak_w)
    fd(2*a)
    kwadrat("skyblue",jak_w)
    setheading(-135)
    pu()
    fd(2*a*math.sqrt(2))
    pd()
    kwadrat("skyblue",jak_w)
    
def srodek_big(jak_w):
    a = jak_w/11
    pu()
    setpos(0,0)
    setheading(180)
    fd(3.5*a)
    rt(90)
    fd(1.5*a)
    pd()
    setheading(0)
    kwadraty(jak_w)
    rt(90)
    fd(2*a)
    lt(90)
    fd(2*a)
    rt(90)
    kwadraty(jak_w)
    setheading(-45)
    pu()
    fd(2*a*math.sqrt(2))
    pd()
    setheading(0)
    kwadraty(jak_w)
    setheading(-135)
    pu()
    fd(2*a*math.sqrt(2))
    pd()
    setheading(0)
    kwadraty(jak_w)

def mini_rząd(jak_w):
    a = jak_w/11
    for i in range(3):
        pd()
        kwadrat("skyblue",jak_w)
        pu()
        fd(a)
        rt(90)

def kwadraty(jak_w):
    a = jak_w/11
    fd(3*a)
    rt(90)
    fd(3*a)
    rt(90)
    fd(3*a)
    rt(90)
    fd(3*a)

def cztery_trójki(jak_w):
    a = jak_w/11
    lt(90)
    pu()
    fd(2*a)
    pd()
    mini_rząd(jak_w)
    pu()
    fd(2*a)
    lt(90)
    fd(a)
    for i in range(3):
        pd()
        kwadrat("skyblue",jak_w)
        pu()
        rt(90)
        fd(a)
    rt(45)
    fd(2*a*math.sqrt(2))
    rt(45)
    fd(2*a)
    rt(90)
    fd(a)
    mini_rząd(jak_w)
    rt(135)
    fd(6*a*math.sqrt(2))
    setheading(0)
    fd(2*a)
    lt(90)
    fd(a)
    for i in range(3):
        pd()
        kwadrat("skyblue",jak_w)
        rt(90)
        pu()
        fd(a)

def srodek_(jak_w):
    srodek_mini(jak_w)
    srodek_big(jak_w)
    cztery_trójki(jak_w)

def czerwony_kwadrat(jak_w):
    a = jak_w/11
    fillcolor("red")
    begin_fill()
    setheading(0)
    fd(2*a)
    rt(90)
    fd(2*a)
    rt(90)
    fd(2*a)
    rt(90)
    fd(2*a)
    end_fill()

def rogi(jak_w):
    a = jak_w/11
    pu()
    setpos(-3.5*a,3.5*a)
    pd()
    czerwony_kwadrat(jak_w)
    pu()
    setpos(1.5*a,3.5*a)
    pd()
    czerwony_kwadrat(jak_w)
    pu()
    setpos(1.5*a,-1.5*a)
    pd()
    czerwony_kwadrat(jak_w)
    pu()
    setpos(-3.5*a,-1.5*a)
    pd()
    czerwony_kwadrat(jak_w)
    pu()

def linie(jak_w):
    a = jak_w/11
    fd(7*a)
    rt(90)
    fd(a)
    rt(90)
    fd(7*a)
    rt(90)
    fd(a)

    
def ramka(jak_w):
    a = jak_w/11
    pu()
    setpos(-3.5*a,4.5*a)
    setheading(0)
    pd()
    linie(jak_w)
    pu()
    setpos(-3.5*a,-3.5*a)
    pd()
    setheading(0)
    linie(jak_w)
    pu()
    setpos(-4.5*a,-3.5*a)
    pd()
    setheading(90)
    linie(jak_w)
    pu()
    setpos(3.5*a,-3.5*a)
    pd()
    setheading(90)
    linie(jak_w)
    mini_kwadraty(jak_w)

def mini_kwadraty(jak_w):
    a = jak_w/11
    kwadrat("skyblue",jak_w)
    fd(8*a)
    kwadrat("skyblue",jak_w)
    setheading(180)
    pu()
    fd(8*a)
    pd()
    kwadrat("skyblue",jak_w)
    rt(180)
    fd(8*a)
    kwadrat("skyblue",jak_w)

def czerwone_rządki_wys(jak_w):
    a = jak_w/11
    for i in range(7):
        kwadrat("red",jak_w)
        pu()
        fd(a)
        pd()
        
def czerwone_rządki_szer(jak_w):
    a = jak_w/11
    for i in range(7):
        kwadrat("red",jak_w)
        setheading(0)
        pu()
        fd(a)
        pd()
        
def rama(jak_w):
    a = jak_w/11
    pu()
    setpos(-5.5*a,-2.5*a)
    pd()
    czerwone_rządki_wys(jak_w)
    pu()
    setpos(4.5*a,-2.5*a)
    pd()
    czerwone_rządki_wys(jak_w)
    lt(90)
    fd(8*a)
    rt(90)
    fd(a)
    czerwone_rządki_szer(jak_w)
    pu()
    setpos(-3.5*a,-4.5*a)
    pd()
    czerwone_rządki_szer(jak_w)
    

speed(0)
rogi(400)
srodek_(400)
ramka(400)
rama(400)

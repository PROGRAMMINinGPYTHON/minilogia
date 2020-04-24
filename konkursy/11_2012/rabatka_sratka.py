from turtle import *


def RABATKA(ilek,ilep):
    a  = 460/ilek/2/8
    pu()
    setpos(-460/2,-230/2)
    pd()
    łodygi(ilek,ilep)
def łodygi(ilek,ilep):
    for i in range(ilek):
        color("green")
        setheading(90)
        fd(115)
        gowno(ilek,ilep)
        color("green")
        setheading(-90)
        fd(115)
        lt(90)
        fd(460/ilek/2)
        lt(90)
        fd(230)
        gowno(ilek,ilep)
        color("green")
        setheading(-90)
        fd(230)
        lt(90)
        fd(460/ilek/2)
        lt(90)
        fd(115)
        gowno(ilek,ilep)
        setheading(-90)
        fd(115)
        
def gowno(ilek,ilep):
    a  = 460/ilek/2/8
    for i in range(ilep):
        setheading(-90+360/ilep/2)
        lt(360/ilep*i)
        color("purple")
        fd(a)
        rt(90)
        platek(ilek,ilep)         
    
def platek(ilek,ilep):
    a  = 460/ilek/2/8
    for i in range(ilep):
        color("purple")
        fillcolor("purple")
        begin_fill()
        fd(1.5*a/2)
        lt(30)
        fd(1.5*a)
        rt(180+60)
        fd(1.5*a)
        lt(30)
        fd(1.5*a)
        lt(30)
        fd(1.5*a)
        rt(180+60)
        fd(1.5*a)
        lt(30)
        fd(0.75*a)
        end_fill()
        lt(90)
        pu()
        fd(1.5*a)
        rt(90)
        pd()
    rt(90)
    fd((1.5*a*ilep)+a)
speed(0)

RABATKA(2,3)  

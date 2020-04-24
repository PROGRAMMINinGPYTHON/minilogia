from turtle import *

def RABATKA(ilek,ilep):
    pass

def platek(ilek,ilep):
    a = 460/ilek/2/8
    for i in range(ilep):
        fillcolor("purple")
        color("purple")
        begin_fill()
        fd(1.5*a)
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
        end_fill()
        lt(30)
        lt(90)
        pu()
        fd(1.5*a)
        rt(90)
        pd()
def glowa(ilek,ilep):
    a = 460/ilek/2/8
    for i in range(ilep):
        setheading((360/ilep)*i)
        fd(a)
        lt(90)
        pu()
        fd(0.75*a)
        rt(180)
        pd()
        platek(ilek,ilep)
        rt(90)
        fd((1.5*a*ilep))
        lt(90)
        fd(0.75*a)
        rt(90)
        fd(a)
        
        
def łodygi(ilek,ilep):
    for i in range(1):
        color("yellowgreen")
        setheading(90)
        fd(115)
        glowa(ilek,ilep)
        rt(180)
        fd(115)
        lt(90)
        fd(460/ilek/2)
        lt(90)
        fd(230)
        glowa(ilek,ilep)
        rt(180)
        fd(230)
        lt(90)
        fd(460/ilek/2)
        lt(90)
        fd(115)
        glowa(ilek,ilep)
        rt(180)
        fd(115)
speed(0)
łodygi(1,3)

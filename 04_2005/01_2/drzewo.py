from turtle import *
from random import *
def DRZEWO(ile,dl):
    gałąź(ile,dl)
    liść(ile,dl)
    pieniek(ile,dl)

def gałąź_krotka(ile,dl):
    a = 400/(ile+2)/5
    rt(360)
    leaf(ile,dl)

def gałąź_dluga(ile,dl):
    a = 400/(ile+2)/5
    liczba_lisci = randrange(2,dl+1)
    for i in range(liczba_lisci):
        leaf(ile,dl)
        pu()
        setheading(0)
        fd(6*a)        

def leaf(ile,dl):
    a = 400/(ile+2)/5
    liść_part_one(ile,dl)
    leaf_part_two(ile,dl)
    leaf_part_three(ile,dl)
    
def liść_part_one(ile,dl):
    a = 400/(ile+2)/5
    color("yellow")
    begin_fill()
    fillcolor("yellow")
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    lt(90)
    fillcolor("red")
    begin_fill()
    color("red")
    fd(a)
    rt(90)
    fd(a)
    lt(90)
    fd(a)
    lt(90)
    fd(2*a)
    lt(90)
    fd(2*a)
    lt(90)
    fd(a)
    end_fill()

def leaf_part_two(ile,il):
    a = 400/(ile+2)/5
    rt(180)
    fd(a)
    fillcolor("yellowgreen")
    begin_fill()
    color("yellowgreen")
    rt(90)
    fd(2*a)
    rt(90)
    fd(2*a)
    lt(90)
    fd(a)
    lt(90)
    fd(3*a)
    lt(90)
    fd(3*a)
    lt(90)
    fd(a)
    end_fill()

def leaf_part_three(ile,dl):
    a = 400/(ile+2)/5
    rt(180)
    fd(a)
    fillcolor("black")
    color("black")
    begin_fill()
    rt(90)
    fd(3*a)
    rt(90)
    fd(3*a)
    lt(90)
    fd(a)
    lt(90)
    fd(4*a)
    lt(90)
    fd(4*a)
    lt(90)
    fd(a)
    end_fill()

def pieniek(ile,dl):
    a = 400/(ile+2)/5
    pu()
    fillcolor("black")
    begin_fill()
    setpos(-a,-200)
    pd()
    setheading(0)
    fd(2*a)
    lt(90)
    fd(3*a)
    lt(90)
    fd(2*a)
    lt(90)
    fd(3*a)
    end_fill()

def dolna_gałąź(ile,dl):
    a = 400/(ile+2)/5
    pu()
    setpos(-4*a,-200+3*a)
    pd()
    setheading(0)
    fillcolor("black")
    begin_fill()
    fd(8*a)
    lt(90)
    fd(a)
    lt(90)
    fd(8*a)
    lt(90)
    fd(a)
    end_fill()

def piętra(ile,dl):
    a = 400/(ile+2)/5
    setpos(3*a,-200+4*a)
    for i in range(ile+1):
        if i%2 == 0:
            setheading(0)
            gałąź_krotka(ile,dl)
        else:
            pu()
            setpos(3*a,-200+8*a)
            gałąź_dluga(ile,dl)
        
        
speed(0)   
piętra(2,7)

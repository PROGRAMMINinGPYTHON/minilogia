from turtle import *
import math
def kafelek(ile):
    długosc = 480/2/ile
    c = 1*math.sqrt(2)*100/ile
    b = długosc-c
    a = c/2
    fillcolor("yellow")
    begin_fill()
    for i in range(4):
        fd(długosc*2-2)
        lt(90)
    end_fill()
    setheading(45)
    fd(b)
    setheading(0)
    background_red(ile)
    lt(45)
    fd(długosc*2*math.sqrt(2)-b-3)
    lt(135)
    fd(długosc*2-2)
    lt(135)
    fd(długosc*2*math.sqrt(2)-3)
    lt(45)

def rządek(ile):
    długosc = 480/2/ile
    c = 1*math.sqrt(2)*100/ile
    b = długosc-c
    a = c/2
    for i in range(ile):
        kafelek(ile)

def part1(ile):
    długosc = 480/2/ile
    c = 1*math.sqrt(2)*100/ile
    b = długosc-c
    a = c/2
    fillcolor("red")
    begin_fill()
    for i in range(4):
        fd(b)
        lt(90)
    end_fill()
    fd(b)
    rt(45)

def part2(ile):
    długosc = 480/2/ile
    c = 1*math.sqrt(2)*100/ile
    b = długosc-c
    a = c/2
    fillcolor("red")
    begin_fill()
    fd(b)
    lt(135)
    fd(b)
    lt(45)
    fd(b)
    lt(135)
    fd(b)
    end_fill()
    lt(45)
    fd(b)

def part3(ile):
    długosc = 480/2/ile
    c = 1*math.sqrt(2)*100/ile
    b = długosc-c
    a = c/2
    lt(135)
    fillcolor("red")
    begin_fill()
    fd(b)
    rt(45)
    fd(b)
    rt(135)
    fd(b)

def part4(ile):
    długosc = 480/2/ile
    c = 1*math.sqrt(2)*100/ile
    b = długosc-c
    a = c/2
    rt(45)
    fd(b)
    end_fill()
    rt(135)
    fd(b)
    rt(45)
    fd(b)
    rt(45)
    fillcolor("red")
    begin_fill()
    rt(90)
    for i in range(4):
        fd(b)
        lt(90)
    end_fill()

def red(ile):
    długosc = 480/2/ile
    c = 1*math.sqrt(2)*100/ile
    b = długosc-c
    a = c/2
    part1(ile)
    part2(ile)
    part3(ile)
    part4(ile)

def kratka(ile):
    długosc = 480/2/ile
    c = 1*math.sqrt(2)*100/ile
    b = długosc-c
    a = c/2
    for i in range(ile):
        rządek(ile)
        pu()
        setpos(-240,-240+(długosc*2*(i+1)-3*(i+1)))

        pd()
def background_red(ile):
    długosc = 480/2/ile
    c = 1*math.sqrt(2)*100/ile
    b = długosc-c
    a = c/2
    for i in range(4):
        red(ile)
        fd(b)
        lt(90)
        fd(b)
        lt(90)

speed(0)
setpos(-480/2,-480/2)
kratka(2)
done()
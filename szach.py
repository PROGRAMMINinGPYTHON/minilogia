from turtle import *
def szach(n):
    a=400/n
    setheading(180)#szachownica ma 400x400
    fd(200)
    lt(90)
    fd(200)
    lt(90)
    fd(400)
    lt(90)
    fd(400)
    lt(90)
    fd(400)
    lt(90)
    fd(400)
    setheading(0)
    for i in range(n):
        fd(a)
        lt(90)
        fd(400)
        rt(180)
        fd(400)
        lt(90)
    lt(90)
    for i in range(n):
        fd(a)
        lt(90)
        fd(400)
        rt(180)
        fd(400)
        lt(90)
speed(0)
szach(4)


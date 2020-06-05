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



def BUKIET():
    pass

kwiatek("yellow","orange")
done()
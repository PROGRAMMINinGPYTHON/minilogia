from turtle import *
def prostokąt(kol):
    fillcolor(kol)
    begin_fill()
    for i in range(2):
        fd(40)
        rt(90)
        fd(20)
        rt(90)
    end_fill()
prostokąt("blue")
done()
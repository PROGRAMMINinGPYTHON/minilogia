from turtle import *
global a
a = 20

def pięciokąt():
    for i in range(5):
        fd(a)
        lt(72)

def przejscie_w_kwiatku():
    fd(a)
    rt(72)

def kwiatek():
    lt(36)
    for i in range(5):
        pięciokąt()
        przejscie_w_kwiatku()

def przejscie_do_kwiatka():

    lt(72)
    fd(a)
    lt(216)
    fd(a)
    lt(72)
    fd(a)
    lt(72)
    # fd(a)
    rt(72)
    fd(a)
    rt(36)

def dwa_gowna():
    kwiatek()
    przejscie_do_kwiatka()
    kwiatek()
def ramka():
    pass

dwa_gowna()
done()
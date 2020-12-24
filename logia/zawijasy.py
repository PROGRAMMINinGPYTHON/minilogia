from turtle import *

def jeden_zawijas(litera, a):
    alfabet = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 2, "g": 3, "h": 4, "i": 5, "j": 5, "k": 6, "l": 3, "m": 4,
               "n": 5, "o": 6, "p": 7, "q": 4, "r": 5, "s": 6, "t": 7, "u": 8,
               "v": 5, "w": 6, "x": 7, "y": 8, "z": 9}
    for i in range(alfabet[litera]):
        pd()
        fd(a)
        lt(90)
        a = a - 4
    pu()

def koduj(napis):
    a = 780 / len(napis)
    napis = list(napis)
    print(napis)
    pu()
    setpos(-780 / 2, -a / 2)
    pd()
    for i in range(len(napis)):
        print(napis[i])
        jeden_zawijas(napis[i],a)
        pu()
        setpos(-780 / 2, -a / 2)
        setheading(0)
        fd(a*(i+1)+a/10*(i+1))
        pd()

speed(0)
koduj("abcdefghijklmnopqrstuwxyz")
done()

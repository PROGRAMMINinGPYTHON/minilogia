from turtle import *


def szyfruj(napis):
    napis = list(napis)
    print(napis)
    a = 700 / len(napis)
    setpos(-350 + a, -2.5 * a)
    print(a)
    for i in range(len(napis)):
        jedna_litera(napis[i], a)
        pu()
        setpos(-350 + a, -2.5 * a)
        setheading(0)
        fd(a * i + 1 * a)
        pd()


def kwadrat(kolor, a):
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()


def jedna_litera(litera, a):
    # ta mapa jest zdecydowanie do zmiany , caly alfabet musze wpisac , trzeba jakos inaczej
    kazda_litera = {"A": ["a", "a", "a", "a", "a"], "B": ["a", "a", "a", "a", "b"], "C": ["a", "a", "a", "b", "a"],
                    "D": ["a", "a", "a", "b", "b"], "E": ["a", "a", "b", "a", "a"],
                    "F": ["a", "a", "b", "a", "b"], "G": ["a", "a", "b", "b", "a"], "H": ["a", "a", "b", "b", "b"],
                    "I": ["a", "b", "a", "a", "a"], "J": ["a", "a", "b", "a", "a"],
                    "K": ["a", "b", "a", "a", "b"], "L": ["a", "b", "a", "b", "a"], "M": ["a", "b", "a", "b", "b"],
                    "N": ["a", "b", "b", "a", "a"], "O": ["a", "b", "b", "a", "b"],
                    "P": ["a", "b", "b", "b", "a"], "R": ["b", "a", "a", "a", "a"], "S": ["b", "a", "a", "a", "b"],
                    "T": ["b", "a""a", "b", "a"], "U": ["b", "a", "a", "b", "b"],
                    "V": ["b", "a", "a", "b", "b"], "W": ["b", "a", "b", "a", "a"], "X": ["b", "a", "b", "a", "b"],
                    "Y": ["b", "a", "b", "b", "a"], "Z": ["b", "a", "b", "b", "b"]
                    }
    x = kazda_litera[litera]
    setheading(90)
    for i in range(5):
        kwadrat("yellow" if x[i] == "a" else "blue", a)
        setheading(90)
        fd(a)
        # if x[i] == "a":
        #     kwadrat("yellow", a)
        #     setheading(90)
        #     fd(a)
        # else:
        #     kwadrat("blue", a)
        #     setheading(90)
        #     fd(a)


speed(0)
rt(90)
szyfruj("AAAAAAAAAABBBBBBBBBBCCCCCCCCCCDDDDDDDDDDXXXXXXXXXXYYYYYYYYYYZZZZZZZZZZ")
# szyfruj("GODZINAKODOWANIA")
# szyfruj("ABCDXYZ")
print(pos())
done()

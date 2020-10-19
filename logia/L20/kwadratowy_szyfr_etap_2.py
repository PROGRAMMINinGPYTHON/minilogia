from turtle import *

wspolrzedne_liter = {}

# a - dlugosc boku kwadratu
# x, y - lewy dolny róg
def kwadrat(kolor, x, y, a):
    pu()
    setpos(x, y)
    color("black", kolor)
    pd()
    begin_fill()
    setheading(0)
    for i in range(4):
        fd(a)
        lt(90)

    end_fill()


def rysuj_litere(litera, a, x, y):
    wspolrzedne_litery = wspolrzedne_liter[litera]
    # print("rysuj_litere ", litera, " ", wsp[0], " ", wsp[1], " ", a, " ", x, " ", y)
    for i in range(13):
        kwadrat("white", x, y + i * a, a)
        kwadrat("white", x + a, y + i * a, a)


    kwadrat("orange", x + wspolrzedne_litery[0] * a, y + wspolrzedne_litery[1] * a, a)

def inicjalizuj_wspolrzedne():
    for i in range(13):
        litera = chr(i + ord('a'))
        wspolrzedne_liter[litera] = (0, i)

        litera = chr(ord('a') + 13 + i)
        wspolrzedne_liter[litera] = (1, 12-i)



def koduj(napis):
    a = 760 / 2 / len(napis)
    x = -760 / 2
    y = -13 * a / 2
    i = 0
    inicjalizuj_wspolrzedne()
    print(wspolrzedne_liter)
    for litera in napis:
        rysuj_litere(litera, a, x + i * a * 2, y)
        i += 1


speed(0)
koduj("abcdefghi")
#koduj("ablmnopyz")
#koduj("abcdefghijklmnopqrstuwxyzabcdefghijklm")
koduj("abbbbbbbbbbbbbbbb")

done()

#
# print(chr(97))
# print(ord('a'))
# print(ord("m"))

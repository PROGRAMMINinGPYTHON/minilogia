# from turtle import *
#
# def koduj(napis):
#     kodowanie(napis)
#
# def podklad(napis):
#     a = 760/2/len(list(napis))
#     pu()
#     setpos(-760/2,-13*a/2)
#     pd()
#     for i in range(len(list(napis))):
#         for j in range(13):
#             for k in range(2):
#                 setheading(0)
#                 for l in range(4):
#                     fd(a)
#                     lt(90)
#                 fd(a)
#             lt(90)
#             fd(a)
#             lt(90)
#             fd(2*a)
#         rt(180)
#         fd(2*a)
#         rt(90)
#         fd(13*a)
#
# def \gdzie(napis,idx,x2,y2):
#     a = 760/2/len(list(napis))
#     tab = list(napis)
#     ord_a = ord('a')
#     if ord(tab[idx]) - ord_a >13:
#         x = 0
#     else:
#         x = 1
#     if ord(tab[idx])- ord_a >12:
#         (ord(tab[idx])-ord_a)+(ord(tab[idx])-ord_a)
#     else:
#         y = ord(tab[idx])-96
#     print(ord("m")-96)
#     pu()
#     setpos(x2+x*a,y2+y*a)
#     pd()
#
# def kodowanie(napis):
#     a = 760/2/len(list(napis))
#     pu()
#     setpos(-760 / 2, (-13*a)/2)
#     pd()
#     for i in range(len(list(napis))):
#         gdzie(napis,i,-380+a*i*2,(-15*a)/2)
#         setheading(0)
#         kwadrat(a)
#
#
# def kwadrat(a):
#     fillcolor("orange")
#     begin_fill()
#     fd(a)
#     lt(90)
#     fd(a)
#     lt(90)
#     fd(a)
#     lt(90)
#     fd(a)
#     lt(90)
#     end_fill()
#
#
# speed(0)
#
#
# def szyfr(napis):
#     #podklad(napis)
#     kodowanie(napis)
#
#
# szyfr("abnportwsabc")
# print(ord("n"))
# done()
#
#









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


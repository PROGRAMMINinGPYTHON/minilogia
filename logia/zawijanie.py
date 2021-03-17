import math


def koduj(napis, ile):
    pass

global x
def zamiana_napisu_na_tablice(napis):
    x = []
    a = math.ceil(math.sqrt(len(napis) + 1))
    for i in range(a):
        x.append([])
        for j in range(a):
            w = 0
            for q in range(len(x)):
                w = w + len(x[q])
            if w == len(napis):
                print(napis, x, a)
                return napis,a,x
            else:
                x[i].append(napis[j + a * i])
    print(napis,x,a)
    return napis,a,x

def zamiana_na_ramke(napis,a,x):
    print("------------------------------")
    print(napis,a,x)
    for u in range(len(x)):
        while len(x[u]) <a:
            x[u].append("")
            print(x)
    for z in range(a-len(x)):
        x.append(["","","","",""])
    ramki = []
    print(ramki,"_________________________")
    for i in range(math.ceil(a/2)):
        for j in range(a-i*2):
            pass
    print(ramki)
testy = [
    [],

]


def testowanie():
    for x in testy:
        msg = "blad"
        assert koduj(x[0], x[1]) == x[2], f"blad{msg}"


zamiana_napisu_na_tablice("tajnawiadomoscantka")
zamiana_na_ramke("tajnawiadomoscantka",zamiana_napisu_na_tablice("tajnawiadomoscantka")[1],zamiana_napisu_na_tablice("tajnawiadomoscantka")[2])
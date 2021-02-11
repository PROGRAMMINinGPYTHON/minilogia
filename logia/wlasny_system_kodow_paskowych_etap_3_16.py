def suma_cyfr(liczba):
    liczba = str(liczba)
    suma = 0
    for znak in liczba:
        suma += int(znak)
    return suma



def jaka(a, b, n):
    lcz_liczb = 0
    for i in range(1, 100001):
        suma = suma_cyfr(i)
        if suma > a and suma < b:
            lcz_liczb += 1
            if lcz_liczb == n:
                return i
    return -1



testy = [
    [1, 10, 4, 5],
    [1,3,5,110],
    [21,23,20,985],
    [3,17,34,43],
    [23,39,58,2598],
    [2,4,60,-1],
    [1,4,90,-1],
    [1,40,100,103],
    [20,40,100,1589],
    [25,30,100,4896],
    [28,32,100,7967],

]


def testowanie():
    for x in testy:
        wywolanie = jaka(x[0], x[1], x[2])
        msg = "ERROR", "for params : ", x, " dostal ", wywolanie, "oczekiwal: ", x[3]
        assert wywolanie == x[3], f"blad{msg}"
    print("OK")


testowanie()

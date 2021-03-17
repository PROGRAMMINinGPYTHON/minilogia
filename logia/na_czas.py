


def liczba(a,n):
    x = 0
    w = x**n
    while a>=w:
        x+= 1
        w = x ** n
    return x-1

testy = [
    [],
         ]

print(liczba(90972061672647417382949994702882855264900000,2))

def testowanie():
    pass

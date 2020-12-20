
def optymalizacja_mandatow(a, b, c):
    b = b.split()
    c = c.split()
    for i in range(a):
        c[i] = int(c[i])
        b[i] = int(b[i])
    c.sort()
    b.sort()
    suma = 0
    for i in range(a):
        x = str(b[i]) + str(c[-1 - i])
        suma = suma + int(x)
    return (suma)

def wywolanie():
    a = int(input())
    b = input()
    c = input()
    print(optymalizacja_mandatow(a, b, c))

wywolanie()

testy = [
    [3, "5 2 30", "13 9 7", 579],
    [5, "5 12 7 2 8", "1 1 1 1 1", 345],
]

def dodajMilionMandatow():
    milionMandatow = ""
    for i in range (1000000):
        milionMandatow += str(100000)
        if (i < 999999): milionMandatow += " "

    milion = [1000000, milionMandatow, milionMandatow, 100000100000000000]
    testy.append(milion)


def testowanie():

    dodajMilionMandatow()

    a = 100000100000
    b = a * 1000000
    print (a)
    print(b)

    for x in testy:
        assert optymalizacja_mandatow(x[0], x[1], x[2]) == x[3]
        print(x[0] , " OK", )
    print("ok")



# testowanie()

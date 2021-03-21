import math

def najw_plus():
    a = input()
    b = input()
    b= b.split()
    tablica = b
    for m in range(int(a)):
        tablica[m] = int(tablica[m])
    tab_wynikow = []
    najwiekszy = 0
    for i in range(len(tablica)):
        if najw_plus_na_tej_pozycji(tablica,najwiekszy,i) == None:
            tab_wynikow.append(0)
        else:
            tab_wynikow.append(najw_plus_na_tej_pozycji(tablica, najwiekszy, i))
    print(max(tab_wynikow))


def najw_plus_na_tej_pozycji(tablica, najw_dotychczas, pozycja):
    p = najw_dotychczas
    k = math.floor((tablica[pozycja]-1)/2)
    print(k)
    srodek = 0
    while p <k:
        srodek = p+k//2
        if srodek == p or k == srodek:
            if x_pozycji_za_i_przed(tablica, pozycja, k):
                return k
            else:
                return p
        if x_pozycji_za_i_przed(tablica, pozycja, srodek):
            p = srodek
        else:
            k = srodek
        print(p,k,srodek)
    return srodek

def x_pozycji_za_i_przed(tablica, pozycja, x):
    for p in range(x):
        if tablica[pozycja - p] >= x + 1 and pozycja-x>=0:
            pass
        else:
            return False

        if tablica[pozycja + p] >= x + 1 and pozycja+x+1 <=len(tablica):
            pass
        else:
            return False
    return True


# print(najw_plus_na_tej_pozycji([6,5,4,6,3,5,2],0,2))
print(najw_plus_na_tej_pozycji([6,5,4,6,3,5,2],0,6))


# najw_plus()
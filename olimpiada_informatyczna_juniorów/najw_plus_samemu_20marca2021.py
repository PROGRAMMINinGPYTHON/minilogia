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
    x = 0
    while x<len(tablica) and tablica[pozycja]>x*2+1:
        spr_czy_x_pozycji_za_i_przed(tablica,pozycja,x)
        x+= 1
        if spr_czy_x_pozycji_za_i_przed(tablica,pozycja,x) == False:
            return x-1


def spr_czy_x_pozycji_za_i_przed(tablica, pozycja, x):
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

najw_plus()
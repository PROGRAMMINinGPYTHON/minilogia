def wczytanie_drugiej_lini():
    b = input()
    b = list(b)
    for i in range(0,len(b),2):
        b[i] = int(b[i])
    print(b)

def wczytanie_pierwszej_lini():
    pass


def znajdz_idx_najw_wartosci(tab_liczenie):
    idx_najw = 0
    for i in range(len(tab_liczenie)):
        if tab_liczenie[i] > tab_liczenie[idx_najw]:
            idx_najw = i
            print(idx_najw)
    return idx_najw


def wypisanie():
    pass


def dodawanie_przyciskow(pierwsza_linia, tab_z_przyciskami, tab_licznenie):
    for i in range(pierwsza_linia[2]):
        pass


wczytanie_drugiej_lini()
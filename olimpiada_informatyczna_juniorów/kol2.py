tablica = []
def pociagi(n,m,z):
    liczba_miast = n
    liczba_miejsc = m
    liczba_zgloszen = z
    tablica_wynikow = []
    for w in range(liczba_miast+1):
        tablica.append(0)
    for i in range(liczba_zgloszen):
        a = input()
        a = a.split()
        for q in range(len(a)):
            a[q] = int(a[q])
        tablica_wynikow.append(zgloszenie(liczba_miejsc,a[2],a[0],a[1],tablica))
    # for p in range(len(tablica_wynikow)):
    #     print(tablica_wynikow[p])
    print('\n'.join(tablica_wynikow))

def zgloszenie(max_osob_ktore_moge_zabrac, ile_osob, od_kad,do_kad,tablica):
    if sprawdzenie_zgloszenia(max_osob_ktore_moge_zabrac, ile_osob, od_kad, do_kad, tablica) != True:
        return "N"
    for k in range(od_kad , do_kad):
        tablica[k] += ile_osob
    return "T"


def sprawdzenie_zgloszenia(max_osob_ktore_moge_zabrac, ile_osob, od_kad, do_kad,tablica):  # tablica pokoazuje ile jest osob w ktorym miescie
    tak_czy_nie = True  # zakladam ze  da sie
    for j in range(od_kad, do_kad):
        if tablica[j] + ile_osob > max_osob_ktore_moge_zabrac:
            tak_czy_nie = False
            return False
    return tak_czy_nie

b = input()
b = b.split()
b[0] = int(b[0])
b[1] = int(b[1])
b[2] = int(b[2])
pociagi(b[0],b[1],b[2])
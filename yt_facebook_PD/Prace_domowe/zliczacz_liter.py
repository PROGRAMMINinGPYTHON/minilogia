def wylicz_i_wypisz():
    caly_tekst = []
    liczba_znakow = 0
    ilosc_wierszy = int(input())
    for linia in range(ilosc_wierszy):
        wiersz = input()
        caly_tekst.append(list(wiersz))

    for znak in range(ord('a'), ord('z')):
        for j in range(ilosc_wierszy):
            liczba_znakow += caly_tekst[j].count(chr(znak))
        if liczba_znakow > 0:
            print(chr(znak), liczba_znakow)
        liczba_znakow = 0
    liczba_znakow = 0
    for znak in range(ord('A'), ord('Z')):
        liczba_znakow += + caly_tekst[j].count(chr(znak))
        if liczba_znakow > 0:
            print(chr(znak), liczba_znakow)
        liczba_znakow = 0


wylicz_i_wypisz()
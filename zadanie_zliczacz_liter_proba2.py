licznik = {}
for i in range (ord('z') - ord('a') + 1):
    licznik[chr(ord('a') + i)] = 0
    licznik[chr(ord('A') + i)] = 0


def przetworzenie_jednego_wierszu(wiersz):
    for znak in wiersz:
        if (znak != ' '):
            licznik[znak] = licznik[znak]+1


def zlicz():
    for i in range(int(input())):
        przetworzenie_jednego_wierszu(input())


def wypisz():
    for i in range(ord('z') - ord('a') + 1):
        if (licznik[chr(ord('a') + i)]>0):
            print(chr(ord('a') + i), licznik[chr(ord('a') + i)])
    for i in range(ord('z') - ord('a') + 1):
        if (licznik[chr(ord('A') + i)]>0):
            print(chr(ord('A') + i), licznik[chr(ord('A') + i)])
zlicz()
wypisz()
































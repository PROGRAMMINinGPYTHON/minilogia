ilosc_programow = input()
rozmiary_programow = input()
rozmiary_programow = rozmiary_programow.split()
ilosc_plyt = input()
rozmiar_plyt = input()
rozmiar_plyt = rozmiar_plyt.split()


def programy():
    przetworzenie_wstepne()
    # przetwarzanie()


def przetworzenie_wstepne():
    for i in range(len(rozmiar_plyt)):
        rozmiar_plyt[i] = int(rozmiar_plyt[i])
    for i in range(len(rozmiary_programow)):
        rozmiary_programow[i] = int(rozmiary_programow[i])

    rozmiary_programow.sort()
    rozmiar_plyt.sort()
    if ilosc_programow > ilosc_plyt:
        for i in range(int(ilosc_programow) - int(ilosc_plyt)):
            rozmiary_programow.pop(-1)
    else:
        for i in range(int(ilosc_plyt) - int(ilosc_programow)):
            rozmiar_plyt.pop(0)

def przetw():
    print(rozmiary_programow)
    print(rozmiar_plyt)
    lcz = 0
    k = 0
    l = 0
    for i in range(len(rozmiary_programow)):
        for j in range(len(rozmiary_programow)-i):
            if rozmiary_programow[i]<rozmiar_plyt[j+i]:
                lcz += 1
                break
    print(lcz)
przetworzenie_wstepne()
przetw()



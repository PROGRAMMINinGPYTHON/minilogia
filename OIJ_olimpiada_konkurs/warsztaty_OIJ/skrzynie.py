def wczytanie():
    a = input()
    a = a.split()
    a[0] = int(a[0])
    a[1] = int(a[1])
    skrzynie = input()
    skrzynie = skrzynie.split()
    for i in range(len(skrzynie)):
        skrzynie[i] = int(skrzynie[i])
    return skrzynie, a[1]


def ile_czasu(skrzynie, ile_kluczy):
    czas = 0
    skrzynie.sort()
    ost = skrzynie[-1]
    czas_skrzyni = 0
    for i in range(len(skrzynie) - ile_kluczy + 1):
        czas_skrzyni += skrzynie[i]
    return min(czas_skrzyni, ost)


print(ile_czasu(wczytanie()[0], 2))

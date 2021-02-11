samogłoski = ["a", "e", "i", "o", "u", "y"]


def dodanie_a(slowo):
    waga = 0
    for i in range(len(slowo)):
        if slowo[i] in samogłoski:
            waga = waga - 1
        else:
            waga = waga + 1
    return waga


def dodanie_b(slowo):
    waga = dodanie_a(slowo)
    for i in range(round(len(slowo) / 2)):
        print(waga)


dodanie_a(["a", "a", "b", "b", "a", "b"])

dodanie_b(["a", "a", "b", "b", "a", "b"])

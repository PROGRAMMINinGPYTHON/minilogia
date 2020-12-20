def zamiana_na_inty(tab_progm, tab_plyt):  # w tej funkcji zamieniam str w tablicy na inty , nic szczegolnego
    for i in range(len(tab_progm)):  # tutaj zamieniam str w tab programy na inty
        tab_progm[i] = int(tab_progm[i])
    for j in range(len(tab_plyt)):  # tutaj zamieniam str w tab plyty na inty
        tab_plyt[j] = int(tab_plyt[j])


def programy(ilosc_prog, tab_programow, ile_plyt, tab_plyt):
    zamiana_na_inty(tab_programow, tab_plyt)
    tab_plyt.sort()  # sortuje tablice plyt
    tab_programow.sort()  # sortuje tablice programow
    lcz = 0  # definiuje zmienna lcz , slozy ona do przechowywania tego ile programow sie zmiescilo w plythach
    while len(tab_programow) > 0 and len(tab_plyt) > 0:  # tutaj usuwam wszystkie mniejsze wartosci z tab plyt od tab programow od 0
        while len(tab_plyt) > 0 and tab_programow[0] > tab_plyt[0]:
            tab_plyt.pop(0)
        if len(tab_plyt) > 0:  # tutaj sprawdzam czy tablica nie jest pusta, jesli jest to nic nie robie , jesli nie jest to zwiekszam lcz o 1 oraz usuwam z tab programow indeks 0 , poniewaz ten program juz sie zmiescil na jednej z plyt , usuwam z tab plyt indeks 0
            lcz += 1
            tab_programow.pop(0)
            tab_plyt.pop(0)
    return lcz


print(programy(input(), input().split(), input(), input().split()))

testy = [
    [["1", "1", "1"], ["0", "0", "0", "0"], 0],
    [["1", "1", "1"], ["9", "9"], 2],
    [["1", "1", "9"], ["8", "8"], 2],
    [["2", "2", "2"], ["1", "1", "3"], 1],
    [["1", "9", "9", "9", "9"], ["1", "1", "1", "1", "1"], 1],
    [["8", "1", "4"], ["5", "5", "4", "4", "6"], 2],
    [["2", "3", "4"], ["1", "2", "3"], 2],
    [["0", "0"], ["1", "1"], 2],
    [["0", "0"], ["1", "1"], 2],
    [["1111111111", "22222222"], ["9"], 0]

]


def testowanie():
    for test in testy:
        msg = " dla " + " ".join(test[0]) + ", plyty: " + " ".join(test[1]) + " otrzymany wynik" + str(
            programy(len(test[0]), test[0].copy(), len(test[1]), test[1].copy())) + " oczekiwany wynik" + str(test[2])
        assert programy(len(test[0]), test[0], len(test[1]), test[1]) == test[2], f"blad {msg}"

# testowanie()

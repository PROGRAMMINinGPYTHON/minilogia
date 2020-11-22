def zamiana_na_inty(tab_progm, tab_plyt):
    for i in range(len(tab_progm)):
        tab_progm[i] = int(tab_progm[i])
    for j in range(len(tab_plyt)):
        tab_plyt[j] = int(tab_plyt[j])


def programy(ilosc_prog, tab_programow, ile_plyt, tab_plyt):
    lcz = 0
    # print("prog ", tab_programow, " plyt ", tab_plyt)
    for i in range(len(tab_programow)):
        k = 0
        for j in range(len(tab_plyt)):
            if tab_programow[i] <= tab_plyt[j]:
                lcz = lcz + 1
                tab_plyt.pop(j)
                break
            else:
                print(lcz)
                tab_plyt.pop(j)

    print(lcz)
    return lcz


programy(input(),input().split(),input(), input().split())


testy = [
    [["1", "1", "9"], ["8", "8"], 2],
    [["2", "2", "2"], ["1", "1", "3"], 1],
    [["1", "9", "9", "9", "9"], ["1", "1", "1", "1", "1"], 1],
    [["8", "1", "4"], ["5", "5", "4", "4", "6"], 2],
    [["2", "3", "4"], ["1", "2", "3"], 2],
    [["0", "0"], ["1", "1"], 2]

]


def testowanie():
    for test in testy:
        print("testuje dla programy: ", test[0], ", plyty: ", test[1], "otrzymany wynik",
              programy(len(test[0]), test[0].copy(), len(test[1]), test[1].copy()), "oczekiwany wynik", test[2])
        assert programy(len(test[0]), test[0], len(test[1]), test[1]) == test[2]
        print("OK")


# testowanie()

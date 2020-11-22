# ilosc_programow = int(input())
# rozmiary_programow = input()
# ilosc_plyt = int(input())
# rozmiary_plyt = input()
# rozmiary_programow = rozmiary_programow.split()
# rozmiary_plyt = rozmiary_plyt.split()


def programy(ilosc_programow, rozmiary_programow, ilosc_plyt, rozmiary_plyt):
    zamiana_na_inty(rozmiary_programow, rozmiary_plyt)
    usuniecie(ilosc_programow, rozmiary_programow, ilosc_plyt, rozmiary_plyt)
    return przetwarzanie(rozmiary_programow, rozmiary_plyt)


# def wczytanie():
# print(ilosc_programow)
# print(rozmiary_programow)
# print(ilosc_plyt)
# print(rozmiary_plyt)

def usuniecie(ilosc_programow, rozmiary_programow, ilosc_plyt, rozmiary_plyt):
    rozmiary_programow.sort()
    rozmiary_plyt.sort()
    if ilosc_plyt > ilosc_programow:
        for i in range(ilosc_plyt - ilosc_programow):
            rozmiary_plyt.pop(0)
    else:
        for j in range(ilosc_programow - ilosc_plyt):
            rozmiary_programow.pop(-1)


def zamiana_na_inty(rozmiary_programow, rozmiary_plyt):
    for i in range(len(rozmiary_programow)):
        rozmiary_programow[i] = int(rozmiary_programow[i])
    for j in range(len(rozmiary_plyt)):
        rozmiary_plyt[j] = int(rozmiary_plyt[j])


def przetwarzanie(rozmiary_programow, rozmiary_plyt):
    lcz = 0
    for i in range(len(rozmiary_plyt)):
        for j in range(len(rozmiary_plyt)):
            if i+j == len(rozmiary_plyt):
                break
            else:
                if rozmiary_plyt[i] >= rozmiary_programow[i+j]:
                    lcz = lcz + 1
                    break
                else:
                    pass
    return lcz


testy = [
    # [["1", "1", "9"], ["8", "8"], 2],
    # [["2", "2", "2"], ["1", "1", "3"], 1],
    [["1", "9", "9", "9", "9"], ["1", "1", "1", "1", "1"], 1],
    [["8", "1", "4"], ["5", "5", "4", "4", "6"], 2],
    [["2", "3", "4"], ["1", "2", "3"], 2],
    [["0","0"],["1","1"],2]

]


def testowanie():
    for test in testy:
        print("testuje dla programy: ", test[0], ", plyty: ", test[1], "otrzymany wynik", programy(len(test[0]), test[0].copy(), len(test[1]), test[1].copy()), "oczekiwany wynik", test[2])
        assert programy(len(test[0]), test[0], len(test[1]), test[1]) == test[2]
        print("OK")

#testowanie()
print(programy(int(input()), input().split(), int(input()), input().split()))
# wczytanie()

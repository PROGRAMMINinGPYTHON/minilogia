def strony(a,b):
    pass

def wypisanie_wszystkich_percostam_liter(ile_liter):
    tab_liter = ['a','b','c','d']
    print("--------")
    for i in range(1):
        print(tab_liter)
    for i in range(4):
        for i in range(3):
            for j in range(1):
                tmp = tab_liter[2]
                tab_liter[2] = tab_liter[3]
                tab_liter[3] = tmp
                print(tab_liter)
            tmp = tab_liter[1]
            tab_liter[1] = tab_liter[2]
            tab_liter[2] = tmp
            print(tab_liter)
    tmp = tab_liter[0]
    tab_liter[0] = tab_liter[1]
    tab_liter[1] = tmp
    print(tab_liter)



wypisanie_wszystkich_percostam_liter(2)
testy = [
    [2,["ba"],1],
    [2,["ab"],1],

]


def testowanie():
    for x in testy:
        wywolanie = strony(x[0], x[1])
        msg = "blad! ", "oczekiwal:, ", x[2]," dostal: ", wywolanie
        assert wywolanie == x[2] , f"blad{msg}"

# testowanie()
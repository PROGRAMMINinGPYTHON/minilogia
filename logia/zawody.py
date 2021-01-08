def zawody(lista):
    najslabszy = [100,0]
    tab_alfabet = ["A","B","C","D"]
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[i][j] <najslabszy[0]:
                najslabszy = lista[i][j],j
        lista[i].remove(najslabszy[0])
        tab_alfabet.pop(najslabszy[1])
        najslabszy = [100,0]
    print(tab_alfabet)
zawody([[4,0,2,1],[1,2,3],[2,1]])











testy = []

def testowanie():
    pass

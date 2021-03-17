def lucas(n):
    pierwsza = 2
    nastepna = 1
    www = pierwsza
    for i in range(n-1):
        # print(nastepna)
        pierwsza = nastepna
        nastepna = nastepna+www
        www = pierwsza % 100
    www = str(www)
    if len(www) == 1:
        pass
    else:
        www = www[-2]+www[-1]
    if len(www) == 1:
        print(www[0])
        return int(www[0])
    else:
        if www[0] == "0":
            print(www[1])
            return int(www[1])
        else:
            print(www)
            return int(www)

lucas(10000000)

testy = [
    [10000000, 24]
    # [1, 2],
    # [2, 1],
    # [11, 23],
    # [44, 29],
    # [999, 3],
    # [100044, 79],
    # [200046, 11],
    # [687654, 71],
    # [897895, 18],
    # [8090386, 36],
    # [10000000, 24],
    # [9, 47],
    # [35, 43],
    # [45, 7],
]


def testowanie():
    for x in testy:
        msg = "blad"
        assert lucas(x[0]) == x[1], f"blad{msg}"

testowanie()




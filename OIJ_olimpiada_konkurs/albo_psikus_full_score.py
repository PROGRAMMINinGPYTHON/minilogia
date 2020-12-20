import math


# a = int(input())
# b = input()
# b = b.split()

def psikus(a, b):
    stpar = True
    liczStpar = 0
    niep = 0
    zak = 0
    psik = 0
    for elem in b:
        if int(elem) % 2 == 0:
            psik = psik + 1 + zak
            zak += 1
            # niep bez zmian
            if (stpar):
                liczStpar +=1
        else:
            if stpar:
                psik = psik + liczStpar
                stpar = False
            else:

            zak = (niep + 1) // 2
            niep += 1
    return psik

testy = [
    # [1, "4", 1],
    # [2, "4 2", 3],
    # [3, "4 2 3", 3],
    [4, "4 2 3 1", 6],
    [1, "1", 0],
    [1, "2", 1],
    [2, "2 2", 3],
    [2, "2 3", 1],
    [1, "1", 0],
    [2, "1 1", 1],
    [3, "1 1 1", 2],
    [4, "1 1 1 1", 4],
    [5, "1 1 1 1 1", 6],
    [6, "1 1 1 1 1 1", 9],

]


def test():
    for x in testy:
        msg = "test ", x[0], " ", x[1],"otrzymal " ,psikus(x[0],x[1].split()),"oczekiwal ",x[2]
        assert psikus(x[0], x[1].split()) == x[2], f"blad {msg}"
    print("ok")


test()

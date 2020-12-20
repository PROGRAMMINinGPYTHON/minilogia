import math

# a = int(input())
# b = input()
# b = b.split()


def nieparzyste(a):
    ile = 0
    for i in range(1, a + 1):
        ile += math.floor(i / 2)
    return ile


def psikus(droga):
    lcz = 0
    for j in range(0, len(droga)):
        pom = 0

        for i in range(j, len(droga)):
            pom = pom + int(droga[i])
            if pom % 2 == 0:
                lcz += 1
    return lcz


def wszystko(a, b):
    x = 0

    while int(b[x]) % 2 == 1 and x < a - 1:
        x += 1
        if x == a - 1:
            return nieparzyste(a)
    return psikus(b)


# wszystko(a, b)

testy = [
    [4, "4 2 3 1", 6],
    [1, "1", 0],
    [1, "2", 1],
    [2,"2 2", 3],
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
        msg = "test ", x[0]," ", x[1]
        assert wszystko(x[0], x[1].split()) == x[2], f"blad {msg}"
    print("ok")


test()

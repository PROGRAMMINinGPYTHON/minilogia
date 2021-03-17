def minWys(l, p, wysokosci):
    i = l
    minimum = wysokosci[l]
    while i < p:
        if wysokosci[i] > minimum:
            minimum = wysokosci[i]
        i+=1

    return minimum


def jestPlus(L, N, wysokosci):
    idx = L
    while idx < N - L:
        if (wysokosci[idx] >= 2 * L + 1) and minWys(idx - L, idx + L + 1, wysokosci) >= L+1:
            return True
        idx += 1

    return False


def plus():
    N = int(input())
    wysokosci = [int(x) for x in input().split()]

    lewy = 0;
    p = N

    while lewy + 1 < p:
        srodek = (lewy + p) // 2

        if jestPlus(srodek, N, wysokosci):
            lewy = srodek
        else:
            p = srodek - 1

    if lewy == p and jestPlus(lewy, N, wysokosci):
        print(lewy)
        return
    else:
        if jestPlus(p, N, wysokosci):
            print(p)
            return
        elif jestPlus(p - 1, N, wysokosci):
            print(lewy)
            return
        elif jestPlus(lewy, N, wysokosci):
            print(lewy)
            return
        else:
            print(0)
            return

plus()

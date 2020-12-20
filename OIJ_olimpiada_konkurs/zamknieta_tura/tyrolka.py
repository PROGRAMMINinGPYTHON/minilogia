def tyrolka(n,a):
    n = int(input())
    for j in range(n):
        x = input()
        a.append(x)
    for i in range(n):
        b = a[i]
        a[i] = b.split()
    for k in range(n):
        a[k][0] = int(a[k][0])
        a[k][1] = int(a[k][1])
    print(a)
    najm = [1, "a", "b"]
    for j in range(n):
        for i in range(n - 1):
            if a[j][1] > a[i + 1][1]:
                l = a[j][1] - a[i + 1][1]
            else:
                l = a[i + 1][1] - a[j][1]
            if a[j][0] > a[i + 1][0]:
                l = l / (a[j][0] - a[i + 1][0])
            else:
                if a[i + 1][0] - a[j][0] == 0:
                    pass
                else:
                    l = l / (a[i + 1][0] - a[j][0])
            if l > 0 and l < najm[0]:
                print(l)
                print(a[i],a[j])
                najm[0] = l
                najm[1] = i
                najm[2] = j




tyrolka()

testy = []


def testowanie():
    for x in testy:
        assert tyrolka()

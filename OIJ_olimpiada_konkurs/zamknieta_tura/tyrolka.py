def tyrolka():
    n = int(input())
    a = []
    for i in range(n):
        x = input()
        x = x.split()
        a.append(x)
    for j in range(n):
        a[j][0] = int(a[j][0])
        a[j][1] = int(a[j][1])
    najm = [9999999,x,y]
    obl = 2000000000000000000000
    for r in range(n):
        for g in range(n - 1):
            if a[r][1] > a[g][1]:
                obl = a[r][1] - a[g][1]
            else:
                obl = a[g][1] - a[r][1]
            if obl == 0:
                pass
            else:
                if a[r][0] > a[g][0]:
                    if a[r][0] ==  a[g][0]:
                        pass
                    else:
                        obl = obl / (a[r][0] - a[g][0])
                else:
                    if a[g][0] == a[r][0]:
                        pass
                    else:
                        obl = obl / (a[g][0] - a[r][0])
                if obl > 0 and obl < najm[0]:
                    najm[0] = obl
                    najm[1] = r+1
                    najm[2] = g+1
    print(najm[1],najm[2])


def testRet():
    return 4, 6, "abc"


x, y, z = testRet()

# print(x)
# print(y)
# print(z)
# print(testRet())

tyrolka()

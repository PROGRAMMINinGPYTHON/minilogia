p = []
k = []


def roztopy():
    a = input()
    a = int(a)
    p = []
    k = []
    for i in range(a):
        x = input().split()
        p.append(int(x[0]))
        k.append(int(x[1]))
    p.sort()
    k.sort()
    p.append(0)
    lcz = 0
    najw = lcz
    q = 0
    t = 0
    while t <len(p)-1:
        if p[t] <= k[q]:    #
            lcz += 1
            t += 1
        else:
            lcz -= 1
            q += 1
        if lcz > najw:
            najw = lcz
    print(najw)
    return najw


roztopy()

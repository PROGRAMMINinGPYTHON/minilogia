

def tyrolka():
    n = input()
    a = []
    n = int(n)
    for i in range(n):
        x = input()
        x = x.split()
        a.append(x)
    for j in range(n):
        a[j][0] = int(a[j][0])
        a[j][1] = int(a[j][1])
    # print(a)
    wysokosci = {}
    for u in range(n):
        if a[u][1] not in wysokosci:
            wysokosci[a[u][1]] = [a[u][0]]
        else:
           wysokosci[a[u][1]].append(a[u][0])
    for s in range(200000):
        if s in wysokosci:
            # print(wysokosci[s])
            wysokosci[s].sort()
            while len(wysokosci[s])>2:
                wysokosci[s].pop(1)
            # print(wysokosci[s])
    # print(wysokosci)
    w = []
    for q in range(1,200000):
        if q in wysokosci:
            w.append([(wysokosci[q][0]),q])
            if len(wysokosci[q])>1:
                w.append([wysokosci[q][1],q])
    print(wysokosci)
    najm = [9999999,'x','y']
    obl = 2000000000000000000000
    print(wysokosci)
    print(a)
    a = w

    print(a)
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



tyrolka()
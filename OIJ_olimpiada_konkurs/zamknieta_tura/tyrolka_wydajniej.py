

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
    print(a)
    wysokosci = {}
    for u in range(n):
        if a[u][1] not in wysokosci:
            wysokosci[a[u][1]] = [a[u][0]]
            print(wysokosci)
        else:
           wysokosci[a[u][1]].append(a[u][0])
           print(wysokosci)
    # for i in range()
tyrolka()



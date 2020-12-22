

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


tyrolka()



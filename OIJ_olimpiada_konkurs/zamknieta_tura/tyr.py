
def tyr():
    a = []
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
    najm = 999

print(tyrolka())



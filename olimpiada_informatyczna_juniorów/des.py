N = int(input())

L = [int(l) for l in input().split()]

L.sort()

if len(L)<4:
    print(0)
else:
    a = L[-4]
    print(a*a)


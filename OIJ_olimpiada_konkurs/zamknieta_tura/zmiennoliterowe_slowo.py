

def zmien_slow(a):
    print(a)
    a = list(a)
    print(a)
    ile_trojek = 0
    q = 0
    for j in range(len(a)-1):
        if a[q] == "a" and a[q+1] == "a":
            a.pop(q)
            q = q-1
        if a[q]== "b" and a[q+1] == "b":
            a.pop(q)
            q = q-1
        q += 1
        print(a)


    print(len(a))
    for i in range(len(a)):
        if a[i] == "a" and a[i+1] == "b" and a[i+2] == "a":
            ile_trojek += 1
        if a[i] == "b" and a[i+1] == "a" and a[i+2] == "b":
            ile_trojek += 1

    print(ile_trojek)
zmien_slow(input())

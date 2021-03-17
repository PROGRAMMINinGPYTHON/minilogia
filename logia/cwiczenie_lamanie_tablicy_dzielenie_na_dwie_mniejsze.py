def liczba(a, n):
    if a == 1:
        return 1
    p = 1
    k = a
    while p<k:
        s = (p+k) // 2
        if s ** n <= a:
            p = s+1
        else:
            k = s
    return p -1

liczba(1024,2)

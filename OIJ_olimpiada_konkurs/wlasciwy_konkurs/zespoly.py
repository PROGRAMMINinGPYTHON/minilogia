

def zespol():
    a = int(input())
    b = input()
    b = b.split()
    for i in range(a):
        b[i] = int(b[i])
    b.sort()
    lcz = 0
    j = 0
    while j < a-2:
        if b[j] == b[j + 1] and b[j] == b[j + 2]:
            lcz += 1
            j += 2
        elif b[j] == b[j + 1] and b[j + 1] == b[j + 2] - 1:
            lcz += 1
            j += 2
        elif b[j] + 1 == b[j + 1] and b[j + 1] == b[j + 2]:
            lcz += 1
            j += 2
        j += 1
    print(lcz)


zespol()

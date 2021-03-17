# zakladam ze t <3
def najw_plus():
    a = input()
    b = input()
    b = b.split()
    for i in range(len(b)):
        b[i] = int(b[i])
    if b[0] >= 2 and b[1] >= 3 and b[2] >= 2:
        print(1)
    else:
        print(0)


najw_plus()

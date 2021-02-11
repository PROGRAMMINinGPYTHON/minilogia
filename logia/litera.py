def litera(a):
    wystepowanie_liter = []
    laczony_napis = ""
    for i in range(len(a)):
        laczony_napis = laczony_napis + a[i]
    for j in range(26):
        l = laczony_napis.count(chr(j + 97))
        if l > 0:
            wystepowanie_liter.append([l, chr(j + 97)])
    najw = [wystepowanie_liter[0]]
    for g in range(len(wystepowanie_liter)):
        if najw[0][0] < wystepowanie_liter[g][0]:
            najw[0] = wystepowanie_liter[g]
    for t in range(len(wystepowanie_liter)):
        if najw[0][0] == wystepowanie_liter[t][0]:
            najw.append(wystepowanie_liter[t])
    p = 0
    for c in range(len(najw) - 1):
        if najw[c - p] == najw[c + 1 - p]:
            najw.pop(c)
            p += 1
    if len(najw) == 1:
        return ("'" + najw[0][1] + "'")
    else:
        print("[", end="")
        for m in range(len(najw)):
            if m == len(najw) - 1:
                print("'" + najw[m][1] + "'", end="")
            else:
                print("'" + najw[m][1] + "'", end=",")
        print("]")


# litera(['ala', 'ma', 'kota'])
# print("------------------")
# litera(['abc', 'bac', 'cab'])
# print("------------------")
# litera(['bacdefghijklmnopqrstuvwxyz', 'aeouy', 'zyxwvutsrqponmlkjihgfedcab', 'diefghij'])
# print("------------------")
# litera(['cabdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedbac', 'acegikmoqsuwybdfhjlnprtvxz'])
# print("------------------")
# litera(['d', 'b', 'c', 'a', 'ddd', 'eeu', 'eu', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'fug',
#         'hiju', 'klmno', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

testy = [
    [['ala', 'ma', 'kota'], "'a'"]

]


def testowanie():
    for x in testy:
        print(x[0])
        assert litera(x[0]) == x[1]
    print("OK")

testowanie()

def czy_poprawne_nawiasy (nawiasy):
    stos = []
    x = True
    for i in range(len(nawiasy)):
        if nawiasy[i] == "(":
            stos.append("(")
            print(stos)
        else:
            if len(stos) == 0:
                return False
            else:
                stos.pop()

    if len(stos) >=1:
        x = False
    return x

print(czy_poprawne_nawiasy("()()"))
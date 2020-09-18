#główna_funkcja
def roz(napis):
    pass
#sprawdzam czy napis jest palindromem
def czy_to_palindrom(napis):
    napis_orginal = napis
    napis = list(napis)
    napis2 = list(napis_orginal)
    for i in range(round((len(napis)/2))):
        tmp = napis[i]
        napis[i] = napis[-1-i]
        napis[-1-i] = tmp
    if napis == napis2:
        print("tak_to_palindrom")
        return napis
    else:
        print("to nie palindrom")
        zamiana_w_palindrom(napis_orginal)

# zamieniam napis w palindrom
def zamiana_w_palindrom(napis):
    x = list(napis)
    for i in range(1,round(len(napis))+1):
        x.append(napis[-i])
        print(x)
    return(x)


print(czy_to_palindrom("ojk"))

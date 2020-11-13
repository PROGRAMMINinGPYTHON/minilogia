tab = [1,1,1,1,2,2,2,2,2,6]
def max_podciag(tab):
    max_wartosc = tab[0]
    max_dl = 1
    for i in range(len(tab)):
        pomoc = 0
        while i+pomoc<len(tab) and tab[i] == tab[i+pomoc] :
            pomoc+= 1
        if pomoc>max_dl:
            max_dl = pomoc
            max_wartosc = tab[i]
    return max_wartosc, max_dl

a, b = max_podciag(tab)
print (a)
print( b)




































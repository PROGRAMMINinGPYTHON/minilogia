tablica = [9,8,7,5,3]
def sort(tab):
    for i in range(len(tab)):
        wstawianie(i,tab)
def zamiana(x,y,tab):
    tmp = tab[x]
    tab[x] = tab[y]
    tab[y] = tmp

def wstawianie(poz,tab):
    while poz>0 and tab[poz]<tab[poz-1]:
        zamiana(poz,poz-1,tab)
        print(tab)
        poz -= 1

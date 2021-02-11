def odjecie(liczba):
    liczba = list(liczba)
    for i in range(len(liczba)):
        liczba[i] = int(liczba[i])
    liczba.sort()
    liczba_dol_gora = liczba

    liczba_gora_dol = []

    for i in range(len(liczba)):
        liczba_gora_dol.append(liczba[-1 - i])

    zlep_dol_gora = ""
    zlep_gora_dol = ""
    for i in range(len(liczba)):
        zlep_dol_gora = zlep_dol_gora + str(liczba_dol_gora[i])
        zlep_gora_dol = zlep_gora_dol + str(liczba_gora_dol[i])

    zlep_gora_dol = int(zlep_gora_dol)
    zlep_dol_gora = int(zlep_dol_gora)
    if zlep_gora_dol > zlep_dol_gora:
        x = zlep_gora_dol - zlep_dol_gora
    else:
        x = zlep_dol_gora - zlep_gora_dol
    return x


l = input()
a = odjecie(l)
lcz = 0
while a != l:
    a = odjecie(l)
    if str(a) == str(l):
        break
    l = str(a)
    lcz += 1

print(lcz)





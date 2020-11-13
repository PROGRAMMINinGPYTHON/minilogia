

olimp_i_j = input()

olimp_i_j = []
wczytanie = list(wczytanie)
if len(wczytanie) > 2:
    for i in range(len(wczytanie)):
        if wczytanie[i] == "o":
            olimp_i_j.append("o")
        if wczytanie[i] == "i":
            olimp_i_j.append("i")
        if wczytanie[i] == "j":
            olimp_i_j.append("j")

if len(olimp_i_j) > 2:
    while olimp_i_j[0] == "i" or olimp_i_j[0] == "j":
        olimp_i_j.pop(0)

for k in range(len(olimp_i_j)):
    if len(olimp_i_j) > 2:
        if k == len(olimp_i_j) - 2:
            break
        if olimp_i_j[k] == "o" and olimp_i_j[k + 1] == "o":
            olimp_i_j.pop(k)
        if olimp_i_j[k] == "i" and olimp_i_j[k + 1] == "i":
            olimp_i_j.pop(k)
        if olimp_i_j[k] == "j" and olimp_i_j[k + 1] == "j":
            olimp_i_j.pop(k)
        if olimp_i_j[k] == "o" and olimp_i_j[k + 1] == "j":
            olimp_i_j.pop(k + 1)
        if olimp_i_j[k] == "i" and olimp_i_j[k + 1] == "o":
            olimp_i_j.pop(k + 1)
        if olimp_i_j[k] == "j" and olimp_i_j[k + 1] == "i":
            olimp_i_j.pop(k + 1)

licznik = 0
for i in range(len(olimp_i_j)):
    if len(olimp_i_j) > 2:
        if olimp_i_j[i] == "o" and olimp_i_j[i + 1] == "i" and olimp_i_j[i + 2] == "j":
            licznik += 1

if licznik == 0:
    return "NIE"
else:
    return licznik


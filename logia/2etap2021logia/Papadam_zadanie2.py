napis = input()
lcz_papadam = 0
szukam = ["p", "a", "p", "a", "d", "a", "m"]
nr_szukanej = 0
for x in napis:
    if nr_szukanej == 7:
        nr_szukanej = 0
    if x == szukam[nr_szukanej]:
        nr_szukanej += 1
        if nr_szukanej == 7:
            lcz_papadam += 1

print(lcz_papadam)


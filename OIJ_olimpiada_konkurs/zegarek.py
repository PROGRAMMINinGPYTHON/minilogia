def zegarek(godz):
    godz = godz.split()
    for i in range(3):
        godz[i] = int(godz[i])
    godz[2] += 1
    if godz[2] == 60:
        godz[1] += 1
        godz[2] = 0
        if godz[1] == 60:
            godz[1] = 0
            godz[0] += 1
            if godz[0] == 24:
                godz[0] = 0

    wynik = ""
    if godz[2] < 10:
        godz[2] = '0' + str(godz[2])
    else:
        godz[2] = str(godz[2])

    if godz[0] < 10:
        godz[0] = '0' + str(godz[0])
    else:
        godz[0] = str(godz[0])

    if godz[1] < 10:
        godz[1] = '0' + str(godz[1])
    else:
        godz[1] = str(godz[1])

    wynik += str(godz[0]) + ':' + str(godz[1]) + ':' + godz[2]
    return (wynik)


print(zegarek(input()))


oczekiwany_wynik = {
    "12 34 51": "12:34:52",
    "23 59 59": "00:00:00",
    "0 0 0": "00:00:01",
    "1 1 01": "01:01:02",
    "10 2 59": "10:03:00"
}


def testowanie():
    for key in oczekiwany_wynik:
        print("testuje dla", key, "otrzymany wynik", zegarek(key), "oczekiwany wynik", oczekiwany_wynik[key])
        assert zegarek(key) == oczekiwany_wynik[key]


# testowanie()

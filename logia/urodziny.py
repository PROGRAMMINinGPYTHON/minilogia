ile_dni_ma_mies = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31

}


def zamiana_str_data_do_tab_data(data):
    data = list(data)
    dzien = data[1] + data[2]
    mies = data[3] + data[4]
    rok = data[5] + data[6] + data[7] + data[8]
    rok = int(rok)
    mies = int(mies)
    dzien = int(mies)
    x = [dzien, mies, rok]
    return x


def dodanie_dnia_do_daty(data, rok):
    x = 0
    for i in range(1000):
        if data[2] % 4 == 0 and data[1] == 2 and data[0] == 28 and x == 0:
            data[0] += -1
            x += 1
            # for i in range(8):
        if data[1] == 12 and data[0] == 31:
            data[2] = data[2] + 1
            data[1] = 1
            data[0] = 1
        else:
            if data[0] == ile_dni_ma_mies[data[1]]:
                data[0] = 1
                data[1] = data[1] + 1
            else:
                data[0] = data[0] + 1
    return data


def urodziny(a, b):
    print(a)
    data = zamiana_str_data_do_tab_data(a)
    print(data)
    x = dodanie_dnia_do_daty(data,1000)
    print(x)
    data = dodanie_dnia_do_daty(x,1000)
    print(data)tr
    9: 30,
    10: 31,
    11: 30,
    12: 31

}


def zamiana_str_data_do_tab_data(data):
    data = list(data)
    dzien = data[1] + data[2]
    mies = data[3] + data[4]
    rok = data[5] + data[6] + data[7] + data[8]
    rok = int(rok)
    mies = int(mies)
    dzien = int(mies)
    x = [dzien, mies, rok]
    return x


def dodanie_dnia_do_daty(data, rok):
    x = 0
    for i in range(1000):
        if data[2] % 4 == 0 and data[1] == 2 and data[0] == 28 and x == 0:
            data[0] += -1
            x += 1
            # for i in range(8):
        if data[1] == 12 and data[0] == 31:
            data[2] = data[2] + 1
            data[1] = 1
            data[0] = 1
        else:
            if data[0] == ile_dni_ma_mies[data[1]]:
                data[0] = 1
                data[1] = data[1] + 1
            else:
                data[0] = data[0] + 1
    return data


def urodziny(a, b):
    print(a)
    data = zamiana_str_data_do_tab_data(a)
    print(data)
    x = dodanie_dnia_do_daty(data,1000)
    print(x)
    data = dodanie_dnia_do_daty(x,1000)
    print(data)tr
    mies = data[3] + data[4]
    rok = data[5] + data[6] + data[7] + data[8]
    rok = int(rok)
    mies = int(mies)
    dzien = int(mies)
    x = [dzien, mies, rok]
    return x


def dodanie_dnia_do_daty(data, rok):
    x = 0
    for i in range(1000):
        if data[2] % 4 == 0 and data[1] == 2 and data[0] == 28 and x == 0:
            data[0] += -1
            x += 1
            # for i in range(8):
        if data[1] == 12 and data[0] == 31:
            data[2] = data[2] + 1
            data[1] = 1
            data[0] = 1
        else:
            if data[0] == ile_dni_ma_mies[data[1]]:
                data[0] = 1
                data[1] = data[1] + 1
            else:
                data[0] = data[0] + 1
    return data


def urodziny(a, b):
    print(a)
    data = zamiana_str_data_do_tab_data(a)
    print(data)
    x = dodanie_dnia_do_daty(data,1000)
    print(x)
    data = dodanie_dnia_do_daty(x,1000)
    print(data)tr
        if data[1] == 12 and data[0] == 31:
            data[2] = data[2] + 1
            data[1] = 1
            data[0] = 1
        else:
            if data[0] == ile_dni_ma_mies[data[1]]:
                data[0] = 1
                data[1] = data[1] + 1
            else:
                data[0] = data[0] + 1
    return data


def urodziny(a, b):
    print(a)
    data = zamiana_str_data_do_tab_data(a)
    print(data)
    x = dodanie_dnia_do_daty(data,1000)
    print(x)
    data = dodanie_dnia_do_daty(x,1000)
    print(data)tr== 31:
            data[2] = data[2] + 1
            data[1] = 1
            data[0] = 1
        else:
            if data[0] == ile_dni_ma_mies[data[1]]:
                data[0] = 1
                data[1] = data[1] + 1
            else:
                data[0] = data[0] + 1
    return data


def urodziny(a, b):
    print(a)
    data = zamiana_str_data_do_tab_data(a)
    print(data)
    x = dodanie_dnia_do_daty(data,1000)
    print(x)
    data = dodanie_dnia_do_daty(x,1000)
    print(data)tr
}


def zamiana_str_data_do_tab_data(data):
    data = list(data)
    dzien = data[1] + data[2]
    mies = data[3] + data[4]
    rok = data[5] + data[6] + data[7] + data[8]
    rok = int(rok)
    mies = int(mies)
    dzien = int(mies)
    x = [dzien, mies, rok]
    return x


def dodanie_dnia_do_daty(data, rok):
    x = 0
    for i in range(1000):
        if data[2] % 4 == 0 and data[1] == 2 and data[0] == 28 and x == 0:
            data[0] += -1
            x += 1
            # for i in range(8):
        if data[1] == 12 and data[0] == 31:
            data[2] = data[2] + 1
            data[1] = 1
            data[0] = 1
        else:
            if data[0] == ile_dni_ma_mies[data[1]]:
                data[0] = 1
                data[1] = data[1] + 1
            else:
                data[0] = data[0] + 1
    return data


def urodziny(a, b):
    print(a)
    data = zamiana_str_data_do_tab_data(a)
    print(data)
    x = dodanie_dnia_do_daty(data,1000)
    print(x)
    data = dodanie_dnia_do_daty(x,1000)
    print(data)tr


urodziny("u13022004", 1)
testy = [
    ["u06042093", 1, "u01012096"],
    ["u05041989", 1, "u31121991"]

]


def testowanie():
    for x in testy:
        msg = "ERROR", print(x[0], x[1], x[2])
        assert urodziny(x[0], x[1]) == x[2], f"blad{msg}"
# testowanie()

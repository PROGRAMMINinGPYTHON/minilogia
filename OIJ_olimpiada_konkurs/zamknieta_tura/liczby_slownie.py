def liczby_slownie(a):
    a = a.split()
    jednosci = {'jeden': "1", "dwa": "2", "trzy": "3", "cztery": "4", "piec": "5", "szesc": "6", "siedem": "7",
                "osiem": "8", "dziewiec": "9", "dziesiec": "10", "jedenascie": "11",
                "dwanascie": "12", "trzynascie": "13", "czternascie": "14", "pietnascie": "15", "szesnascie": "16",
                "siedemnascie": "17", "osiemnascie": "18", "dziewietnascie": "19", }
    dziesiatki = {"dwadziescia": "20", "trzydziesci": "30", "czterdziesci": "40", "piecdziesiat": "50",
                  "szescdziesiat": "60", "siedemdziesiat": "7", "osiemdziesiat": "80", "dziewiecdziesiat": "90", }
    setki = {"sto": "1", "dwiescie": "2", "trzysta": "3", "czterysta": "4", "piecset": "5", "szescset": "6",
             "siedemset": "7", "osiemset": "8", "dziewiecset": "9"}
    y = a
    x = [0, 0, 0]
    for i in range(0, len(y)):
        if y[i] in setki:
            setki[a[i]].split()
            x[0] = setki[a[i]]
        else:
            if y[i] in dziesiatki:
                dziesiatki[a[i]].split()
                x[1] = dziesiatki[a[i]][0]
            else:
                if y[i] in jednosci:
                    if y[i] in jednosci:
                        jednosci[a[i]].split()
                        if len(jednosci[a[i]]) == 1:
                            x[2] = jednosci[a[i]]
                        else:
                            x[1] = jednosci[a[i]][0]
                            x[2] = jednosci[a[i]][1]
    j = ""
    for i in range(3):
        x[i] = int(x[i])
    while x[0] == 0:
        x.pop(0)
    for i in range(len(x)):
        j += str(x[i])
    return j


def wczytanie():
    a = input()
    return a


# x = wczytanie()
# print(liczby_slownie(x))
# print(wczytanie())
testy = [
    ['jeden', "1"],
    ['dwa', "2"], ['trzy', '3'], ['cztery', '4'],
    ['piec', "5"], ['szesc', '6'], ['siedem', '7'],
    ['osiem', "8"], ['dziewiec', '9'], ['dziesiec', '10'],
    ["jedenascie", "11"],["dwanascie" ,"12"], ["trzynascie", "13"], ["czternascie", "14"], ["pietnascie", "15"],[ "szesnascie", "16"],
    ["siedemnascie", "17"], ["osiemnascie", "18"], ["dziewietnascie", "19"],
    ['dwa', "2"], ['trzy', '3'], ['cztery', '4'],
    ['dziesiec', "10"], ["sto", '100'], ["siedemnascie", "17"],
    ["dziewiecset dziewiecdziesiat dziewiec", "999"],["dwadziescia","20"],["dwadziescia trzy","23"],["dwadziescia piec","25"],["dwadziescia dziewiec", "29"],
    ["trzydziesci","30"],["trzydziesci trzy","33"],["trzydziesci cztery","34"],["czterdziesci","40"],["czterdziesci dwa","42"],["czterdziesci piec","45"],["piecdziesiat","50"],
    ["piecdziesiat szesc","56"],["szescdziesiat","60"],["siedemdziesiat","70"],["osiemdziesiat","80"],["dziewiecdziesiat","90"],["sto","100"],["sto jeden","101"],
    ["sto dziesiec","110"],["sto dwanascie","112"],["sto piecdziesiat szesc","156"],["sto piecdziesiat","150"],["dwiescie","200"],["dwiescie dwa","202"],
    ["dwiescie dwadziescia dwa","222"],["trzysta dwanascie","312"],["czterysta","400"],["piecset","500"],["szescset","600"],["siedemset","700"],["osiemset","800"],
    ["dziewiecset","900"],["siedemset czterdziesci","740"]



]


def testowanie():
    q = 0
    for p in testy:
        assert liczby_slownie(testy[q][0]) == testy[q][1]
        q += 1
        print(p)
    print("OK")


testowanie()

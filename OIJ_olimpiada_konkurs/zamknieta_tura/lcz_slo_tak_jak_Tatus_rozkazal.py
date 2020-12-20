def lcz_slow(a):
    a = a.split()
    print(a)
    jednosci = {'jeden': "1", "dwa": "2", "trzy": "3", "cztery": "4", "piec": "5", "szesc": "6", "siedem": "7",
                "osiem": "8", "dziewiec": "9", "dziesiec": "10", "jedenascie": "11",
                "dwanascie": "12", "trzynascie": "13", "czternascie": "14", "pietnascie": "15", "szesnascie": "16",
                "siedemnascie": "17", "osiemnascie": "18", "dziewietnascie": "19", }
    dziesiatki = {"dwadziescia": "2", "trzydziesci": "3", "czterdziesci": "4", "piecdziesiat": "5",
                  "szescdziesiat": "6", "siedemdziesiat": "7", "osiemdziesiat": "8", "dziewiecdziesiat": "9", }
    setki = {"sto": "1", "dwiescie": "2", "trzysta": "3", "czterysta": "4", "piecset": "5", "szescset": "6",
             "siedemset": "7", "osiemset": "8", "dziewiecset": "9"}
    x = []
    j = 0
    for i in range(4):
        if len(x) == 3:
            j += 2
            print(x)
            print("ddddddddddddd")
            x = []
        if a[-i - 1] in jednosci and i == 0+j:
            x.insert(0, jednosci[a[-i - 1]])
            print(jednosci[a[i - 1]])
            print(a[i - 1])
        else:
            if a[-i - 1] in dziesiatki:
                if i == 0:
                    x.append(0, 0)
                x.insert(0, dziesiatki[a[-i - 1]])

            else:
                if a[-i - 1] in setki:
                    if i == 0:
                        x.insert(0, 0)
                        x.insert(0, 0)
                    if i == 1:
                        x.insert(0, 0)
                    x.insert(0, setki[a[-i - 1]])

    print(x)


lcz_slow(input())

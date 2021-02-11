
liter_liczby = {
    "21":"a","22":"b","23":"c","24":"d","25":"e","26":"f","27":"g","28":"h","29":"i","30":"j","31":"k","32":"l","33":"m",
    "41":"n","42":"o","43":"p","44":"q","45":"r","46":"s","47":"t","48":"u","49":"v","50":"w","51":"x","52":"y","53":"z"
                }
def deszyfr(lista):
    zwrocenie = []
    for j in range(len(lista)):
        for i in range(0,len(str(lista[j]))-1,2):
            lista[j] = str(lista[j])
            x = lista[j][i] +lista[j][i+1]
            w = liter_liczby[str(x)]
            zwrocenie.append(w)
        zwrocenie.append("okej")
    zwrocenie_x = []
    a = ""
    for k in range(len(zwrocenie)-1):
        if zwrocenie[k] == "okej" and zwrocenie[k+1] != "okej":
            zwrocenie_x.append(a)
            a = ""
        else:
            a = a+zwrocenie[k]
    zwrocenie_x.append(a)
    print(zwrocenie_x)
    return zwrocenie_x
deszyfr([232821473121, 22212252, 30212729])



testy = [
    []

]


def testowanie():
    for x in testy():
        msg = "blad"
        assert testy[0] == testy[1] ,f"blad{msg}"






testy = [
    [[31452122],'["krab"]'],


]
def testowanie():
    pass
import math

def liczba(a,n):
    a = math.pow(a,1.0/n)
    print(math.floor(math.pow(a,1.0/n)))
    return int(math.floor(math.pow(a,1.0/n)))
# liczba(90972061672647417382949994702882855264900000,2)

testy = [
    [121104,2,348],
    []

]
def testowanie():
    for x in testy:
        msg = "blad"
        print(x[0])
        assert liczba(x[0],x[1]) == x[2], f"blad{msg}"

testowanie()
liczba(117649,3)
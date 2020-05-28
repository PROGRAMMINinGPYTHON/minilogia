slownik = {
    "a":"taka literka",
    "b":"literka po a",
    "c":"litera po b",
    "d":"czwarta litera w alfabecie",
    "z":"ostatnia litera alfabetu",
    "y":"przedostatnia literka alfatetu"
}
def slownik_nauka():
    for i in slownik:
        print(slownik[i])
    print(slownik["a"])
    print(slownik.keys())
    print(slownik.values())


slownik_nauka()
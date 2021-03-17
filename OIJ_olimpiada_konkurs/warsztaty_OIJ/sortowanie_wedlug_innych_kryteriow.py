

lista_str = ["acd","abc","bx","adsfsaf", "", "dsdsafsafsafsafsdafsadfdsafsdafsadfs", "aa","ab","aaa"]

def klucz(slowo):
    return (len(slowo),slowo)

print(lista_str)
print(sorted(lista_str,key=(klucz)))

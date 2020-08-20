# Wczytujemy liczbę desek.
N = int(input())

# Wczytujemy długości desek. Wszystkie elementy konwertujemy
# z napisów na liczby.
L = [int(l) for l in input().split()]

# Sortujemy długości desek używając funkcji bibliotecznej.
L.sort()

# Jeżeli desek jest mniej niz 4, to nie da sie zbudować piaskownicy.
if N < 4:
    print(0)
# W przeciwnym przypadku budowa zawsze jest możliwa.
else:
    print(L[N-4] ** 2)

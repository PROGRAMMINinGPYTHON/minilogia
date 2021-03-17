x = input()
x = x.split()
a = x[0]
b = x[1]
c = x[2]
d = x[3]
a = int(a)
b = int(b)
c = int(c)
d = int(d)
if a * b < c * d:
    print("NIE")
else:
    if max(c, d) > max(a, b):
        print("NIE")
    else:
        print("TAK")

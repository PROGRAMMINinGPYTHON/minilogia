a = input()
b = input()
b = b.split()
for q in range(len(b)):
    b[q] = int(b[q])
b.sort()
zbior = set()

for i in range(len(b)):
    if b[i] - 1 in zbior:
        if b[i] in zbior:
            zbior.add(b[i] + 1)
        else:
            zbior.add(b[i])
    else:
        zbior.add(b[i]-1)
print(len(zbior))
a = input()
b = input()
b = b.split()
for i in range(len(b)):
    b[i] = int(b[i])
ktora_operacja = 0
zbior = set()
for j in range(len(b)):
    if b[j] in zbior:
        b[j] -= 1
        if b[j] in zbior:
            b[j] += 2
            if b[j] in zbior:
                pass
    zbior.add(b[j])
lcz = len(zbior)
print(lcz)
info = {}
slownik2 = dict()

info["KLUCZ"] = "WARTOŚĆ"
print(info)

del info["KLUCZ"]
if "LG123" in info:
    del info["LG123"]


if 20 in info:
    info[20].append(50)
else:
    info [20] = [2]

info[20].append(57)
info[20].append(59)

print(info)

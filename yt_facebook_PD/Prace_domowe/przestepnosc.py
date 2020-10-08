a = int(input())
if a%4 == 0:
    if a%400 != 0 and a%100 == 0:
        print("NIE")
    else:
        print("TAK")
else:
    print("NIE")

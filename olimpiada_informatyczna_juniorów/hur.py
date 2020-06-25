x = int(input())
for i in range(1,x+1):
    if i % 7 == 0 and i % 11 == 0:
        print("Wiwat!")
    elif i % 7 == 0:
        if i == 0:
            pass
        else:
            print("Hurra!")
    elif i % 11 == 0:
        if i == 0:
            pass
        else:
            print("Super!")
    else:
        print(i)

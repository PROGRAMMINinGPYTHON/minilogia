def dukaty(ile):
    money = 0
    if ile>20:
        x = 1
    else :
        x = 0
    for i in range(ile+x):
        if (i+1)%5 == 0:
            money = money+3
        else:
            money = money+1
        if money>50:
            money = money*0.25
    print(round(money))
    return(round(money))

dukaty(6)
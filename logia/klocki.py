





def kolit(napis):
    napis = list(napis)
    x = 0
    for i in range(len(napis)):
        for j in range(i):
            if x<len(napis):
                print(napis[x],end="")
                x += 1
            else:
                pass
        print("")
kolit("ABCDEFGHIJKLMNOP")
print(int("j"))
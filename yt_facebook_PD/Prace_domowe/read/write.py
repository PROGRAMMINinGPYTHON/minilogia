
a = input()
a = list(a)

# for i in range(1+len(a)-2):
#     a.pop(i+1)

for i in range(len(a)):
    print(a[i],end = " ")
    if i+1 == len(a):
        print("")

for i in range(len(a)):
    print(a[-i-1], end=" ")
import sys
def szyfr():
    a = input()
    b = list(a)
    for i in range(len(b)):
        x = ord(b[i])
        print(chr(x+3))


szyfr()
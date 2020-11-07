from math import *
def dukaty(ile_dni):
    x = 0
    for i in range(1,ile_dni+1):
        x = x+1
        if i >1 and i%5 == 0:
            x = x+2
        if x>49:
            x = x - floor(3*(x*0.25))
    return x
dukaty(6)

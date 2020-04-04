from sortowanie_dwa import *


def test_sortowanie_dwa():
    tab = [1, 4, 2, 3]
    sortowanie(tab)
    assert tab == [1, 2, 3, 4]

def test_sortowanie_dwa_a():
    tab = [1, 4, 2, 3,6,5,8,7]
    sortowanie(tab)
    assert tab == [1,2,3,4,5,6,7,8]

def test_sortowanie_dwa_b():
    tab = [9,8,7,6,5,4,3,2,1]
    sortowanie(tab)
    assert tab == [1, 2, 3, 4,5,6,7,8,9]

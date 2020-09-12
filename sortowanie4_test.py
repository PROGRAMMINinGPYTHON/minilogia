from sortowanie_inne_1 import *

def test_sortowanie():
    tab = [3, 1]
    sortowanie(tab)
    assert tab == [1, 3]

def test_sortowanie_2():
    tab = ["a","n","b","d","auto"]
    sortowanie(tab)
    assert tab == ["a","auto","b","d","n"]

def test_sortowanie_3():
    tab = [1,3,2,4,6,5,8,7]
    sortowanie(tab)
    assert tab == [1,2,3,4,5,6,7,8]

#def test_failed():
#    tab =[1,2,4,3]
#    sortowanie(tab)
#    assert tab == [1,2,4,3]

def test_5():
    tab=[10,9,8,7,6,5,4,3,2,1]
    sortowanie(tab)
    assert tab == [1,2,3,4,5,6,7,8,9,10]

def test_4():
    tab =[]
    sortowanie(tab)
    assert tab == []

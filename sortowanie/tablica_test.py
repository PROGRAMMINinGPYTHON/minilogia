from sortowanie import *
import itertools

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

##def test_failed():
##    tab =[1,2,4,3]
##    sortowanie(tab)
##    assert tab == [1,2,4,3]

def test_5():
    tab=[10,9,8,7,6,5,4,3,2,1]
    sortowanie(tab)
    assert tab == [1,2,3,4,5,6,7,8,9,10]

def test_4():
    tab =[]
    sortowanie(tab)
    assert tab == []

def test_6():
    tab = [1,2,3,4,5]
    sortowanie(tab)
    assert tab == [1,2,3,4,5]

def test_7():
    tab = [5,2,3,4,9]
    print(tab)
    sortowanie(tab)
    print (tab)
    assert tab == [2,3,4,5,9]
    
def test_kombinacje():
    sorted = [1,2,3,4,5,6]
    all = list(itertools.permutations(sorted))
    for tuple in all:
        tab = list(tuple)
        sortowanie(tab)
        assert tab == sorted

        
    

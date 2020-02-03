def test_title():
    txt = "poszla ola do przedszkola"
    assert txt.title() == "Poszla Ola Do Przedszkola"

def test_upper():
    txt = "poszla ola do przedszkola"
    assert txt.upper() == "POSZLA OLA DO PRZEDSZKOLA"

def test_replace():
    napis="ministerstwo"
    assert napis.replace("i","d") == "mdndsterstwo"

def test_lower():
    txt = "AbCDefg"
    assert txt.lower() == "abcdefg"
    
##def test_len():
##    txt = len("tddd")
##    assert txt.len(txt) == 4


def test_len():
    dddd = "ddd"
    assert len(dddd) == 3

    
def test_count():
    napis="MINISTERSTWO DO SPRAW NIEZBYT ISTOTNYCH SPRAW"
    assert napis.count("IS") == 2



def test_strip():
    txt = 

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

def test_len():
    dddd = "ddd"
    assert len(dddd) == 3
   
def test_count():
    napis="MINISTERSTWO DO SPRAW NIEZBYT ISTOTNYCH SPRAW"
    assert napis.count("IS") == 2

def test_strip():
    txt ="  ddf"
    assert txt.strip() =="ddf"

def test_split():
    txt ="MINI AUTO"
    assert txt.split() == ['MINI' , 'AUTO']
    assert "foo;bar;baz".split() == ["foo", "bar", "baz"]

def test_indyk():
    txt = "Hello, welcome to my world."
    x = txt.index("welcome")
    assert txt.index("welcome") == 7
    assert txt.index("to") == 2

        
def test_NIE():
    txt ="MINI AUTO"
    assert not (txt.split() == ['MINI' , 'AUTO', "foo"])

def test_NIE2():
    txt = "kjsakfdj"
    assert not (txt.upper()) ==("kjsakfdj")

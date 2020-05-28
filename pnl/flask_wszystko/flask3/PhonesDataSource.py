class Phone:
    def __init__(self,nr,name,price):
        self.nr = nr
        self.name= name
        self.price = price

dane=[
    Phone(1,"Xiaomi","cheap"),
    Phone(2,"Iphone","bad for eyes"),
    Phone(3,"Samsung","medium"),
    Phone(4,"Realme","cheap")
]
def getAll():
    return dane

def getOne(nr):
    return[e for e in dane if int(e.nr)==int(nr)][0]#ta linia jest nie do końca jasna
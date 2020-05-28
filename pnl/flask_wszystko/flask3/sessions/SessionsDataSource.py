class Book:
    def __init__(self,id,name,description):
        self.id = id
        self.description = description
        self.name = name

data=[
    Book(1, 'Tomek Sayer',"książka przygodowa"),
    Book(2,'Felix Net i Nika oraz TMK',"ksiązka przygodowa"),
    Book(3,'W Pustyni I W Puszczy',"nudna książka")

]
def getAll():
    return data

def getOne(id):
    return[e for e in data if int(e.id)==int(id)][0]

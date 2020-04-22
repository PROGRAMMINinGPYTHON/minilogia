class Product:
    def __init__(self,id,name,description):
        self.id= id
        self.name = name
        self.description = description

dane= [
    Product(1,'apple',' red fruit'),
    Product(2,'orange','fruit'),
    Product(3,'car','very, cool thing')
]

def getAll():
    return dane

def getOne(id):
    return[e for e in dane if int(e.id)==int(id)][0]

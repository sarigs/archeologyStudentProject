class Basket:
    def __init__(self, Id):
        self.Id = Id


class Loci:
    def __init__(self, Id):
        self.Id = Id
        self.baskets = []
    def addBasket(self, basket):
        self.baskets
     


class Sub_type:
    def __init__(self, Id, Basket):
        self.Id = str(Id)
        self.basket = Basket


class Type:
    def __init__(self, Id, Sub_type):
        self.Id = str(Id)
        self.Sub_type = Sub_type

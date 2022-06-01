class Basket:
    def __init__(self, Id):
        self.Id = 'basket ' + str(Id)


class Loci:
    def __init__(self, Id, Basket):
        self.Id = 'locus ' + str(Id)
        self.basket = Basket


class Sub_type:
    def __init__(self, Id, Basket):
        self.Id = str(Id)
        self.basket = Basket


class Type:
    def __init__(self, Id, Sub_type):
        self.Id = str(Id)
        self.Sub_type = Sub_type

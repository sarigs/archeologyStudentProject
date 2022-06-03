
class Shard:
    def __init__(self,id, name):
        self.id = id
        self.name = name
    def __str__(self):
        return 'Shard:id=' + str(self.id) + ', name=' + str(self.name)
    def serialize(self):
        return str(self.id) + ',' + str(self.name)
    def deserialize(self, str):
        arr = str.split(',')
        return Shard(arr[0], arr[1])

class Basket:
    def __init__(self, id, datetime=None, type=None, start_height=None, close_height=None, shards={}):
        self.id = id
        self.datetime = datetime
        self.type = type
        self.start_height = start_height
        self.close_height = close_height
        self.shards = shards
    def getID(self):
        return self.id
    def __str__(self):
        return 'Basket:id=' + str(self.id) + ', Shards=' + self.shards.__str__()


class Locus:
    def __init__(self, id, type=None, height=None, baskets={}):
        self.id = id
        self.type = type
        self.height = height
        self.baskets = baskets
    def getBaskets(self):
        return self.baskets
    def __str__(self):
        return 'Locus:id=' + str(self.id) + ', Baskets=' + self.baskets.__str__()

class Area:
    def __init__(self, id, name, loci = {}):
        self.name = name
        self.id = id
        self.loci = loci
    def getLoci(self):
        return self.loci
    def __str__(self):
        return 'Area:id=' + str(self.id) + ', Loci=' + self.loci.__str__()


class Site:
    def __init__(self, id, name, areas={}, datetime=None, license_id=None):
        self.name = name
        self.id = id
        self.datetime = datetime
        self.license_id = license_id
        self.areas = areas

    def getArea(self):
        return self.areas

    def getDateTime(self):
        return self.datetime

    def __str__(self):
        return 'Site:id=' + str(self.id) + ', areas=' + self.areas.__str__()


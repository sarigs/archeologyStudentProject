# class Shard:
#     def __init__(self,id, name):
#         self.id = id
#         self.name = name
#     def __str__(self):
#         return 'Shard:id=' + str(self.id) + ', name=' + str(self.name)
#     def serialize(self):
#         return str(self.id) + ',' + str(self.name)
#     def deserialize(self, str):
#         arr = str.split(',')
#         return Shard(arr[0], arr[1])

class Site:
    def __init__(self, id, name, datetime=None, license_id=None):
        self.name = name
        self.id = id
        self.datetime = datetime
        self.license_id = license_id

    def getDateTime(self):
        return self.datetime

    def __str__(self):
        return 'Site:id='

class Locus:
    def __init__(self, id,  name):
        self.id = id
        self.name = name
    def __str__(self):
        return 'Locus:id=' + str(self.id)

class Area:
    def __init__(self, id, name):
        self.name = name
        self.id = id
    def __str__(self):
        return 'Area:id=' + str(self.id)

class Horizon:
    def __init__(self, id, name):
        self.name = name
        self.id = id
    def __str__(self):
        return 'Horizon:id=' + str(self.id)

class Basket:
    def __init__(self, id, site: Site, area: Area, locus: Locus, horizon: Horizon, type='', start_height=None, close_height=None):
        self.id = id
        self.type = type
        self.start_height = start_height
        self.close_height = close_height
        self.site = site
        self.area = area
        self.locus = locus
        self.horizon = horizon
    def __str__(self):
        return 'Basket:id=' + str(self.id) + ';area=' + str(self.area)




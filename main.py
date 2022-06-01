import datetime
import csv

class Shard:
    def __init__(self,id, name):
        self.id = id
        self.name = name
    def __str__(self):
        return 'Shard:id=' + str(self.id) + ', name=' + str(self.name)
    def serialize(self):
        return str(id) + ',' + str(name)
    def deserialize(self, str):
        arr = str.split(' ,')
        return Shard(arr[0], arr[1])
class Bascket:
    def __init__(self, id, datetime, type, start_height, close_height, shards):
        self.id = id
        self.datetime = datetime
        self.type = type
        self.start_height = start_height
        self.close_height = close_height
        self.shards = shards
class Locus:
    def __init__(self, id, type, height, basckets):
        self.id = id
        self.type = type
        self.alt = alt
        self.lat = lat
        self.height = height
        self.busckets = busckets
class Area:
    def __init__(self, name, id, locuses):
        self.name = name
        self.id = id
        self.locuses = locuses
class Site:
    def __init__(self, name, id, license_id, area):
        self.name = name
        self.id = id
        self.datetime = datetime
        self.license_id = license_id
        self.areas = areas


def read_file(fileNamePath):
    with open(fileNamePath, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i = 0
        for row in spamreader:
            if i > 10:
                break
            i += 1
            print(row)

# def insertRowIntoObjects(row):


if __name__ == '__main__':
    read_file('data.csv')
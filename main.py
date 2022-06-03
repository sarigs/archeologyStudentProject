import csv
from DataModel import *

def readFile(fileNamePath, mySite):
        f = open(fileNamePath, "r")
        i = 0
        for row in f:
            if i > 10:
                break
            i += 1
            print(row)
            if i > 1:
                populateRow2Site(row, mySite)

def populateRow2Site(row, mySite: Site):
    row_arr = row.split(',')
    area_id = row_arr[1]
    locus_id = row_arr[2]
    basket_id = row_arr[4]

    # TBD - isaac/yulia to complete
    # ...
    if area_id in mySite.areas:
        area = mySite.areas[area_id]
    else:
        area = Area(area_id, area_id)
        mySite.areas[area_id] = area

    if locus_id in mySite.areas[area_id].loci:
        locus = mySite.areas[area_id].loci[locus_id]
    else:
        locus = Locus(locus_id, locus_id)
        mySite.areas[area_id].loci[locus_id] = locus

    if basket_id in mySite.areas[area_id].loci[locus_id].baskets:
        basket = mySite.areas[area_id].loci[locus_id].baskets[basket_id]
    else:
        basket = Basket(basket_id, basket_id)
        mySite.areas[area_id].loci[locus_id].baskets[basket_id] = basket

if __name__ == '__main__':
    mySite = Site('DOR', 'DOR')
    readFile('data.csv', mySite)
    print(mySite)
    for basket in mySite.areas['D2'].loci['19736'].baskets:
        print(basket)
    print('end')
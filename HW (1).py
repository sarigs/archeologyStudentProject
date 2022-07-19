import csv
from DataModel import *
import matplotlib.pyplot as plt 

global AreaList, LocusList, WeightList

AreaList = []
LocusList = []
WeightList = []

def readFile(fileNamePath, inventory):
        f = open(fileNamePath, "r")
        i = 0
        for row in f:
            if i > 10:
                break
            i += 1
            #print(row)
            if i > 1:
                populateRow2Site(row, inventory) 

def populateRow2Site(row, inventory):
    row_arr = row.split(',')
    area_id = row_arr[1]
    locus_id = row_arr[2]
    basket_id = row_arr[4]
    weight_id = row_arr[10]
    # TBD add more attributes
    site = Site('DOR', 'DOR')
    area = Area(area_id, area_id)
    locus = Locus(locus_id, locus_id)
    weight = Weight(weight_id, weight_id)
    basket = Basket(basket_id, site, area, locus, weight)
    AreaList.append(area)
    LocusList.append(locus)
    WeightList.append(weight)

    inventory[basket_id] = basket

def getBasket(basketId, inventory):
    if basketId in inventory:
        return inventory[basketId]
    return None

def getbaskets(type, inventory):
    baskets = []
    for basket_id in inventory:
        if inventory[basket_id].type == type:
            baskets.append(inventory[basket_id])
    return baskets

def graphMaker(Xaxis, Yaxis):
    plt.plot(Xaxis, Yaxis) 
    Xaxis_type = 'Weight'
    if (Yaxis == AreaList):
        Yaxis_type = 'Area'

    else:
        Yaxis_type = 'Locus'

    plt.xlabel(Xaxis_type)
    plt.ylabel(Yaxis_type)

    plt.title(Xaxis_type + " | " + Yaxis_type) 
    plt.show() 




if name == 'main':
    INVENTORY = {}
    readFile('data.csv', INVENTORY)
    print(getBasket('195048', INVENTORY))
    print(getbaskets('Grinding stone', INVENTORY))
    graphMaker(WeightList, AreaList)
    graphMaker(WeightList, LocusList)
    print('end')
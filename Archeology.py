import csv


def readFile(fullPathFilename):
    with open(fullPathFilename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i = 0
        for row in spamreader:
            if i > 10:
                break
            i += 1
            print(row)

# def insertRowIntoObjects(row):


if __name__ == '__main__':
    readFile('data.csv')
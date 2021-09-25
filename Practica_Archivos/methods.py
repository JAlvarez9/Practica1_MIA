import csv


def readCSV():
    rows = []
    file = open('/home/josee/Documents/Archivos/Practica/ejemplo.csv')
    type(file)
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    print(header)
    for row in csvreader:
        rows.append(row)
    print(rows)
    return rows
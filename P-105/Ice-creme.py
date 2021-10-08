import csv
import numpy as np


def getDataSource(data_path):
    Ice_scream = []
    Cold_drink = []
    Temperature= []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Ice_scream.append(float(row["Ice scream sales"]))
            Cold_drink.append(float(row["Cold drink Sales"]))
            Temperature.append(float(row["Temperature"]))

    return {"x" : cups_of_coffee, "y": sleep_hours}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Ice cream and cold drink sales at differet temeparatures :-  \n--->",correlation[0,1])

def setup():
    data_path  = "Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()
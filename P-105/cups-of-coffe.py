import csv
import numpy as np


def getDataSource(data_path):
    cups_of_coffee = []
    sleep_hours = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cups_of_coffee.append(float(row["Cups Of coffee"]))
            sleep_hours.append(float(row["Hours Of sleep"]))

    return {"x" : cups_of_coffee, "y": sleep_hours}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Sleep Hours And coffee :-  \n--->",correlation[0,1])

def setup():
    data_path  = "cups of coffee vs hours of sleep.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()
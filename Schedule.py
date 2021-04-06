

import csv
import sys
import numpy as np
import pandas as pd


with open('/Users/roberthaire/Documents/Test-bar.csv', newline='') as csvfile:
    schedule = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in schedule:
        print(', '.join(row))



# df = pd.DataFram(columns = ["Name", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

df = pd.DataFrame(
    {
        "Name":["Rob", "Shelly"]
    }
)
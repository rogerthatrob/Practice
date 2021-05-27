

import csv
import sys
import numpy as np
import pandas as pd

print("hi")
# with open('/Users/roberthaire/Documents/Test-bar.csv', newline='') as csvfile:
#    schedule = csv.reader(csvfile, delimiter=' ', quotechar='|')
#    for row in schedule:
#       print(', '.join(row))

dates = pd.date_range("20130101", periods=6)

df = pd.DataFrame(
    {
        "name": ["Name", "Monday", "Tuesday"],
        "date": ["date", "date", "date"]
    }
)
print(df)

# df = pd.DataFram(columns = ["Name", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

# df = pd.DataFrame(
#     {
#         "Name":["Rob", "Shelly"],
#         "Monday": [],
#         "Tuesday": [],
#         "Wednesday": ["S1\n8pm"],
#         "Thursday": [],
#         "Friday": [],
#         "Saturday": [],
#         "Sunday": []
#     }
# )
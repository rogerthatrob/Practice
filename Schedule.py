

import csv
import sys


print("test", sys.version)
try:
    import numpy as np
    print('numpy imported\n')
except ImportError:
    print("numpy is not installed")

with open('/Users/roberthaire/Documents/Test-bar.csv', newline='') as csvfile:
    schedule = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in schedule:
        print(', '.join(row))



df = pd.DataFram(columns = ["Name", "Monday", "Tuesday"]
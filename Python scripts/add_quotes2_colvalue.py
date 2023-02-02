

'''
 - add "" to values in columns
 - This one is for the reconcile-csv troubleshooting process....
'''


import pandas as pd
import csv

df = pd.read_csv('.../nalt_labels.csv')
df.update('"' + df[['Label', 'NALT_URI']].astype(str) + '"')
df.to_csv('..../nalt_labels.csv')
print(df)

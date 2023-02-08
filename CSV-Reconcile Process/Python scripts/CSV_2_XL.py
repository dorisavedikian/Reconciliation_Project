
'''
    - Save csv as excel file
    - Creating an excel file so I can remove duplicate URI's - later I used OpenRefine to do this 
'''

import pandas as pd
import csv

cvsDataframe = pd.read_csv('.../nalt_labels.csv')           
resultExcelFile = pd.ExcelWriter('.../nalt_labels.xlsx')    
cvsDataframe.to_excel(resultExcelFile, index=False)     
resultExcelFile.save()    

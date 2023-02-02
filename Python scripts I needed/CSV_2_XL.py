
'''
    - Save csv as excel file
    - Creating an excel file so I can remove duplicate URI's - later I used OpenRefine to do this 
'''

import pandas as pd
import csv

cvsDataframe = pd.read_csv('/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation Project/reconciliation/reconciliation_data/nalt_labels.csv')           
resultExcelFile = pd.ExcelWriter('/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation Project/reconciliation/reconciliation_data/nalt_labels.xlsx')    
cvsDataframe.to_excel(resultExcelFile, index=False)     
resultExcelFile.save()    

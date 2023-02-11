
'''
    - Save csv as excel file
    - Creating an excel file so I can remove duplicate URI's - later I used OpenRefine to do this 
'''

import pandas as pd
import csv

#cvsDataframe = pd.read_csv('.../nalt_labels.csv') 
cvsDataframe = pd.read_table('/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/nalt_labels_DATA/nalt_altlabels_suffix.tsv')          
resultExcelFile = pd.ExcelWriter('/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/nalt_labels_DATA/nalt_altlabels_suffix.xlsx')    
cvsDataframe.to_excel(resultExcelFile, index=False)     
resultExcelFile.save()    

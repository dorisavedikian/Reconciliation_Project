
'''
 - Turn csv into tsv and save

import csv
csv.writer(open(".....Reconciliation_Project/csv-reconcile_process/nalt_labels_DATA/nalt_altlabels.tsv", 'w+'), delimiter='\t').writerows(csv.reader(open("..../Reconciliation_Project/csv-reconcile_process/nalt_labels_DATA/nalt_altlabels.csv")))

    - Save csv as excel file
    - Creating an excel file so I can remove duplicate URI's - later I used OpenRefine to do this 

'''

import pandas as pd
import csv

#cvsDataframe = pd.read_csv('.../nalt_labels.csv') 
cvsDataframe = pd.read_table('/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/examples/awic/sme_labels/beta_prepared.tsv')          
resultExcelFile = pd.ExcelWriter('/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/examples/awic/sme_labels/beta_prepared.xlsx')    
cvsDataframe.to_excel(resultExcelFile, index=False)     
resultExcelFile.save()    




'''
- This combines the matched alt label and pref label reconciliation outputs from openRefine into one tsv file and excel file
'''
import os
import csv
import string
import pandas as pd
import numpy as np
from pathlib import Path
from IPython.display import HTML

df1 = pd.read_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/pref_label_matched.csv")
df1['Type'] = str('skos:prefLabel')
df1['NALT_URI'] = df1['Nalt_URI']
df3 = df1.drop(['Nalt_URI'], axis=1)

df2 = pd.read_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/alt_label_matched.csv")
df2['Type'] = str('skos:altLabel')
df2[['NALT_URI', '_randomint']] = df2['Nalt_URI'].str.split('_', expand=True)         
df4 = df2.drop(['Nalt_URI','_randomint'], axis=1)    

df5 = pd.concat([df3, df4])
df6 = df5.drop(df5.iloc[:,3:11], axis=1)    
df7 = HTML(df6.to_html(render_links=True, escape=False))
df7.to_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/matched_reconciliation.csv", index=False)

cvsDataframe = pd.read_csv('/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/matched_reconciliation.csv')          
resultExcelFile = pd.ExcelWriter('/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/examples/awic/reconciled/matched_reconciliation.xlsx')    
cvsDataframe.to_excel(resultExcelFile, index=False)     
resultExcelFile.close() 

os.remove("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/matched_reconciliation.csv") 
os.remove("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/alt_label_matched.csv")
os.remove("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/alt_label_matched.xlsx")
os.remove("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/pref_label_matched.csv")

# python3 python_scripts/Results_100%_matched.py
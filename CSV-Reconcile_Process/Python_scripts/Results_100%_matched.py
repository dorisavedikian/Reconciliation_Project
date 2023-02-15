
'''
- This combines the matched alt label and pref label reconciliation outputs from openRefine into one tsv file and excel file
'''
import os
import csv
import string
import pandas as pd
import numpy as np
from pathlib import Path

df1 = pd.read_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/Biotech/Reconciled/pref_label_matched.csv")
df1['Type'] = str('skos:prefLabel')
df1['NALT_URI'] = df1['Nalt_URI']
df3 = df1.drop(['Nalt_URI'], axis=1)

df2 = pd.read_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/Biotech/Reconciled/alt_label_matched.csv")
df2['Type'] = str('skos:altLabel')
df2[['NALT_URI', '_randomint']] = df2['Nalt_URI'].str.split('_', expand=True)         
df4 = df2.drop(['Nalt_URI','_randomint'], axis=1)    

df5 = pd.concat([df3, df4])
df5.to_excel("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/examples/Biotech/reconciled/matched_reconciliation.xlsx", sheet_name='Perfect Matches', index = False)

os.remove("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/FDH/Reconciled/alt_label_matched.csv")
os.remove("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/FDH/Reconciled/pref_label_matched.csv")

# python3 python_scripts/Results_100%_matched.py
# Open Personal.xlsm, matched_reconciliation.xlsx and run the HyperAdd macros on 
# the NALT_URI column

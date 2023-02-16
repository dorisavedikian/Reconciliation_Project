
'''
- This combines the unmatched alt label and pref label reconciliation outputs from openRefine into one tsv and excel file
- Only the SME labels that score 100% but were "unmatched" during reconciliation are included
- Some SME labels will score 100% because they differ from a NALT term by only a case difference or comma, or some other minor difference.
- This also creates the list of SME labels that are not in the NALT
'''
import os
import csv
import string
import pandas as pd
import numpy as np
from pathlib import Path

df1 = pd.read_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/longer_process/Examples/Cotton/Reconciled/pref_label_unmatched.csv")                                          
df2 = pd.read_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/longer_process/Examples/Cotton/Reconciled/alt_label_unmatched.csv")   
df1['Best_Match_Type'] = str('skos:prefLabel')
df2['Best_Match_Type'] = str('skos:altLabel')
df1['NALT_URI_Best_Match'] = df1['Nalt_URI_Best_Match']
df7 = df1.drop(['Nalt_URI_Best_Match'], axis=1)
df2[['NALT_URI_Best_Match', '_randomint']] = df2['Nalt_URI_Best_Match'].str.split('_', expand=True)         
df4 = df2.drop(['Nalt_URI_Best_Match','_randomint'], axis=1)
df3 = pd.concat([df7, df4])    
df5 = df3.loc[df3['Score'] == 100] 
#df6 = df5.drop_duplicates(keep='first')
df5.to_excel('/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/longer_process/examples/Cotton/reconciled/unmatched_but_100.xlsx', sheet_name='Look up Best_Match', index=False) 
    
df8 = df3.loc[df3['Score'] < 100] 
#df9 = df8.drop_duplicates(keep='first')
df8.to_excel("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/longer_process/Examples/Cotton/Reconciled/SME_Label_Not_In_The_NALT.xlsx", sheet_name = 'Not in Nalt', index=False)
   
#os.remove("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/longer_process/Examples/Biotech/Reconciled/pref_label_unmatched.csv")
#os.remove("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/longer_process/Examples/Biotech/Reconciled/alt_label_unmatched.csv")


# python3 longer_process/python_scripts/Results_100%_unmatched.py
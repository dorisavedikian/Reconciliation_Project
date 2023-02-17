
'''
- This edits the Matched output and saves it as an excel file
'''
import os
import csv
import pandas as pd
import numpy as np
import string

df = pd.read_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/shorter_process/Examples/FDH/Reconciled/label_matched.csv")
df[['NALT_URI_Best_Match', '_randomint']] = df['Nalt_URI'].str.split('_', expand=True)         
df1 = df.drop(['Nalt_URI','_randomint'], axis=1)    
df1.to_excel("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/shorter_process/examples/FDH/reconciled/matched_reconciliation.xlsx", sheet_name='Perfect Matches', index = False)

df2 = pd.read_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/shorter_process/Examples/FDH/Reconciled/label_unmatched.csv")                                          
df2[['NALT_URI_Best_Match', '_randomint']] = df2['Nalt_URI'].str.split('_', expand=True)         
df3 = df2.drop(['Nalt_URI','_randomint'], axis=1)    
df4 = df3.loc[df3['Score'] == 100] 
df4.to_excel('/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/shorter_process/examples/FDH/reconciled/Unmatched_but_100%.xlsx', sheet_name='Look up Best_Match', index=False) 
df5 = df3.loc[df3['Score'] < 100]    
df5.to_excel("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/shorter_process/Examples/FDH/Reconciled/Labels_Not_In_NALT.xlsx", sheet_name = 'Not in Nalt', index=False) 

#os.remove("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/shorter_process/Examples/Biotech/Reconciled/label_unmatched.csv")
#os.remove("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/shorter_process/Examples/ADC/Reconciled/label_matched.csv")

# python3 shorter_process/python_scripts/Matches.py


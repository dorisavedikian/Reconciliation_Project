
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

df1 = pd.read_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/pref_label_unmatched_100.csv")                                          
df2 = pd.read_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/alt_label_unmatched.csv")   
df3 = pd.concat([df1, df2])
df4 = df3.drop(df3.iloc[:,3:11], axis=1)    
df5 = df4.loc[df4['Score'] == 100] 
df6 = df5.drop_duplicates(keep='first')
df6.to_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/unmatched_but100_recon.csv", index=False)

df2 = pd.read_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/alt_label_unmatched.csv")   
df7 = df2.drop(df2.iloc[:,3:11], axis=1)    
df8 = df7.loc[df7['Score'] < 100] 
df9 = df8.drop_duplicates(keep='first')
df9.to_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/SME_Label_Not_In_The_NALT.csv", index=False)

cvsDataframe = pd.read_csv('/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/unmatched_but100_recon.csv')          
resultExcelFile = pd.ExcelWriter('/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/examples/awic/reconciled/unmatched_but100_recon.xlsx')    
cvsDataframe.to_excel(resultExcelFile, index=False)     
resultExcelFile.close() 

os.remove("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/pref_label_unmatched_100.csv")
os.remove("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/alt_label_unmatched.csv")
os.remove("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/alt_label_unmatched.xlsx")
os.remove("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/unmatched_but100_recon.csv")

print('This dataframe are all the SME labels that scored 100% but were "unmatched" during reconciliation.')
print('So for this reason, there is no URI because there is no NALT term that EXACTLY matches these labels.')
print('However, these SME labels differ from actual NALT terms by only a case difference, additional comma or some other minor difference.')
print('These are the ones that we would need to manually look up.')


# python3 python_scripts/Results_100%_unmatched.py
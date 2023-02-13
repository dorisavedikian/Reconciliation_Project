'''
- This seperates the unmatched output of the pref label reconciliation into two data frames; 1) unmatched but 100% & 2) unmatched and < 100% 
- The data frame that is unmatched and < 100% will be used as the new SME list of labels that will be reconciled to the alt_labels_suffix.tsv
'''
import os
import csv
import pandas as pd

df = pd.read_csv('/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/pref_label_unmatched.csv')
df1 = df.drop(df.iloc[:,3:12], axis=1)
df2 = df1.loc[df1['Score'] == 100] 
df3 = df1.loc[df1['Score'] < 100]
df4 = df3.drop(['Score'], axis=1) 

df2.to_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/pref_label_unmatched_100.csv", index=False)
df4.to_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/SME_labels/beta_prepared_2.tsv", sep="\t", index=False)

os.remove('/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/pref_label_unmatched.xlsx')
os.remove('/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/pref_label_unmatched.csv')

# python3 python_scripts/pref_label_unmatched.py

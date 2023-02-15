'''
- This seperates the unmatched output of the pref label reconciliation into two data frames; 1) unmatched but 100% & 2) unmatched and < 100% 
- The data frame that is unmatched and < 100% will be used as the new SME list of labels that will be reconciled to the alt_labels_suffix.tsv
'''
import os
import csv
import pandas as pd

df = pd.read_csv('/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/ADC/Reconciled/unmatched_pref_label.csv')

df2 = df.loc[df['Score'] == 100] 
df2.to_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/ADC/Reconciled/pref_label_unmatched.csv", index=False)

df3 = df.loc[df['Score'] < 100]
df4 = df3.drop(['Score'], axis=1) 
df4.to_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/ADC/SME_labels/ADC_2.tsv", sep="\t", index=False)

#os.remove('/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/Biotech/Reconciled/unmatched_pref_label.csv')

# python3 python_scripts/unmatched_pref_label.py

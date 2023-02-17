
'''
- This edits the Matched and Unmatched OpenRefine output's (removes suffix, seperates based on score) and saves it as an excel file
'''
import os
import csv
import pandas as pd
import numpy as np
import string

df1 = pd.read_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/shorter_process/Examples/FDH/Reconciled/label_matched.csv")
df2 = pd.read_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/shorter_process/Examples/FDH/Reconciled/label_unmatched.csv")                   
df1.drop_duplicates(subset=['Label'], keep='first')
df2.drop_duplicates(subset=['Label'], keep='first')

df1[['NALT_URI_Best_Match', '_randomint']] = df1['Nalt_URI'].str.split('_', expand=True)         
df_1 = df1.drop(['Nalt_URI','_randomint'], axis=1)  
df3 = df_1.loc[df_1['Score'] == 100] 
df3['Label = Best_Match'] = np.where((df3['Label'] == df3['Best_Match']), True, False)

df2[['NALT_URI_Best_Match', '_randomint']] = df2['Nalt_URI'].str.split('_', expand=True)         
df_2 = df2.drop(['Nalt_URI','_randomint'], axis=1)
df4 = df_2.loc[df_2['Score'] < 100]  
df4 = df4.round({'Score': 0})
df4.sort_values(by=['Score'], ascending = False)

writer = pd.ExcelWriter('/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/shorter_process/Examples/FDH/Reconciled/Reconciliation.xlsx', engine = 'xlsxwriter')
df_1.to_excel(writer, sheet_name='Matched & 100%', index = False)
df3.to_excel(writer, sheet_name='Unmatched but 100%', index=False) 
df4.to_excel(writer, sheet_name = 'Unmatched & < 100%', index=False) 
writer.close()

#os.remove("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/shorter_process/Examples/Biotech/Reconciled/label_unmatched.csv")
#os.remove("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/shorter_process/Examples/ADC/Reconciled/label_matched.csv")

# python3 shorter_process/python_scripts/Matches.py


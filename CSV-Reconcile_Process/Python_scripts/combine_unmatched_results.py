
'''
- This combines the unmatched alt label and pref label reconciliation outputs from openRefine into one tsv file
- Only the SME labels that were "unmatched" but scored 100% are included
- This is created because some labels will score 100% because they are different due to a case difference or a comma
'''

import csv
import string
import pandas as pd
import numpy as np
from pathlib import Path

df1 = pd.read_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/pref_label_unmatched.csv")
df1.loc[df1['Score'] == 100]              # Select rows that contain score = 100 only

df2 = pd.read_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/alt_label_unmatched.csv")
df2.loc[df2['Score'] == 100]
df2['Nalt_URI'] = df2['Nalt_URI_suffix'].str[:-7]           # Remove last 7 char 
df2.drop(['NALT_URI_suffix'], axis=1)    

labels_directory = "reconciled_labels"
Path(labels_directory).mkdir(exist_ok=True)
labels_csvfile = Path(labels_directory) / "unmatched_labels_withperfectscore.tsv"

with open(labels_csvfile, 'w', newline='') as csvfile:
    df3 = pd.concat([df1, df2])
    df3.to_csv(csvfile, sep="\t")

print('Please note, if the Nalt_URI column is empty in this dataframe...It is because there exists a nalt term that differs slightly from the SME proposed label (ie, a case difference, an additional comma, etc.')
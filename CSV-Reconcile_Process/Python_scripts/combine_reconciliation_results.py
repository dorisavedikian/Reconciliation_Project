
'''
- This combines the reconciliation outputs from openRefine into one tsv file
- Only the SME labels that have a reconciliation score of 100% are collected into this new
'''

import csv
import string
import pandas as pd
import numpy as np
from pathlib import Path

df1 = pd.read_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/pref_label_reconciliation.csv")
df1['Type'] = str('skos:prefLabel')
df1.loc[df1['Score'] == 100]              # Select rows that contain score = 100 only

df2 = pd.read_csv("....csv)
df2['Type'] = str('skos:altLabel')
df2.loc[df2['Score'] == 100]
df3['Nalt_URI'] = df2['Nalt_URI_suffix'].str[:-5]     # Remove last 5 char 

labels_directory = "reconciled_labels"
Path(labels_directory).mkdir(exist_ok=True)
labels_csvfile = Path(labels_directory) / "reconciled_labels.tsv"

with open(labels_csvfile, 'w', newline='') as csvfile:
    df4 = pd.concat([df1, df3])
    df4.to_csv(csvfile, sep="\t")

print('Please note, if the Nalt_URI column is empty in this dataframe...It is because there exists a nalt term that differs slightly from the SME proposed label (ie, a case difference, an additional comma, etc.')

'''
- This combines the matched alt label and pref label reconciliation outputs from openRefine into one tsv file
'''


import csv
import string
import pandas as pd
import numpy as np
from pathlib import Path

df1 = pd.read_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/pref_label_matched.csv")
df2 = pd.read_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/alt_label_matched.csv")
df1['Type'] = str('skos:prefLabel')
df2['Type'] = str('skos:altLabel')
df2['Nalt_URI'] = df2['Nalt_URI_suffix'].str[:-7]       # Remove last 7 char 
df2.drop(['NALT_URI_suffix'], axis=1)    

labels_directory = "Reconciled"
Path(labels_directory).mkdir(exist_ok=True)
labels_csvfile = Path(labels_directory) / "matched_labels.tsv"

with open(labels_csvfile, 'w', newline='') as csvfile:
    df3 = pd.concat([df1, df2])
    df3.to_csv(csvfile, sep="\t")

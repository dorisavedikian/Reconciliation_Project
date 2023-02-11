
'''
-
'''

import csv
import string
import pandas as pd
import numpy as np
from pathlib import Path

df = pd.read_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/Reconciled/pref_label_reconciliation.csv")
df['Type'] = str('skos:prefLabel')
df.loc[df['Score'] == 100]              # Select rows that contain score = 100 only

df2 = pd.read_csv("....csv)
df2['Type'] = str('skos:altLabel')
df2.loc[df['Score'] == 100]


df2.to_csv("....tsv", sep="\t")

labels_directory = "reconciled_labels"
Path(labels_directory).mkdir(exist_ok=True)
labels_csvfile = Path(labels_directory) / "reconciled_labels.tsv"

with open(labels_csvfile, 'w', newline='') as csvfile:


print('Please note, if the Nalt_URI column is empty in this dataframe...It is because there exists a nalt term that differs slightly from the proposed label (ie, case difference, additional comma, etc.')
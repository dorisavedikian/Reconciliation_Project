
'''
 - I used Tom Bakers nalt_label.ipynb to create this script
 - This collects all the altlabel values and URI's only and saves it as a tsv file
 - Adds a column "NALT_URI_suffix" to the nalt_altlabel.tsv - this column is the column 'Nalt_URI' with a suffix added 
'''

import csv
import pandas as pd
import numpy as np
import random
import string
from pathlib import Path
from rdflib import Graph, SKOS

labels_directory = "CSV-Reconcile_Process/nalt_labels_DATA"
Path(labels_directory).mkdir(exist_ok=True)
labels_csvfile = Path(labels_directory) / "nalt_altlabels.tsv"

n = Graph()
n.parse('/Volumes/USDA HD/NAL/MyGitFolder/NALT/nalt4ma/nalt/nalt.nt', format='nt11')
# n.parse('.../nalt4ma/nalt/nalt.nt', format='nt11')

labels_tuples = []

for predicate in [SKOS.altLabel]:
    for (concept, label) in n.subject_objects(predicate):
        if label.language == "en":
            labels_tuples.append((str(concept), label.value))

with open(labels_csvfile, 'w', newline='') as csvfile:
    labelwriter = csv.writer(csvfile, delimiter='\t', dialect='excel')
    labelwriter.writerow(('NALT_URI', 'Label'))
    for line in sorted(labels_tuples):
        labelwriter.writerow(line)
    
# Add column "Nalt_URI_suffix" to data frame
df = pd.read_table("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/nalt_labels_DATA/nalt_altlabels.tsv")
df['randomint'] = np.random.randint(1000, 5000, size=len(df))
for Nalt_URI in df:
    df['Nalt_URI_suffix'] = df.loc[:,'NALT_URI'].astype(str) + '_' + df.loc[:,'randomint'].astype(str)
df1 = df.drop(["randomint"], axis=1)
df1.to_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/AWIC/nalt_labels_DATA/nalt_altlabels_suffix.tsv", sep="\t")

# Removes last 5 characters of the 'Nalt_URI_suffix' column - do this after reconciliation
# df['Nalt_URI_suffix'] = df['Nalt_URI_suffix'].str[:-5]

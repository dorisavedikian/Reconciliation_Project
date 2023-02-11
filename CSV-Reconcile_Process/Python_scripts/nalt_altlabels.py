
'''
 - I used Tom Bakers nalt_label.ipynb to create this script
 - This collects all the altlabel values and URI's in the NALT and saves it as a tsv file
 - Also, adds a column "NALT_URI_suffix" to the nalt_altlabel.tsv - this new column is the column 'Nalt_URI' with a random suffix added 
'''

import csv
import string
import pandas as pd
import numpy as np
from pathlib import Path
from rdflib import Graph, SKOS

labels_directory = "nalt_labels_DATA"
Path(labels_directory).mkdir(exist_ok=True)
labels_csvfile = Path(labels_directory) / "nalt_altlabels.tsv"
n = Graph()
n.parse('/Volumes/USDA HD/NAL/MyGitFolder/NALT/nalt4ma/nalt/nalt.nt', format='nt11')
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
 
# Add column "Nalt_URI_suffix" to data frame so URI's are unique
df = pd.read_table("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/nalt_labels_DATA/nalt_altlabels.tsv")
df['randomint'] = np.random.randint(10, 10000, size=len(df))  
df['Nalt_URI_suffix'] = df.loc[:,'NALT_URI'].astype(str) + '_' + df.loc[:,'randomint'].astype(str)
df1 = df.drop(['randomint', 'NALT_URI'], axis=1)    # is this really necessary?
df2 = df[['Nalt_URI_suffix', 'Label']]              # is this really necessary?
df2.to_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/nalt_labels_DATA/nalt_altlabels_suffix.tsv", sep="\t", index=False)


# python3 python_scripts/nalt_altlabels.py
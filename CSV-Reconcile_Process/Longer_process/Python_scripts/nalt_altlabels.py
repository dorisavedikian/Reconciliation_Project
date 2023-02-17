
'''
 - I used Tom Bakers nalt_label.ipynb to create this script
 - This collects all the altlabel values and URI's in the NALT and saves it as a tsv file
 - Also, adds a column "NALT_URI_suffix" - this new column is the column 'Nalt_URI' with a random suffix added 
'''
import csv
import string
import numpy as np
from pathlib import Path
from rdflib import Graph, SKOS

labels_directory = "longer_process/nalt_labels_DATA"
Path(labels_directory).mkdir(exist_ok=True)
labels_csvfile = Path(labels_directory) / "nalt_altlabels_suffix.tsv"

n = Graph()
n.parse('/Volumes/USDA HD/NAL/MyGitFolder/NALT/nalt4ma/nalt/nalt.nt', format='nt11')

labels_tuples = []

for predicate in [SKOS.altLabel]:
    for (concept, label) in n.subject_objects(predicate):
        if label.language == "en":
            labels_tuples.append((str(concept), str(concept) + '_' + str(np.random.randint(1,100000000)), label.value))

with open(labels_csvfile, 'w', newline='') as csvfile:
    labelwriter = csv.writer(csvfile, delimiter='\t', dialect='excel')
    labelwriter.writerow(('NALT_URI', 'NALT_URI_Suffix', 'Label'))
    for line in sorted(labels_tuples):
        labelwriter.writerow(line)

# python3 longer_process/python_scripts/nalt_altlabels.py



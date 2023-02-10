
'''
 - I used Tom Bakers nalt_label.ipynb to create this 
 - This collects all the preflabel values and URI's instead of the altlabels and the preflabels values and URI's
'''

import csv
from pathlib import Path
from rdflib import Graph, SKOS

#labels_directory = "CSV-Reconcile_Process/Examples/AWIC/nalt_labels_DATA"
labels_directory = "CSV-Reconcile_Process/Examples/AWIC/nalt_labels_DATA"
Path(labels_directory).mkdir(exist_ok=True)
labels_csvfile = Path(labels_directory) / "nalt_preflabels.tsv"

n = Graph()
n.parse('/Volumes/USDA HD/NAL/MyGitFolder/NALT/nalt4ma/nalt/nalt.nt', format='nt11')
# n.parse('.../nalt4ma/nalt/nalt.nt', format='nt11')

labels_tuples = []

for predicate in [SKOS.prefLabel]:
    for (concept, label) in n.subject_objects(predicate):
        if label.language == "en":
            labels_tuples.append((str(concept), label.value))

with open(labels_csvfile, 'w', newline='') as csvfile:
    labelwriter = csv.writer(csvfile, delimiter='\t', dialect='excel')
    labelwriter.writerow(('NALT_URI', 'Label'))
    for line in sorted(labels_tuples):
        labelwriter.writerow(line)
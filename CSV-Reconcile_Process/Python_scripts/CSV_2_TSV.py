
'''
 - Turn csv into tsv and save
'''

import csv


csv.writer(open(".....Reconciliation_Project/nalt_labels_DATA/nalt_altlabels_numbered.tsv", 'w+'), delimiter='\t').writerows(csv.reader(open("..../Reconciliation_Project/nalt_labels_DATA/nalt_altlabels_numbered.csv")))

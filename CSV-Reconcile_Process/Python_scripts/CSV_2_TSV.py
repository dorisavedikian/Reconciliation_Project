
'''
 - Turn csv into tsv and save
'''

import csv


csv.writer(open(".....Reconciliation_Project/csv-reconcile_process/nalt_labels_DATA/nalt_altlabels.tsv", 'w+'), delimiter='\t').writerows(csv.reader(open("..../Reconciliation_Project/csv-reconcile_process/nalt_labels_DATA/nalt_altlabels.csv")))

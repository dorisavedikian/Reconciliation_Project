
'''
 - Turn csv into tsv and save
'''

import csv


csv.writer(open("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/nalt_labels_DATA/nalt_altlabels_1stsplit.tsv", 'w+'), delimiter='\t').writerows(csv.reader(open("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/nalt_labels_DATA/nalt_altlabels_1.csv")))

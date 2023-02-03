
'''
 - Turn csv into tsv and save
'''

import csv


csv.writer(open("..../nalt_altlabels1.tsv", 'w+'), delimiter='\t').writerows(csv.reader(open("..../nalt_altlabel1.csv")))

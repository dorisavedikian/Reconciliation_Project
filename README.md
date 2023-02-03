# Reconciliation_Project


$ This Repo is to document the reconciliation process. $

Original nalt_label.tsv file has 145,755 rows

After splitting it into two files...the nalt_preflabel.tsv and nalt_altlabel.tsv each file had the following # of rows...

- nalt_preflabel.tsv had 76,932 rows ---> reconciled to beta prepared.tsv resulted in 739 reconciled nalt terms

- nalt_altlabel.tsv had 68,823 rows ----> 37,105 were matching rows....

After removing the mathcing rows I reconciled the other 31,718 rows / alt labels to the beta prepared demo data & I was able to reconcile another 3 nalt terms to the beta prepared demo data...

Currently trying to figure out how to reconcile the beta prepared demo data to all of the nalt_altlabels.tsv - this file still has a lot of duplicate URI's...there are many concepts with > 1 alt label....Some concepts have 20 alt labels...

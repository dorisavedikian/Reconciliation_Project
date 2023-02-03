# Reconciliation_Project


This Repo is to document the reconciliation process.

UNDER CONSTRUCTION

Currently trying to figure out how to reconcile the beta prepared demo data to the nalt_altlabels.tsv - this file still has a lot of duplicate URI's...there are many concepts with > 1 alt label....Some concepts have 20 alt labels...

So far, using only the nalt_preflabels.tsv to reconcile the beta prep demo data, I was able to reconcile 739 of the 908 terms to nalt concepts...
However, the beta prepared demo data has been reconciled before and the expectation is that 748 of the beta prepared terms reconcile to the nalt....

I tried reconciling the beta prepared labels to the nalt_altlabels.tsv after removing the duplicates in openRefine and was able to reconcile 3 more of the beta prepared proposed labels to the nalt...but this method still leaves me with still needing to reconcile the beta prepared labels to 31,718 alt labels....


Original nalt_label.tsv file has 145,755 rows

After splitting it into two files; nalt_preflabel.tsv and nalt_altlabel.tsv each file had the following # of rows...

nalt_preflabel.tsv had 76,932 rows

nalt_altlabel.tsv had 68,823 rows

The nalt_prelabel.tsv had unique URI's in the nalt_uri column
However, the nalt_allabel.tsv has 37,105 matching rows....
After removing the mathcing rows I reconciled the other 31,718 rows / alt labels and URI's to the beta prepared demo data 
I was able to reconcile another 3 nalt terms to the beta prepared demo data...


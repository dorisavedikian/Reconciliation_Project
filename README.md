# Reconciliation_Project


## This  Repo  is  to  document  the  reconciliation  process. 

Original [nalt_label.tsv](https://github.com/dorisavedikian/Reconciliation_Project/blob/main/nalt_labels_DATA/nalt_labels.tsv) file has 145,755 rows

After splitting it into two files...

- nalt_preflabel.tsv had 76,932 rows ---> reconciled to beta prepared.tsv resulted in [739 reconciled nalt terms](https://github.com/dorisavedikian/Reconciliation_Project/blob/main/Reconciled/beta%20prepared%20pref_labels_only_reconciled.xls)

- nalt_altlabel.tsv had 68,823 rows ----> 37,105 were matching rows....

After removing the mathcing rows I reconciled the other 31,718 rows / alt labels to the beta prepared demo data & I was able to [reconcile another 3 nalt terms](https://github.com/dorisavedikian/Reconciliation_Project/blob/main/Reconciled/beta%20prepared%20altlabels1stsplit.xls) to the beta prepared demo data...

Currently trying to figure out how to reconcile the beta prepared demo data to *all* of the nalt_altlabels.tsv - this file still has a lot of duplicate URI's...there are many concepts with > 10 alt labels...

![Screen Shot 2023-02-02 at 6 26 31 PM](https://user-images.githubusercontent.com/109038399/216520217-41cb1682-0fc8-44a4-a2b3-f9f1eb47a341.png)


Ok, so I added a suffix to the URI's for all of the alt_labels so that I can run the service - it worked!!!!! 


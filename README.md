# Reconciliation_Project


## This  Repo  is  to  document  the  reconciliation  process. 

Original [nalt_label.tsv](https://github.com/dorisavedikian/Reconciliation_Project/blob/main/nalt_labels_DATA/nalt_labels.tsv) file has 145,755 rows

After splitting it into two files...

- nalt_preflabel_only.tsv had 76,932 rows ---> reconciled to beta prepared.tsv resulted in [742 reconciled nalt terms]()

- nalt_altlabel_only_withsuffix.tsv had 68,823 rows ----> I added a suffix to each URI so they would be considered unique and I ran the service and it worked. 5 beta prepared labels were reconciled to [5 pref labels in the nalt.]()


I aggregated the outputs and there are 747 nalt terms in the beta prepared csv - which is what was expected per the beta prepared reconciliation I have as a reference.


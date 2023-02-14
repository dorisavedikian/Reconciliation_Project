# This  repo  is  to  document  the  reconciliation  process. 

Original [nalt_label.tsv](https://github.com/woody544/nalt4ma/blob/main/nalt/nalt_labels/nalt_labels.tsv) file has 145,755 rows. Because alt and pref labels that correspond to a given concept / resource has the same URI, the openRefine reconciliation service [CSV-Reconcile](https://github.com/gitonthescene/csv-reconcile) will not work. However, if the SME labels are reconciled to alt labels and pref labels seperately than the CSV-Reconcile service can be used.

Everytime the NALT gets updated the following two files should be created using a derivative of Tom Baker's [nalt_labels.ipynb](https://github.com/woody544/nalt4ma/blob/main/nalt/nalt_labels.ipynb) jupiter notebook so that the [pref labels](https://github.com/dorisavedikian/Reconciliation_Project/blob/main/CSV-Reconcile_Process/Python_scripts/nalt_preflabels.py) and [alt labels](https://github.com/dorisavedikian/Reconciliation_Project/blob/main/CSV-Reconcile_Process/Python_scripts/nalt_altlabels.py) are seperated 

After splitting it into two files...

- [nalt_preflabel.tsv](https://github.com/dorisavedikian/Reconciliation_Project/blob/main/CSV-Reconcile_Process/nalt_labels_DATA/nalt_preflabels.tsv) currently has 76,932 rows -----> Should always equal the # of concepts unless there is a concept that doesnt have an english preflabel

- [nalt_altlabel_suffix.tsv](https://github.com/dorisavedikian/Reconciliation_Project/blob/main/CSV-Reconcile_Process/nalt_labels_DATA/nalt_altlabels_suffix.tsv) had 68,823 rows ----> An additional column "Nalt_URI_suffix" was added so the duplicate URI's will be considered unique. 





### The overall process:

![Screen Shot 2023-02-13 at 4 41 21 PM](https://user-images.githubusercontent.com/109038399/218608369-2e5922f8-7860-49bf-9aff-b798df206506.png)

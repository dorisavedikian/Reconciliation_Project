# This  repo  is  to  document the reconciliation process using OpenRefine and the reconciliation service [csv-reconcile](https://github.com/gitonthescene/csv-reconcile) 

Original [nalt_label.tsv](https://github.com/woody544/nalt4ma/blob/main/nalt/nalt_labels/nalt_labels.tsv) file has 145,755 rows. Because alt and pref labels that correspond to a given concept / resource has the same URI, the openRefine reconciliation service [CSV-Reconcile]will not work. However, if we temporarily make the URI's unique by adding a suffix to the URI using a derivative of Tom Baker's [Jupyter notebook](https://github.com/dorisavedikian/Reconciliation_Project/blob/main/CSV-Reconcile_Process/Shorter_process/Python_scripts/nalt_label.py) the process works. 





## The overall process:
![Screen Shot 2023-02-16 at5 10 49 PM](https://user-images.githubusercontent.com/109038399/219524268-e70c9bde-9355-4576-b5b7-f8c18d20cc92.png)

1. [Add suffix to nalt URI's](https://github.com/dorisavedikian/Reconciliation_Project/blob/main/CSV-Reconcile_Process/Shorter_process/Python_scripts/nalt_label.py)
2. [Run reconciliation in OpenRefine](https://github.com/dorisavedikian/Reconciliation_Project/blob/main/CSV-Reconcile_Process/Notes/Notes_csv-reconcile)
3. Run [script](https://github.com/dorisavedikian/Reconciliation_Project/blob/main/CSV-Reconcile_Process/Shorter_process/Python_scripts/Matches.py) on reconciliation output

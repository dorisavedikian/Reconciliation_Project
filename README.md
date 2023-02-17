# This  repo  is  to  document  the  reconciliation  process. 

Original [nalt_label.tsv](https://github.com/woody544/nalt4ma/blob/main/nalt/nalt_labels/nalt_labels.tsv) file has 145,755 rows. Because alt and pref labels that correspond to a given concept / resource has the same URI, the openRefine reconciliation service [CSV-Reconcile](https://github.com/gitonthescene/csv-reconcile) will not work. However, if we temporarily make the URI's unique by adding a suffix to the URI the process works.


## The overall process:

![Screen Shot 2023-02-13 at 4 41 21 PM](https://user-images.githubusercontent.com/109038399/218608369-2e5922f8-7860-49bf-9aff-b798df206506.png)

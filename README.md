## This  repo  is  to  document  the  reconciliation  process. 

Original [nalt_label.tsv](https://github.com/woody544/nalt4ma/blob/main/nalt/nalt_labels/nalt_labels.tsv) file has 145,755 rows. Because alt and pref labels that correspond to a given concept / resource has the same URI, the openRefine reconciliation service (CSV-Reconcile) will not work. 

So, everytime the NALT gets updated the following two files should be created using a derivative of Tom Baker's [nalt_labels.ipynb](https://github.com/woody544/nalt4ma/blob/main/nalt/nalt_labels.ipynb) jupiter notebook so that the [pref labels](https://github.com/dorisavedikian/Reconciliation_Project/blob/main/CSV-Reconcile_Process/Python_scripts/nalt_preflabels.py) and [alt labels](https://github.com/dorisavedikian/Reconciliation_Project/blob/main/CSV-Reconcile_Process/Python_scripts/nalt_altlabels.py) are seperated 

After splitting it into two files...

- [nalt_preflabel.tsv](https://github.com/dorisavedikian/Reconciliation_Project/blob/main/CSV-Reconcile_Process/nalt_labels_DATA/nalt_preflabels.tsv) currently has 76,932 rows -----> Should always equal the # of concepts unless there is a concept that doesnt have an english preflabel

- [nalt_altlabel_suffix.tsv](https://github.com/dorisavedikian/Reconciliation_Project/blob/main/CSV-Reconcile_Process/nalt_labels_DATA/nalt_altlabels_suffix.tsv) had 68,823 rows ----> An additional column "Nalt_URI_suffix" was added so the duplicate URI's will be considered unique 


---------------------------------------------------------------------------------------------------------------------------------------------------------
Pre Reconciliation Process:
- [Remove duplicates from the SME prepared labels list using openRefine](https://guides.library.illinois.edu/openrefine/duplicates)
- [Create tsv of original SME labels list for post reconciliation process](https://github.com/dorisavedikian/Reconciliation_Project/blob/main/CSV-Reconcile_Process/Python_scripts/CSV_2_TSV.py)

Post reconciliation process:
- In openRefine: Double check the unmatched labels by seperating the reconciliation into two seperate excel files / outputs ("matched" and "unmatched"), than use excel to filter the Score column in the "unmatched" version....If there are perfect matches that for some minor reason (ie, a comma, dash or case difference) did not get matched, it will score 100% but it might not get "matched"....check to see if these were already matched as a pref label / alt label....sometimes these subtle differences is what differentiaties between the alt label and pref label....
- Combine all the matching labels using this script [here](https://github.com/dorisavedikian/Reconciliation_Project/blob/main/CSV-Reconcile_Process/Python_scripts/combine_matchedlabels.py) into one database and save as a tsv and csv. 
- Reconcile the original list of proposed labels to the list of matched labels using openRefine - the unmatched list are the terms not in the NALT


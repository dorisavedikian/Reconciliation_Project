# UNDER CONSTRUCTION...the process works but still couple more things to do...see bottom for list...

## This  Repo  is  to  document  the  reconciliation  process. 

Original [nalt_label_ALL.tsv]() file has 145,755 rows. Because alt and pref labels that correspond to a given concept / resource has the same URI, the openRefine reconciliation service will not work. 

So, everytime the NALT gets updated the following two files should be created using a derivative of Tom Baker's [nalt_label.ipynb](https://github.com/woody544/nalt4ma/blob/main/nalt/nalt_labels.ipynb) jupiter notebook so that the pref labels and alt labels are seperated - otherwise CSV-Reconcile reconciliation service will not work.  
After splitting it into two files...

- [nalt_preflabel.tsv]() currently has 76,932 rows -----> Should always equal the # of concepts unless there is a concept that isnt in english

- [nalt_altlabel_withsuffix.tsv]() had 68,823 rows ----> Must add a suffix to each URI using this script [here]() so the duplicate URI's will be considered unique 


---------------------------------------------------------------------------------------------------------------------------------------------------------
Pre Reconciliation Process:
- Remove duplicates from the SME prepared labels list using openRefine
- Create tsv of original SME labels list for post reconciliation process

Post reconciliation process:
- In openRefine: Double check the unmatched labels by seperating the reconciliation into two seperate excel files / outputs ("matched" and "unmatched"), than use excel to filter the Score column in the "unmatched" version....If there are perfect matches that for some minor reason (ie, a comma, dash or case difference) did not get matched, it will score 100% but it might not get "matched"....check to see if these were already matched as a pref label / alt label....sometimes these subtle differences is what differentiaties between the alt label and pref label....
- Combine all the matching labels using this script [here]() into one csv. Also create a tsv of this so that it can be compared to the original list using openRefine. 
- Reconcile the original list of proposed labels to the list of matched labels using openRefine - the unmatched list are the terms not in the NALT

---------------------------------------------------------------------------------------------------------------------------------------------------------
Still need to do the following:
- Create a script for the following:
    - create and add a new column to the nalt_altlabel.csv everytime the NALT gets updated so it can be utilized during this reconciliation process. A new column Nalt_URI_withsuffix needs to be created based off the NALT_URI column values + the suffix “_rand(5)” 
    - combine outputs of matched terms into one data frame and save as a csv? than can reconcile that to the original proposed list using openRefine - the unmatched list are the terms not in the NALT
- Add links to this read me
- Update summary.ipynb explaining everything re the AWIC labels
- Do another example 


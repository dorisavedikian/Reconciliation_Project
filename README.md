# UNDER CONSTRUCTION...the process works but still couple more things to do...

## This  Repo  is  to  document  the  reconciliation  process. 

Original [nalt_label_ALL.tsv]() file has 145,755 rows. Because alt and pref labels that correspond to a given concept / resource has the same URI, the openRefine reconciliation service will not work. So, I used a derivative of Tom Baker's [nalt_label.ipynb](https://github.com/woody544/nalt4ma/blob/main/nalt/nalt_labels.ipynb) jupiter notebook to keep the nalt pref labels and nalt alt labels seperate so that I could try and run the reconciliation on each file seperately.

After splitting it into two files...

- [nalt_preflabel.tsv]() had 76,932 rows ---> reconciled to beta prepared.tsv resulted in X* beta prepared labels reconciled to [X pref labels in the nalt]()

- [nalt_altlabel_withsuffix.tsv]() had 68,823 rows ----> I added a suffix to each URI using this script [here]() so they would be considered unique and I ran the service and it worked. X* beta prepared labels were reconciled to [X alt labels in the nalt.]() 

*These counts include the "unmatched" terms that actualy scored 100% during reconciliation but are "unmatched" because of minor differences such as punctation / case sensitivity.

Post reconciliation process in openRefine:
- Double check the unmatched labels by seperating the reconciliation into two seperate excel files / outputs ("matched" and "unmatched"), than use excel to filter the Score column in the "unmatched" version....If there are perfect matches that for some minor reason (ie, a comma, dash or case difference) did not get matched, it will score 100% but it wont get "matched"....check to see if these were already matched as a pref label / alt label....sometimes these subtle differences is what differentiaties between the alt label and pref label....

I combined the final outputs using this script [here]() into one csv [Y nalt terms in the beta prepared csv]() exist - which is Z more than what was expected per the beta prepared reconciliation I have as a [reference]().







Notes:

The following beta prepared labels are in the NALT and in the [nalt_preflabels.tsv]() that I used to do the reconciliation...But, they are not being reconciled due to minor differences....see examples below......

- Ames test* (<- as seen in the NALT, however, beta prepared data has it all lowercase - 100% matching score in openRefine)
- Breeding and Genetic Improvement (<- as seen in the NALT, however, beta prepared data has it all lowercase - 100% matching score in openRefine)
- New Zealand White rabbit (rabbit is lowercase in the NALT but uppercase in the beta prepared data - also, 100% matching score in openRefine)
- Limulus amebocyte lysate assay (Limulus is uppercase in the NALT but lowercase in the beta prepared data - also 100% matching score in openRefine)

![Screen Shot 2023-02-03 at 3 29 27 PM](https://user-images.githubusercontent.com/109038399/216729925-90ccd491-7d78-44d9-839b-1c15d48ae3df.png)
![Screen Shot 2023-02-03 at 3 33 56 PM](https://user-images.githubusercontent.com/109038399/216730044-c0269078-bb88-450a-b9ba-60b795dd1584.png)
![Screen Shot 2023-02-03 at 3 33 36 PM](https://user-images.githubusercontent.com/109038399/216730053-2bb478f4-9f81-4d3a-8fcc-66b8225d9dcb.png)
![Screen Shot 2023-02-03 at 3 35 40 PM](https://user-images.githubusercontent.com/109038399/216730175-f6add698-a535-4e1e-befd-c66cb52c149f.png)

*The beta prepared data also had 'Ames test' - which did get reconciled to the nalt_preflabel.tsv, the one in the above snip did not get reconciled to the nalt pref label because it is all lowercase and is neither a pref label or alt label.

The way to work around this is too export the reconciliation seperately (unmatched & matched) than filter the Score column of the unmatched excel output to see if there are still any perfect scores.....

This process actually revealed one more match to the NALT that wasnt in the beta prepared reconcile reference I have.....the term: National Center for the Replacement, Refinement and Reduction of Animals in Research...the beta prepared demo data had this in there but no comma after replacement....so, its already a nalt term with a minor difference. 

![Screen Shot 2023-02-03 at 7 52 28 PM](https://user-images.githubusercontent.com/109038399/216746575-cb9aeb70-1662-459f-a7cc-9d1139050a8a.png)

I also double checked the unmatched terms in openRefine after doing the reconciliation against the [nalt_altlabels_withsuffix.tsv]()....

![Screen Shot 2023-02-03 at 9 27 18 PM](https://user-images.githubusercontent.com/109038399/216750459-10875ad8-7819-46e9-b256-c5ee493f2ba8.png)

This did not add any more matching terms to the reconciliation....Most of the labels that were "unamtched" but scored 100% were already reconciled to nalt pref labels...


Still need to do the following:
- Create a script for the following:
    - adds suffix “_rand(5)” to all the values in a column and creates a new column with this new value (currently this process is being done in excel)
    - combine outputs of matched terms into one data frame and save as a csv?
    - remove duplicates from a list of proposed SME labels
- Add links to this read me
- Go through everything and make it so anyone can run anything from there computer
- Remove uneccesary comments
- Put comments / everything specific to the beta prepared labels reconciliation in a seperate folder labeled "example"
- The fact that labels will score 100% but still be unmatched due to very minor things such as case sensitivity is kind of weird....maybe flawed...I dk....I cant see a reason why this would be good...is this unique to the "csv-reconcile" repo? 

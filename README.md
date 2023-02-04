# Reconciliation_Project - UNDER CONSTRUCTION 

## This  Repo  is  to  document  the  reconciliation  process. 

Original [nalt_label_ALL.tsv]() file has 145,755 rows. Because alt and pref labels that correspond to a given concept / resource has the same URI, the openRefine reconciliation service will not work. So, I used a derivative of @tombakers [nalt_label.ipynb](https://github.com/woody544/nalt4ma/blob/main/nalt/nalt_labels.ipynb) jupiter notebook to keep the nalt pref labels and nalt alt labels seperate so that I could try and run the reconciliation on each file seperately.

After splitting it into two files...

- [nalt_preflabel.tsv]() had 76,932 rows ---> reconciled to beta prepared.tsv resulted in X* beta prepared labels reconciled to [X pref labels in the nalt]()

- [nalt_altlabel_withsuffix.tsv]() had 68,823 rows ----> I added a suffix to each URI using this script [here]() so they would be considered unique and I ran the service and it worked. X* beta prepared labels were reconciled to [X alt labels in the nalt.]() 

*These counts include the mistakenly "unmatched" terms during reconciliation.

Post reconciliation process in openRefine:
- Double check the unmatched labels by seperating the reconciliation into two seperate excel files / outputs ("matched" and "unmatched"), than use excel to filter the Score column in the "unmatched" version....If there are perfect matches that for some minor reason (ie, a comma or case difference) did not get matched, it will score 100% but it wont get "matched"....also, the Nalt_URI will of course not be there in the excel file for the unmatched so I had to look those up manually. Additionaly, sometimes these differences is what differentiaties between the alt label and pref label.......for example, (alt label = lethal concentration-50 and pref label = lethal concentration 50) - SO, it may be concisdered "unmatched" when reconciled to the alt labels / pref labels spererately but, it was actually already matched to a pref label or a alt label....

I combined the outputs using this script [here]() into one csv [Y nalt terms in the beta prepared csv]() exist - which is Z more than what was expected per the beta prepared reconciliation I have as a [reference]().







Notes:

The following beta prepared labels are in the NALT and in the [nalt_preflabels.tsv]() that I used to do the reconciliation...But, they are not being reconciled due to minor differences....see examples below...hmmmm....

- Breeding and Genetic Improvement (<- as seen in the NALT, however, beta prepared data has it all lowercase - 100% matching score in openRefine)
- New Zealand White rabbit (rabbit is lowercase in the NALT but uppercase in the beta prepared data - also, 100% matching score in openRefine)
- Limulus amebocyte lysate assay (Limulus is uppercase in the NALT but lowercase in the beta prepared data - also 100% matching score in openRefine)

![Screen Shot 2023-02-03 at 3 29 27 PM](https://user-images.githubusercontent.com/109038399/216729925-90ccd491-7d78-44d9-839b-1c15d48ae3df.png)
![Screen Shot 2023-02-03 at 3 33 56 PM](https://user-images.githubusercontent.com/109038399/216730044-c0269078-bb88-450a-b9ba-60b795dd1584.png)
![Screen Shot 2023-02-03 at 3 33 36 PM](https://user-images.githubusercontent.com/109038399/216730053-2bb478f4-9f81-4d3a-8fcc-66b8225d9dcb.png)
![Screen Shot 2023-02-03 at 3 35 40 PM](https://user-images.githubusercontent.com/109038399/216730175-f6add698-a535-4e1e-befd-c66cb52c149f.png)


The way to work around this is too export the reconciliation seperately (unmatched & matched) than filter the Score column to see if there are still any perfect scores.....

This process actually revealed one more match to the NALT that wasnt in the beta prepared reconcile reference I have.....the term: National Center for the Replacement, Refinement and Reduction of Animals in Research...the beta prepared demo data had this in there but no comma after replacement....

![Screen Shot 2023-02-03 at 7 52 28 PM](https://user-images.githubusercontent.com/109038399/216746575-cb9aeb70-1662-459f-a7cc-9d1139050a8a.png)

I double checked the unmatched terms in openRefine after doing the reconciliation to the [nalt_altlabels_withsuffix.tsv]()....
![Screen Shot 2023-02-03 at 8 53 31 PM](https://user-images.githubusercontent.com/109038399/216750367-fa9a3e91-47f1-49de-8f33-0e30ccc65a25.png)

This did not add any more matching terms to the reconciliation....


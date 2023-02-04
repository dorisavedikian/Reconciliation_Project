# Reconciliation_Project

# UNDER CONSTRUCTION 

## This  Repo  is  to  document  the  reconciliation  process. 

Original [nalt_label_ALL.tsv]() file has 145,755 rows

After splitting it into two files...

- [nalt_preflabel.tsv]() had 76,932 rows ---> reconciled to beta prepared.tsv resulted in [744 reconciled nalt terms]()

- [nalt_altlabel_withsuffix.tsv]() had 68,823 rows ----> I added a suffix to each URI so they would be considered unique and I ran the service and it worked. X beta prepared labels were reconciled to [X pref labels in the nalt.](https://github.com/dorisavedikian/Reconciliation_Project/blob/main/Reconciled/beta%20prepared_reconciled_2alt_labels_withsuffix_only.xlsx)

I aggregated the outputs and there are [744 nalt terms in the beta prepared csv]() - which is 4 less than what was expected per the beta prepared reconciliation I have as a [reference](https://github.com/dorisavedikian/Reconciliation_Project/blob/main/Reconciled/beta%20prepared_reconciled_4_reference.csv).

The following beta prepared labels are in the NALT and in the [nalt_preflabels_only.tsv]() that I used to do the reconciliation...But, they are not being reconciled...hmmmm...

- Ames test (Ames is uppercase in the NALT but lower case in the beta prepared data - 100% matching score in openRefine)
- Breeding and Genetic Improvement (<- as seen in the NALT, however, beta prepared data has it all lowercase - 100% matching score in openRefine)
- New Zealand White rabbit (rabbit is lowercase in the NALT but uppercase in the beta prepared data - also, 100% matching score in openRefine)
- Limulus amebocyte lysate assay (Limulus is uppercase in the NALT but lowercase in the beta prepared data - also 100% matching score in openRefine)

![Screen Shot 2023-02-03 at 3 29 27 PM](https://user-images.githubusercontent.com/109038399/216729925-90ccd491-7d78-44d9-839b-1c15d48ae3df.png)
![Screen Shot 2023-02-03 at 3 33 56 PM](https://user-images.githubusercontent.com/109038399/216730044-c0269078-bb88-450a-b9ba-60b795dd1584.png)
![Screen Shot 2023-02-03 at 3 33 36 PM](https://user-images.githubusercontent.com/109038399/216730053-2bb478f4-9f81-4d3a-8fcc-66b8225d9dcb.png)
![Screen Shot 2023-02-03 at 3 35 40 PM](https://user-images.githubusercontent.com/109038399/216730175-f6add698-a535-4e1e-befd-c66cb52c149f.png)


The way to work around this is too export the reconciliation seperately (unmatched & matched) than filter the Score column to see if there are still any perfect scores.....ie, first exclude unmatched data and create a Nalt_URI and Score column for the matched datas and than exclude matched data and create a Nalt_URI2 and Score2 column... 

This process actually revealed one more match to the NALT.....the term: National Center for the Replacement, Refinement and Reduction of Animals in Research...the beta prepared demo data had this in there but no comma....
(rerun rec against nalt pref labels and get a snip of this one)

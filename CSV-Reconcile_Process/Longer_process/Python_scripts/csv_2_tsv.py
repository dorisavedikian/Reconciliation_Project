

import csv
import pandas as pd
import os 

df = pd.read_csv('/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/longer_process/Examples/ADC/SME_labels/ADC_Labels.csv')
df.to_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/longer_process/Examples/ADC/SME_labels/ADC_Labels.tsv", sep="\t", index=False)

#df1 = pd.read_csv('/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/longer_process/Examples/ADC/SME_labels/ADC_Labels.csv')
#df1.to_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/longer_process/Examples/ADC/SME_labels/ADC_Labels.tsv", sep="\t", index=False)

os.remove("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/longer_processExamples/ADC/SME_labels/ADC_Labels.csv")
#os.remove("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/longer_process/Examples/Biotech/SME_labels/Biotech_Labels.csv")

# python3 python_scripts/csv_2_tsv.py
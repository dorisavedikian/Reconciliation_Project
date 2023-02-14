import csv
import pandas as pd

df = pd.read_csv('/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/Cotton/SME labels/CottonLabels.csv')
df.to_csv("/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/CSV-Reconcile_Process/Examples/Cotton/SME labels/CottonLabels.tsv", sep="\t", index=False)

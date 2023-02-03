'''
 - Trying to create a script that will iterate a df row by row and for the values == null / empty create a 
   new column and append the previous row and column value + numerical suffix to that new column
'''
from fileinput import filename
import pandas as pd
import csv 

def createnewdf(): 
    df2 = {'NALT_URI':[], 'Label':[],  'NALT_URI2':[]}                         
    df = pd.read_csv('/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/nalt_labels_DATA/nalt_altlabels_1.csv')    
    for (index,row) in df.iterrows():                                                                   
        if df['NALT_URI'].isnull():                                                  
            NALT_URI2 = df['NALT_URI'].iloc[-1]        # is this right? need to add numerical suffix to this somehow                     
        else:
            Row_Number, NALT_URI, Label = (index,row).split(',')             
            df2['Row_Number'].append(Row_Number)
            df2['NALT_URI'].append(NALT_URI)
            df2['Label'].append(Label)
            df2['NALT_URI2'].append(NALT_URI2)
    df2 = pd.DataFrame(df2)
    outfile = df2.to_csv('/Volumes/USDA HD/NAL/MyGitFolder/Reconciliation_Project/nalt_labels_DATA/nalt_altlabels_2.csv')

createnewdf()

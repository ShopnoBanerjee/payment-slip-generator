# %%

'''CLEAN PRESENTATION OF HOW LISTY(LIST OF EMPLOYEE DATA) IS MADE'''


import pandas as pd
import numpy as np


# def listy(filename):
#   df = pd.read_csv(f"{filename}.csv")

df = pd.read_csv("salary_sheet.csv")

df = df.rename(columns={"Name of the employees ":"name","ESI NO":"ESI no"})


df=df[['Emp. Code', 'Name of the employees','Actual','Basic', 'HRA ', 'conveyance', 'Washing',
       'OT', 'TOTAL','P.T.', 'P.F.', 'ESI ','Adv.', 'Total.2']]

df=df.astype(str)

columns = [['Emp. Code', 'Name of the employees','Actual','Basic', 'HRA ', 'conveyance', 'Washing',
       'OT', 'TOTAL','P.T.', 'P.F.', 'ESI ','Adv.', 'Total.2']]

listy=[]
for index, row in df.iterrows():
    words=" "
    list=[]
    for col in columns:

        words = words + ' '.join(row[col])+' '
        list=words.split()
        listy.append(list)
# %%




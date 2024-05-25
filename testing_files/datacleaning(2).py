# %%
import pandas as pd
import numpy as np

df = pd.read_excel("salary sheet template.xlsx")
df = df.rename(columns={'Net Payment (Take Home)': 'Net Payment'})
df=df[['Month & Year', 'Name of the employees','UAN no','Actual','Basic', 'HRA', 'conveyance', 'Washing','Extra', 'TOTAL','P.T.', 'P.F.(12%)', 'ESI (0.75%)','Adv.', 'Total deduction', 'Net Payment']]
df=df.astype(str)
df['Adv.'] = df['Adv.'].str.replace('nan','-')

columns = [['Month & Year', 'Name of the employees','UAN no',
            'Actual','Basic', 'HRA', 'conveyance', 'Washing','Extra', 'TOTAL',
            'P.T.', 'P.F.(12%)', 'ESI (0.75%)','Adv.', 'Total deduction'
            '']]

listy=[]
for index, row in df.iterrows():
    words=" "
    list=[]
    for col in columns:

        words = words + ' '.join(row[col])+' '
        list=words.split()
        listy.append(list)
        print(list)

print(listy)

    
    # for col in genre:
    #     row[col] = row[col].replace('[', '').replace(']', '').replace('\'', '')
    #     row[col] = row[col].replace(',', ' ')
    #     words = words + ''.join(row[col])+' '
    # for col in name:
    #     row[col] = row[col].replace(',', ' ')
    #     words = words + ' '.join(row[col])+' '

    # for col in keyword:
    #     words = words + ' '.join(row[col])+ ' '
    # for col in prod:    
    #     row[col] = row[col].replace('[', '').replace(']', '').replace('\'', '')
    # for col in scores:
    #     words = words + str(int(row[col]))
    # df.at[index,'bag_of_words'] = words.lower()
# df.head()
from datetime import datetime






# %%

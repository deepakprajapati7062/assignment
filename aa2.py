import pandas as pd

df= pd.read_csv('user.csv',index_col=False)

df_sort=df.sort_values('Firstname')

df_sort.to_csv('user.csv',encoding='utf-8',index=False)


#record=df.loc[df['Firstname']=='ayush']
#print(record)

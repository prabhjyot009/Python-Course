#6.	Write a python program to Slicing, Indexing, Manipulating and Cleaning Pandas Dataframe

import pandas as pd
player = ['Sachin', 'Sehwag', 'Gambhir', 'Dravid', 'Kohli', 'Dhoni', 'Yuvraj']
score = [100, 200, 150, 50, 75, 125, 180]
df = pd.DataFrame({'Player': player, 'Score': score})
print(df)
#manipulating
df['Score'] = df['Score'].apply(lambda x: x + 10)
print(df)
#cleaning
df['Score'] = df['Score'].apply(lambda x: x - 10)
print(df)
#slicing
print(df.iloc[0:3, 0:2])
#indexing
print(df.loc[0:3, 'Player'])
print(df.loc[0:4,'Score'])
#6.	Write a python program to Slicing, Indexing, Manipulating and Cleaning Pandas Dataframe

import pandas as pd
player = ['Sachin', 'Sehwag', 'Gambhir', 'Dravid', 'Kohli', 'Dhoni', 'Yuvraj']
score = [100, 200, 150, 50, 75, 125, 180]
df = pd.DataFrame({'Player': player, 'Score': score})
print("Orignal Data:\n",df)
#manipulating
df['Score'] = df['Score'].apply(lambda x: x + 10)
print("Manipulating Data:\n",df)
#cleaning
df['Score'] = df['Score'].apply(lambda x: x - 10)
print("Cleaning Data:\n",df)
#slicing
print("Slicing Data:\n",df.iloc[0:3, 0:2])
#indexing
print("Indexing Data:\n")
print(df.loc[0:3, 'Player'])
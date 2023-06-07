#7.	Write a Python Pandas program to get the columns of the DataFrame (movies_metadata.csv file).

import pandas as pd
df = pd.read_csv(r'D:/Dropbox/Study/GitHub/Python-Course/Python/College Python/Assignment/movies_metadata.csv')
print("Columns of the DataFrame:")
print(df.columns)
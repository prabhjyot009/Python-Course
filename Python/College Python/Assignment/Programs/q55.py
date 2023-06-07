#11.	Write a Pandas program to get the details of the columns title and genres of the DataFrame.

import pandas as pd

df = pd.read_csv(r'D:/Dropbox/Study/GitHub/Python-Course/Python/College Python/Assignment/movies_metadata.csv')
print("Details of the columns title and genres:")
print(df[['title', 'genres']])



#9.	Write a Pandas program to get the details of the third movie of the DataFrame (movies_metadata.csv file).

import pandas as pd

df = pd.read_csv(r'D:/Dropbox/Study/GitHub/Python-Course/Python/College Python/Assignment/movies_metadata.csv')
print("Details of the third moviee:")
print(df.iloc[2])
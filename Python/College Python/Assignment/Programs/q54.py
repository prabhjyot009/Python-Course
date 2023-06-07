#10.	 Write a Pandas program to count the number of rows and columns of the DataFrame (movies_metadata.csv file).

import pandas as pd

df = pd.read_csv(r'D:/Dropbox/Study/GitHub/Python-Course/Python/College Python/Assignment/movies_metadata.csv')
print("Number of rows and columns of the DataFrame:")
print(df.shape)

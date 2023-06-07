#12.	 Write a Pandas program to get the details of the movie with title 'Grumpier Old Men'.

import pandas as pd

df = pd.read_csv(r'D:/Dropbox/Study/GitHub/Python-Course/Python/College Python/Assignment/movies_metadata.csv')
df=df.set_index('title')
print("Details of the movie 'Grumpier Old Men:\n",df.loc['Grumpier Old Men'])
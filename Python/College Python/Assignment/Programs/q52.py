#8.	Write a Pandas program to get the information of the DataFrame (movies_metadata.csv file)including data types and memory usage.

import pandas as pd

df = pd.read_csv(r'D:/Dropbox/Study/GitHub/Python-Course/Python/College Python/Assignment/movies_metadata.csv')
print("Information of the DataFrame:")
print(df.info())
print("Data types of the DataFrame:")   
print(df.dtypes)
print("Summary of the DataFrame:")
print(df.describe(include = 'all'))
print("Memory usage of the DataFrame:")
print(df.memory_usage())
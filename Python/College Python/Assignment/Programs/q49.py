#5.	Write a python program to get frequency counts of a columns in Pandas DataFrame.

import pandas as pd

df = pd.DataFrame({'Age': [18,19,19,20,23,20, 21,23]})
count = df.groupby(['Age']).size()
print(count)
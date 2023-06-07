#4.	Write a python program to Convert list of nested dictionary into Pandas dataframe

import pandas as pd
import numpy as np
Name=['A','B','C','D','E']
Age=[20,21,22,23,24]
dict1={'Name':Name,'Age':Age}
print(dict1)
df=pd.DataFrame(dict1)
print(df)
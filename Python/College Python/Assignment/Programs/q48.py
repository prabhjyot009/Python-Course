#4.	Write a python program to Convert list of nested dictionary into Pandas dataframe

import pandas as pd
import numpy as np
Name=['A','B','C','D','E']
Age=[20,21,22,23,24]
dict1={'Name':Name,'Age':Age}
print(dict1)
df=pd.DataFrame(dict1)
print(df)

#algorithm to Convert list of nested dictionary into Pandas dataframe
#step1: start
#step2: import pandas as pd
#step3: define a variable Name and assign ['A','B','C','D','E'] to it
#step4: define a variable Age and assign [20,21,22,23,24] to it
#step5: define a variable dict1 and assign {'Name':Name,'Age':Age} to it
#step6: print dict1
#step7: define a variable df and assign pd.DataFrame(dict1) to it
#step8: print df
#step9: stop
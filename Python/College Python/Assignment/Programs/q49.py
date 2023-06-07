#5.	Write a python program to get frequency counts of a columns in Pandas DataFrame.

import pandas as pd

df = pd.DataFrame({'Age': [18,19,19,20,23,20, 21,23]})
count = df.groupby(['Age']).size()
print(count)


#algorithm to get frequency counts of a columns in Pandas DataFrame.
#step1: start
#step2: import pandas as pd
#step3: define a variable df and assign pd.DataFrame({'Age': [18,19,19,20,23,20, 21,23]}) to it
#step4: define a variable count and assign df.groupby(['Age']).size() to it
#step5: print count
#step6: stop
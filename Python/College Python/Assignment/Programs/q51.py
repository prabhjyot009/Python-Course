#7.	Write a Python Pandas program to get the columns of the DataFrame (movies_metadata.csv file).

import pandas as pd
df = pd.read_csv(r'D:/Dropbox/Study/GitHub/Python-Course/Python/College Python/Assignment/movies_metadata.csv')
print("Columns of the DataFrame:")
print(df.columns)

#algorithm to get the columns of the DataFrame (movies_metadata.csv file).
#step1: start
#step2: import pandas as pd
#step3: define a variable df and assign pd.read_csv(r'D:/Dropbox/Study/GitHub/Python-Course/Python/College Python/Assignment/movies_metadata.csv') to it
#step4: print "Columns of the DataFrame:"
#step5: print df.columns
#step6: stop

#9.	Write a Pandas program to get the details of the third movie of the DataFrame (movies_metadata.csv file).

import pandas as pd

df = pd.read_csv(r'D:/Dropbox/Study/GitHub/Python-Course/Python/College Python/Assignment/movies_metadata.csv')
print("Details of the third moviee:")
print(df.iloc[2])


#algorithm to get the details of the third movie of the DataFrame (movies_metadata.csv file).
#step1: start
#step2: import pandas as pd
#step3: define a variable df and assign pd.read_csv(r'D:/Dropbox/Study/GitHub/Python-Course/Python/College Python/Assignment/movies_metadata.csv') to it
#step4: print "Details of the third moviee:"
#step5: print df.iloc[2]
#step6: stop

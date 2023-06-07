#11.	Write a Pandas program to get the details of the columns title and genres of the DataFrame.

import pandas as pd

df = pd.read_csv(r'D:/Dropbox/Study/GitHub/Python-Course/Python/College Python/Assignment/movies_metadata.csv')
print("Details of the columns title and genres:")
print(df[['title', 'genres']])

#algorithm to get the details of the columns title and genres of the DataFrame.
#step1: start
#step2: import pandas as pd
#step3: define a variable df and assign pd.read_csv(r'D:/Dropbox/Study/GitHub/Python-Course/Python/College Python/Assignment/movies_metadata.csv') to it
#step4: print "Details of the columns title and genres:"
#step5: print df[['title', 'genres']]
#step6: stop






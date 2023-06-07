#10.	 Write a Pandas program to count the number of rows and columns of the DataFrame (movies_metadata.csv file).

import pandas as pd

df = pd.read_csv(r'D:/Dropbox/Study/GitHub/Python-Course/Python/College Python/Assignment/movies_metadata.csv')
print("Number of rows and columns of the DataFrame:")
print(df.shape)


#algorithm to count the number of rows and columns of the DataFrame (movies_metadata.csv file).
#step1: start
#step2: import pandas as pd
#step3: define a variable df and assign pd.read_csv(r'D:/Dropbox/Study/GitHub/Python-Course/Python/College Python/Assignment/movies_metadata.csv') to it
#step4: print "Number of rows and columns of the DataFrame:"
#step5: print df.shape
#step6: stop
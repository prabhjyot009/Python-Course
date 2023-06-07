#12.	 Write a Pandas program to get the details of the movie with title 'Grumpier Old Men'.

import pandas as pd

df = pd.read_csv(r'D:/Dropbox/Study/GitHub/Python-Course/Python/College Python/Assignment/movies_metadata.csv')
df=df.set_index('title')
print("Details of the movie 'Grumpier Old Men:\n",df.loc['Grumpier Old Men'])

#algorithm for a Pandas program to get the details of the movie with title 'Grumpier Old Men'.
#step1: start
#step2: import pandas as pd
#step3: define a variable df and assign pd.read_csv(r'D:/Dropbox/Study/GitHub/Python-Course/Python/College Python/Assignment/movies_metadata.csv') to it
#step4:define a variable df=df.set_index('title')
#step5:print Details of the movie 'Grumpier Old Men df.loc['Grumpier Old Men']
#step6: stop
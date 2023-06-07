#6.	Write a python program to Slicing, Indexing, Manipulating and Cleaning Pandas Dataframe

import pandas as pd
player = ['Sachin', 'Sehwag', 'Gambhir', 'Dravid', 'Kohli', 'Dhoni', 'Yuvraj']
score = [100, 200, 150, 50, 75, 125, 180]
df = pd.DataFrame({'Player': player, 'Score': score})
print("Orignal Data:\n",df)
#manipulating
df['Score'] = df['Score'].apply(lambda x: x + 10)
print("Manipulating Data:\n",df)
#cleaning
df['Score'] = df['Score'].apply(lambda x: x - 10)
print("Cleaning Data:\n",df)
#slicing
print("Slicing Data:\n",df.iloc[0:3, 0:2])
#indexing
print("Indexing Data:\n")
print(df.loc[0:3, 'Player'])

#algorithm to Slicing, Indexing, Manipulating and Cleaning Pandas Dataframe
#step1: start
#step2: import pandas as pd
#step3: define a variable player and assign ['Sachin', 'Sehwag', 'Gambhir', 'Dravid', 'Kohli', 'Dhoni', 'Yuvraj'] to it
#step4: define a variable score and assign [100, 200, 150, 50, 75, 125, 180] to it
#step5: define a variable df and assign pd.DataFrame({'Player': player, 'Score': score}) to it
#step6: print "Orignal Data:\n",df
#step7: df['Score'] = df['Score'].apply(lambda x: x + 10)
#step8: print "Manipulating Data:\n",df
#step9: df['Score'] = df['Score'].apply(lambda x: x - 10)
#step10: print "Cleaning Data:\n",df
#step11: print "Slicing Data:\n",df.iloc[0:3, 0:2]
#step12: print "Indexing Data:\n"
#step13: print df.loc[0:3, 'Player']
#step14: stop
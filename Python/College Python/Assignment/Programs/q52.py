#8.	Write a Pandas program to get the information of the DataFrame (movies_metadata.csv file)including data types and memory usage.

import pandas as pd

df = pd.read_csv(r'D:/Dropbox/Study/GitHub/Python-Course/Python/College Python/Assignment/movies_metadata.csv')
print("Information of the DataFrame:\n")
print(df.info())
print("Data types of the DataFrame:\n")   
print(df.dtypes)
print("Memory usage of the DataFrame:\n")
print(df.memory_usage())

#algorithm to get the information of the DataFrame (movies_metadata.csv file)including data types and memory usage.
#step1: start
#step2: import pandas as pd
#step3: define a variable df and assign pd.read_csv(r'D:/Dropbox/Study/GitHub/Python-Course/Python/College Python/Assignment/movies_metadata.csv') to it
#step4: print "Information of the DataFrame:\n"
#step5: print df.info()
#step6: print "Data types of the DataFrame:\n"
#step7: print df.dtypes
#step8: print "Memory usage of the DataFrame:\n"
#step9: print df.memory_usage()
#step10: stop
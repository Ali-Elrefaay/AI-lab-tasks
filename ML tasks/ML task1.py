# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 09:28:55 2021

@author: workstation
"""

#1,2


import numpy as np
import pandas as pd
dataset=pd.read_csv("Wuzzuf_Jobs.csv")
dataset.describe()




#3


import numpy as np
import pandas as pd
# making data frame from csv file
data = pd.read_csv("Wuzzuf_Jobs.csv")

# dropping ALL duplicate values
data.drop_duplicates(subset =None,
					keep = "first", inplace = True)

import numpy as np
import pandas as pd

dataset = pd.read_csv("Wuzzuf_Jobs.csv")
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values
from sklearn.impute import SimpleImputer
imp_mean = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imp_mean = imp_mean.fit(X[:, 0:3])
X[:, 0:3] = imp_mean.transform(X[:, 0:3])

print(X)


#4,5


import matplotlib.pyplot as plt
import pandas as pd
# Importing the dataset
dataset = pd.read_csv('Wuzzuf_Jobs.csv')

x=dataset['Company'].value_counts()
plt.pie(x)
plt.show() 
print ('the most demanding companies for jobs are', x.index[0:5] )





#6,7



import matplotlib.pyplot as plt
import pandas as pd
# Importing the dataset
dataset = pd.read_csv('Wuzzuf_Jobs.csv')

z=dataset['Title'].value_counts()
print ('the Most popular jobs title are', z.index[0:5] )
fig = plt.figure(figsize = (10, 5))
plt.bar(z.index[0:5], z[0:5], color ='maroon',
		width = 0.4)

plt.xlabel("Most popular jobs title")
plt.ylabel("Number of popular jobs title")
plt.title("Popular jobs title")
plt.show()




#8.9


import matplotlib.pyplot as plt
import pandas as pd
# Importing the dataset
dataset = pd.read_csv('Wuzzuf_Jobs.csv')

y=dataset['Location'].value_counts()
print ('the Most popular areas are', y.index[0:5] )
fig = plt.figure(figsize = (10, 5))
plt.bar(y.index[0:5], y[0:5], color ='maroon',
		width = 0.4)

plt.xlabel("Most popular areas")
plt.ylabel("Number of popular areas")
plt.title("Popular areas")
plt.show()



#10


Dict=dict()
for skills in dataset['Skills']:
    for skill in skills.split(','):
        if skill in Dict.keys():
            Dict[skill]+=1
        else:
            Dict[skill]=1
from collections import Counter          
Max =Counter(Dict)
MaxFive= dict(Max.most_common(5))
print("Top 5 skills :-")
for skill,count in MaxFive.items():    
    print("%s : %d"%(skill,count))

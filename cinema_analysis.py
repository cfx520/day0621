import tushare as ts
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=ts.month_boxoffice('2017-8')
colors=['red','yellow','blue']
print df['boxoffice']
pie=plt.pie(df['boxoffice'],labels=df['MovieName'],autopct='%1.1f%%',
            startangle=0,colors=colors)
plt.axis('equal')
plt.show()
#data=pd.read_csv('1.txt',sep='\t')
#print data


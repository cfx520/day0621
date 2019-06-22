import pandas as pd
import numpy as np
"""
author cfx
"""
s1=pd.Series([100,200,300],index=['a','b','c'])
#s2=pd.Series([500,600,700],index=['a','b','c'])
#print pd.concat([s1,s2])
df1=pd.DataFrame([[100,200,300],[110,120,130],[210,220,230]])
#df2=pd.DataFrame([[10,20,30],[11,12,13],[21,22,23]])
#print pd.concat([df1,s1],axis=1)
gdp1=pd.DataFrame({"city":["shanghai","guangzhou","shenzhen","chongqing"],                   "number":[27466.2,19610.9,19492.6,17558.8]})
gdp2=pd.DataFrame({"city":["shanghai","beijing","shenzhen","suzhou"],
                   "number":[27466.2,24899.3,19492.6,15475.1]})
print pd.merge(gdp1,gdp2)


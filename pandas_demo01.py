#encoding:utf-8
import numpy as np
import pandas as pd
#导入数据分析所需的库
##创建一个一维数组
g=np.array([1,2,3,32])
#print g[0],g[3]
#可以通过数组的索引找到对应的值，但是数组索引缺乏明确的意义
#为了得到明确的意义，于是有了DataFrom
g1=pd.Series(g,index=['zhangsan','lisi','wangwu','zhaoliu'])
#print g1
#注意index的长度和data的长度要一致
g2=pd.Series(100,index=['a','b','c'])
#print g2
g3=pd.Series('abccc',index=[1,2,3,4])
#print g3
g4=pd.Series([0.1,0.2,0.3,0.4],index=[1,2,3,4])
#print g4

g5=pd.Series({'a':101,'b':111,'c':103})
#print g5.index,g5.values
g5.index=['cc','dd','ee']
#g5['cc']=g5['eeee']
#print g5
pg=pd.DataFrame({'city':['beijing','wuhan','changsha','shanghai'],'mark':[70,69,68,66]}
                ,index=['Tsinghua','WHU','zhongnan','Fudan'])
#print pg

ind=pd.Index(['pyhsics','python','math','english'])
s=pd.Series([100,90,80,70],index=ind)
d=pd.DataFrame({'soochow':s,'tsinghua':[98,34,83,49]},index=ind)
#print d
cities_index=[('China','Beijing'),('China','Shanghai'),('USA','Chicago'),('USA','NewYork')]
cities=pd.MultiIndex.from_tuples(cities_index)
#print cities
gdp_index=[('Beijing','2018'),('Shanghai','2019'),('Beijing','2019'),('Shanghai','2018'),('Guangzhou','2018')
    ,('Guangzhou','2019')]
gdp_mind=pd.MultiIndex.from_tuples(gdp_index)
gdp_1=pd.Series([25300,27466,23000,24899,18100,19611],index=gdp_mind)
#print gdp_1
#print gdp_1.unstack().stack()
g1=gdp_1['Shanghai']
#print gdp_1.iloc[0] 返回的是第一个数值
#print gdp_1.loc['Shanghai','2018']
#print gdp_1.loc[:,'2018']
#print gdp_1.loc[gdp_1>25000]
print gdp_1.iloc[1:5]
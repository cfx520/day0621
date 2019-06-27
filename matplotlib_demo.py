#encoding:utf-8
import matplotlib.pyplot as plt
value=[1,2,3,4,5]
sequares=[1,4,9,16,25]
plt.plot(value,sequares,linewidth=5)
plt.title('se',fontsize='24')
plt.ylabel('sequares value',fontsize='24')
plt.xlabel('values',fontsize='24')
x=[1,2,3,4]
plt.scatter(x,[i^2 for i in x])
plt.show()
from random import choice





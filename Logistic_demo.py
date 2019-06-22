from scipy.stats import logistic
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(8,4))
ax=fig.add_subplot(111)
z=np.linspace(-6,6,100)
ax.plot(z,logistic.cdf(z),'r-',label='logistic')
plt.show(ax)
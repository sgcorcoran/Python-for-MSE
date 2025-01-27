#!/usr/bin/env python
# coding: utf-8

# # Short Lesson: Plotting functions

# In[1]:


# only need to import these once
# place all import statements in the first cell of your notebook
import numpy as np
import matplotlib.pyplot as plt
from scipy import special #this contains the erf() function


# In[8]:


np.e


# In[3]:


np.exp(1)


# In[38]:


np.linspace(-2.5, 2.5, 5)


# In[39]:


np.arange(-2.5, 2.5, 0.5)


# #### useful functions in numpy and scipy.special
#     np.piecewise(x, [x < 0, x >= 0], [-1, 1])
#     np.linspace(-2.5, 2.5, 6)
#     np.log()
#     np.log10()
#     np.sin()
#     np.amax()
#     special.erf()

# In[28]:


np.eye(2)


# In[16]:


x=np.array([-10, -5, 0, 10])
np.piecewise(x, [x < 0, x==0, x > 0], [-1, 0, 1])


# In[17]:


x=np.array([-10, -5, 0, 10])
np.piecewise(x, [x < 0, x >= 0], [lambda x: -x, lambda x: x])


# In[20]:


np.linspace(-2.5, 2.5, 6)


# In[34]:


np.arange(0.0, 1.0, 0.25)


# In[27]:


np.inf
np.nan
np.e
np.pi


# In[15]:


# t must be an np array not a python list
def myfunc(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

xdata=np.arange(0.0, 5.0, 0.05)
ydata=myfunc(xdata)

plt.plot(xdata, ydata, 'k*')
plt.ylabel('some label')
plt.show()


# In[31]:


# t must be an np array not a python list
def myfunc(t):
    return special.erf(t)

xdata=np.arange(0.0, 5.0, 0.05)
ydata=myfunc(xdata)

plt.plot(xdata, ydata, 'k*')
plt.ylabel('some label')
plt.show()


# ### Problem 17.32 Callister 10th ed.  Metal oxidation. 

# ![image.png](attachment:image.png)

# <hr>
# Growth laws for oxides on metals: <br>
# <ol>
# <li>Parabolic Growth: $W^2 =K_1 \ t + K_2$</li>
# <li>Linear Growth: $W = K_3 \ t$</li>
# <li>Logarithmic Growth: $W=K_4\ \log(K_5\ t + K_6)$</li>
# </ol>  
# 
# <hr>
# 
# 

# In[12]:


xdata=np.array([0,25, 75, 250])
ydata=np.array([0,1.9, 3.76, 6.4])

plt.plot(xdata, ydata, 'ko')
plt.ylabel('weight increase ' + r'$( mg/cm^2 )$')
plt.xlabel('time (min)')
plt.show()


# In[14]:


from numpy import exp, linspace, random

def gaussian(x, amp, cen, wid):
    return amp * exp(-(x-cen)**2 / wid)

from scipy.optimize import curve_fit

x = linspace(-10, 10, 101)
y = gaussian(x, 2.33, 0.21, 1.51) + random.normal(0, 0.2, x.size)

init_vals = [1, 0, 1]  # for [amp, cen, wid]
best_vals, covar = curve_fit(gaussian, x, y, p0=init_vals)
print('best_vals: {}'.format(best_vals))


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # Short Lesson: Math Operations

# This notebook just highlights a couple of useful constants and functions we will use all the time.  It assumes you know how to perform simiple math operations at this point.  
# 
# Reminder $\text{**}$ means power not "^".  

# In[24]:


5**2


# In[29]:


5^2  #this does not mean power as you can see from output


# First thing we do is import the numpy extension and the scipy.constants extension which has a lot of useful mathematical functions.  A link to the numpy documentation can be found under the jupyter Help menu.  
# <div>
# <img src="attachment:image.png" width="100">
# </div>

# In[2]:


import numpy as np 
from scipy import constants


# Some available constants:
# 
#     np.e  
#     np.pi
#     constants.e  
#     constants.pi
#     constants.R
#     constants.N_A
#     constants.k

# In[3]:


np.e # this "e" is the base of the natural logarithm


# In[12]:


constants.e # notice that this "e" is the charge on an electron


# Some available functions:
# 
#     np.cos(), np.sin(), np.arcsin(),  etc.
#     np.log(), np.log10(), np.sqrt(), etc.
#     np.mean(), np.sum(), np.median(), etc
#     
# General Math: https://numpy.org/devdocs/reference/routines.math.html
# 
# Statistics: https://numpy.org/devdocs/reference/routines.statistics.html
# 
# 
# 

# In[20]:


np.cos(np.pi)


# In[23]:


np.log10(100)


# We can use sympy if we want to perform symbolic manipulation such as derivatives, integration, solving equations, etc.  We will look at that later in the course.  

# In[30]:


np.sqrt(9)


# In[31]:


np.random.randn(3)


# In[34]:


np.random.random((3))


# In[7]:


np.random.randint(3,10, size=100) #notice that 3,10 gives numbers from 3,9


# In[ ]:





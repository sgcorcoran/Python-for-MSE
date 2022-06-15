#!/usr/bin/env python
# coding: utf-8

# ## Creating your own functions for import

# ### Our example comes from crystallography and will require some matrix manipulation so let's 

# 
# #### 1. take a refresher on matrices
# #### 2. look at creating and testing a function
# #### 3. copy function to a text file *.py for import

# When dealing with matrices, you will want to use the numpy.linalg module. You can read the documentation here: https://numpy.org/doc/stable/reference/routines.linalg.html

# In[1]:


import numpy as np  #the linalg module would then be np.linalg


# #### defining a matrix as a numpy array

# In[ ]:





# #### multiplying matrices np.dot()

# In[ ]:





# #### example:  gmatrix used in crystallography
# 
# | | |
# |-|-|
# |![image-2.png](attachment:image-2.png)  |$$ g=\begin{bmatrix}a^{2} & ab \cos{(\gamma)}&ac \cos (\beta) \\ab \cos(\gamma) & b^2 & bc \cos (\alpha) \\ ac  \cos(\beta) & bc \cos(\alpha)&c^2 \end{bmatrix}$$|
# 

# #### simple case: gmatrix for white tin (tetragonal)
# a = b = 0.583 nm
# c = 0.318 nm
# $\alpha = \beta = \gamma = 90^{\circ}$

# In[ ]:





# #### Volume of the unit cell for Tin = sqrt of determinant of $g$

# In[ ]:





# In[ ]:





# #### Gmatrix for any a, b, c, $\alpha, \beta, \gamma$

# In[ ]:





# In[ ]:





# #### Write the function & test

# In[ ]:





# In[ ]:





# #### Put it all in one cell, test again after restarting Kernel, copy to text file *.py

# In[ ]:





# In[ ]:





# Now go an import your .py file in another notebook and see if it works!

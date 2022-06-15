#!/usr/bin/env python
# coding: utf-8

# ## Creating your own functions for import

# ### Our example comes from crystallography and will require some matrix manipulation so let's 
# #### 1. take a refresher on matrices
# #### 2. look at creating and testing a function
# #### 3. copy function to a text file *.py for import

# When dealing with matrices, you will want to use the numpy.linalg module. You can read the documentation here: https://numpy.org/doc/stable/reference/routines.linalg.html

# In[1]:


import numpy as np  #the linalg module would then be np.linalg


# #### defining a matrix as a numpy array

# In[2]:


A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[11,21,31],[41,51,61],[71,81,91]])
print(B)
A


# #### multiplying matrices np.dot()

# In[3]:


np.dot(A,B)


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

# In[4]:


g=np.array([[0.583**2, 0,0],[0,0.583**2, 0],[0,0,0.318**2]])
g


# #### Volume of the unit cell for Tin = sqrt of determinant of $g$

# In[5]:


0.583*0.583*0.318


# In[6]:


np.sqrt(np.linalg.det(g))


# #### Gmatrix for any a, b, c, $\alpha, \beta, \gamma$

# In[7]:


def gmatrix(a,b,c,alpha,beta,gamma):
    alpha=np.deg2rad(alpha)
    beta=np.deg2rad(beta)
    gamma=np.deg2rad(gamma)
    g=np.array([
    [a*a, a*b*np.cos(gamma), a*c*np.cos(beta)],
    [b*a*np.cos(gamma), b*b, b*c*np.cos(alpha)], 
    [c*a*np.cos(beta),c*b*np.cos(alpha),c*c]
    ])
    return(g)
    


# In[8]:


gmatrix(1,2,3, 90,90,90)


# #### Write the function & test

# In[9]:


def vuc(a,b,c,alpha, beta, gamma):
    alpha=np.deg2rad(alpha)
    beta=np.deg2rad(beta)
    gamma=np.deg2rad(gamma)
    g=np.array([
    [a*a, a*b*np.cos(gamma), a*c*np.cos(beta)],
    [b*a*np.cos(gamma), b*b, b*c*np.cos(alpha)], 
    [c*a*np.cos(beta),c*b*np.cos(alpha),c*c]
    ])
    vol=np.sqrt(np.linalg.det(g))
    return(vol)
    


# In[10]:


vuc(1,2,3, 90,90,90)


# #### Put it all in one cell, test again after restarting Kernel, copy to text file *.py

# In[11]:


"""
Unit Cell Volume

The following function calculates the volume of a unit cell of any crystal system 
given the lattice parameters a,b,c,alpha,beta,gamma
"""

import numpy as np

def vuc(a,b,c,alpha, beta, gamma):
    alpha=np.deg2rad(alpha)
    beta=np.deg2rad(beta)
    gamma=np.deg2rad(gamma)
    g=np.array([
    [a*a, a*b*np.cos(gamma), a*c*np.cos(beta)],
    [b*a*np.cos(gamma), b*b, b*c*np.cos(alpha)], 
    [c*a*np.cos(beta),c*b*np.cos(alpha),c*c]
    ])
    vol=np.sqrt(np.linalg.det(g))
    return(vol)


# In[12]:


vuc(1,2,3, 90,90,90)


# Now copy the above cell into a file "your".py  
# "your" = whatever name you pick.

# Now go and import your .py file in another notebook and see if it works!

# In[ ]:





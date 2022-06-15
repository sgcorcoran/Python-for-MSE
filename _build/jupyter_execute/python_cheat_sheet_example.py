#!/usr/bin/env python
# coding: utf-8

# # Example Python Cheat Sheet template

# Double click in the cell below to see how I made this Table of Contents.  For example, the first bullet below is written: ```* [import statements](#import-statements)``` the first part in the square brackets is what you see in the bullet list, the second part links to a markdown cell starting with some number of "#" and named "import statements".  You must include the dash instead of spaces in this statement. 

# #### Table of Contents
# * [import statements](#import-statements)
# * [navigation](#navigation-within-notebook)
# * [defining my own function](#defining-my-own-function)
# * [list comprehensions](#list-comprehensions)
# * [f-string](#f-string)
# * [random numbers](#random-numbers)
# * [starred expressions](#starred-expressions)
# * [equations](#equations)
# * [markdown](#markdown)
# * [dataframes](#dataframes)
# * [reading & writing excel files](#reading-&-writing-excel)
# * [plotting](#plotting)
# * [curve fitting](#curve-fitting)
# 

# #### import statements

# typical import statements
# ```python
# import numpy as np
# import pandas as pd
# from pandas import Series, DataFrame
# import matplotlib.pyplot as plt
# ```
# 
# to use special.erf()
# ```python
# from scipy import special
# ```
# 
# for curve fitting to data
# ```python
# from scipy.optimize import curve_fit
# ```

# #### navigation within notebook

# For referring to a specific section in a notebook just simply add to table of contents:
# ```python
# [link text](#entire-text-of-section-with-hyphen-for-spaces)
# ```

# #### defining my own function

# #### list comprehensions

# In[1]:


[7*x for x in [3,4,5,6,7] if x<=6 and x>3] #list comprehension style with conditional


# #### f-string

# #### random numbers

# ###### starred expressions

# #### equations

# $$\rho=\frac{\sum n A}{N_A V_{cell}}$$
# 
# $$N_{schot} = N_{sites}\ e^{\frac{-Q}{2 k_b T}}$$
# 
# $$N_{sites}=\frac{\rho N_A}{A} $$
# 
# $$\frac{C_{x,t}-C_0}{C_s-C_0}=1-Erf\left(\frac{x}{2 \sqrt{D t}}\right)$$
# 
# 

# #### markdown

# #### dataframes

# #### reading & writing excel

# #### curve fitting

# #### plotting

# [back to top](#Table-of-Contents)

# In[ ]:





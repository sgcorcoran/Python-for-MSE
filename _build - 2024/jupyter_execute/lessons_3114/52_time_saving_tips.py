#!/usr/bin/env python
# coding: utf-8

# # Time Saving Tips & Tricks

# ## Commenting out multiple lines of code

# To comment out multiple lines of code:  
# 1. Highlight the lines you want to comment
# 2. press CTRL+/
# 
# To uncomment, just repeat the above.  

# ## Switching values between two (or multiple) variables

# Rather than doing something like: 

# In[7]:


a,b=4,6
print(f' a = {a} and b = {b}')
t=a
a=b
b=t
print(f' a = {a} and b = {b}')


# you can do this: 

# In[8]:


a,b=4,6
print(f' a = {a} and b = {b}')
a,b = b,a  # you can assign multiple values at once with python
print(f' a = {a} and b = {b}')


# The previous is not only shorter but it is much easier to read and understand.  

# ## Greek Letters:

# Within a **markdown cells**, type `$\mu$` to get $\mu$.  Use LaTeX code between the dollar signs. There are LaTeX helper apps online that will give you the LaTeX code for an equation that you create with a graphical interface. Double dollar signs `$$\mu=\sqrt{\psi}$$` will place the equation on its own line. $$\mu=\sqrt{\psi} $$ 

# For **code cells**, type `\sigma` (no dollar signs) and then press the tab key. 

# In[ ]:





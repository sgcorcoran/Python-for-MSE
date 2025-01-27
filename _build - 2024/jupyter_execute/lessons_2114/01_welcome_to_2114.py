#!/usr/bin/env python
# coding: utf-8

# # Welcome to MSE 2114
# <hr style="height: 3.0px"/>

# :::{important}  
# See our [course Canvas site](https://canvas.vt.edu/courses/168196) for information on homework requirements, due dates, course expectations, grading, regrading, and announcements. 
# :::

# Make sure you follow these links to setup the Anaconda version of python on your computer: 
# *  [Anaconda install](https://docs.anaconda.com/anaconda/install/index.html)
# *  [Setup your linked-in learning account](https://canvas.vt.edu/courses/168196/pages/create-your-linked-in-learning-account)
# *  [Getting Started with Python](https://www.linkedin.com/learning/python-quick-start)
# 
# After watching and following along with "Getting Started with Python," you should be able to answer this week's homework problems.  Below are just a few additional comments and examples that might help.  

# The following `functions` and *topics* are discussed below:  
# 
# * `if`-`else`  
# * *f-string*  
# * `def`  
# * `for` loop  
# * `import numpy`  
# * *list comprehension*  
# * `np.log` vs `np.log10`
# 

# :::{note}
# There are many apps for your phone that also teach python.  Linked-in learning has an app as well so you can watch our first lesson directly on your phone.  The app Python 3 Tutorials is pretty good and you can try searching for apps related to Data Science or Python Pandas.
# :::

# ### Converting your jupyter notebook to pdf for submission in Canvas
# 
# The menu File / Download as / pdf -- does not work well.  
# 
# You need to use File/Print Preview and then right click to select print.  From the print dialogue, change the printer to `Save as PDF` or `Print to PDF Annotator`.  

# <img alt="../images/print_to_pdf.png" src="../images/print_to_pdf.png" width=200>

# :::{figure} ../images/print_to_pdf.png
# :height: 300px
# 
# In the print menu, select "Save as PDF" or "Print to PDF Annotator"
# :::

# ### Importing numpy

# At the top of your notebook, you should import the numpy extension to python.  You will need this for several of the problems this week.  
# 
# ```python
# import numpy as np
# ```
# 
# The "np" is an alias so you can type `np.sqrt()` for example rather than `numpy.sqrt()`.  

# In Canvas there is a folder called "short lessons."  These can be helpful as quick reminders on how to do something.  You can also search in google or use the help menu in the jupyter notebook.  You might want to look at the short lesson "math operations."  

# :::{note}
# It is important to start keeping a notebook called "cheat sheet" where you place common codes that you will need over and over again or how to do certain tasks such as import an excel file, etc.  There is also an android app called "Data Science Cheat Sheets" that contains a nice cheat sheet for Python.
# :::

# In[1]:


import numpy as np #we need this for all statements below that begin np. for example np.log()


# ### Writing your own functions and the if-else statement
# 
# Functions are extremely useful in python.  An example is given below.  The formatting is very important especially the indents.  If a line ends with a colon, the next line must be indented.  The function below also gives the formatting for the if, else conditional statement.  Again, notice the indented formatting.  

# In[76]:


def is_even(x):
    if x%2==0:  #the mod function "%" gives the remainder after dividing in this case by 2
        print( "That number is even")
    else:
        print("That number is odd")


# In[77]:


is_even(5)


# :::{warning}  
# Don't use input() statements in your code.  Write functions instead for changing variables for a repeated calculation.  
# :::

# Let's just look at the if-else statement by itself.  Here we have to set x to a value before entering our if-else. Try copying the code below into your own notebook and change the value of x.  

# In[45]:


x=5
if x%3==0:  #the mod function here is checking if x is divisible by 3
    print( "Yes, x is divisible by 3")
else:
    print("No, x is not divisible by 3")


# It is very important in programming to always think logically step by step through your code.  Flow charts are a great way of visualizing what your code is doing (or what you intend your code to do).  Below is a flow chart for the if-else statement.  You can see here that the if-else is just a logical test with two outcomes -> True or False

# <img alt="../images/flow_if_else.png" src="../images/flow_if_else.png" width=450>

# ```{figure} ../images//flow_if_else.png
# :width: 350px
# :name: if-else flow chart
# 
# Visualizing the 'if-else' statement
# ```

# ### f-string for formatted output

# It would be nice if our output replaced "x" with its actual value so that our output was more helpful.  We can do this with the f-string. The f located in front of the string " " says to look for { } and replace the variables with values. Let's write a function to check if a number is divisible by 3 and return the number along with whether it is or is not divisible by 3.    

# In[2]:


def isdiv3(x):
    if x%3==0:  #the mod function gives the remainder after dividing x/3
        print(f"Yes, {x} is divisible by 3")  ## notice the f in front of our string " "
    else: 
        print(f'No, {x} is not divisible by 3') ## notice the use of { } around our variable


# In[3]:


isdiv3(18)
isdiv3(19)


# :::{note}
# The f-string example above might be one of those things you save in your cheatsheet notebook.
# :::

# ### numpy log functions

# The `numpy.log()` function is base "e" and `numpy.log10()` is base "10"

# This is typically true of most programming languages.  You could also write your own functions so that you could just use ln() and log().

# We should have already run the code:  `import numpy as np` previously in this notebook.  If not, run it now.  

# In[90]:


def ln(x):
    return np.log(x)
    
def log(x):
    return np.log10(x)


# In[84]:


ln(100)


# In[86]:


log(100)


# Also, the constant *e* can be obtained by `np.e`

# In[105]:


np.e


# In[2]:


from jupytercards import display_flashcards

cards=[
    {
        "name": "numpy log example 1",
        "front": "np.log(10)",
        "back": "2.3026"
    },
    {
        "name": "numpy log10 example 1",
        "front": "np.log10(10)",
        "back": "1.0"
    },
    {
        "name": "numpy log10 example 2",
        "front": "np.log10(100)",
        "back": "2.0"
    },
    {
        "name": "numpy log10 example 3",
        "front": "np.log(np.e)",
        "back": "1.0"
    },
    {
        "name": "numpy log example 2",
        "front": "np.log(np.e**2)",
        "back": "2.0"
    }
]


# In[3]:


print("Click on the card below to view the answer. Click Next> to advance to the next card.")
display_flashcards(cards)


# ### Some basic looping

# <img alt="for loop" src="../images/flow_for_loop.png" width=350>

# ::::{margin} 
# :::{figure} ../images//flow_for_loop.png
# :height: 300px
# 
# Visualizing the `for` loop
# :::
# ::::

# Let's start the dicussion on looping with considering the flow chart for a basic `for` loop.  The `for` loop is given a list of items to be used one-by-one in the loop body.  This could be as simple as:  
# ```python
# for x in [3,5,9]:
#     print(x)
# ```  
# which would give the output:  
# 3  
# 5  
# 9

# In[8]:


for x in [3,4,5,6,7]:
    print(x**2)


# if you would like to print a list of the results rather than the result from each iteration, then we need to store the results into a list within the loop body and use `.append()` to update the list each iteration of the for loop.  Our print statement now goes outside the for loop as shown below.  

# In[9]:


y=[] #initialize an empty list for our outputs
for x in [3,4,5,6,7,8]:
    y.append(x**2) # append the current value of x**2 to the list y
print(y)


# ...or maybe we want to also find the sum of the squares

# In[10]:


y=[] #initialize an empty list for our outputs
sum=0 #initialize our variable sum
for x in [3,4,5,6,7,8]:
    y.append(x**2) # append the current value of x**2 to the list y
    sum=sum+x**2 # add the current value of x**2 to our sum
print(y)
print(sum)


# `sum=sum+x**2` works because the **right side is always calculated first** and then this value is assigned to the variable named on the left. In our case it would look like:  
# > sum = 0       initial value (outside loop)  
# 
# enter loop:  sum = current value of `sum` + current value of `x**2`   
# > sum = 0 + 9   first iteration  
# > sum = 9 + 16  second iteration  
# > sum = 25 + 36 third iteration  
# 
# and so on...

# In[4]:


from jupytercards import display_flashcards

cards=[
    {
        "name": "for loop example 1",
        "front": "<p style='text-align:left;padding-left:50px;'>y=[&nbsp]<br>for x in [3,4,5,6,7]:<br> &emsp; y.append(x**2)<br> &emsp; print(y)<br>y</p>",
        "back": "<p>[9]<br>[9, 16]<br>[9, 16, 25]<br>[9, 16, 25, 36]<br>[9, 16, 25, 36, 49]<br>[9, 16, 25, 36, 49]</p>"
    },
    {
        "name": "for loop example 2",
        "front": "<p style='text-align:left;padding-left:50px;'>y=[&nbsp]<br>for x in [3,4,5,6,7]:<br> &emsp; y.append(x**2)<br>y</p>",
        "back": "<p>[9, 16, 25, 36, 49]</p>"
    },
    {
        "name": "for loop example 3",
        "front": "<p style='text-align:left;padding-left:50px;'>for x in [3,4,5,6,7]:<br> &emsp; print(x**2)<br>x</p>",
        "back": "<p>9<br>16<br>25<br>36<br>49<br>7</p>"
    },
    {
        "name": "for loop example 4",
        "front": "<p style='text-align:left;padding-left:50px;'>for x in [3,4,5]:<br> &emsp; m=m+x<br>m</p>",
        "back": "NameError: name 'm' is not defined"
    },
    {
        "name": "for loop example 4",
        "front": "<p style='text-align:left;padding-left:50px;'>m=0<br>for x in [3,4,5]:<br> &emsp; m=m+x<br>m</p>",
        "back": "12"
    }
]


# In[5]:


print("Click on the card below to view the answer. Click Next> to advance to the next card.")
display_flashcards(cards)


# ### Special loop: List Comprehension

# This gives a nice compact way of defining a loop where the returned value is a list of outputs from each iteration.  
# **[** *value_to_save* **for** *iteration_var* **in** *list_of_items* **]**

# In[60]:


[x**2 for x in [3,4,5,6,7]] #list comprehension style


# Compare the above code to the for loop: 

# In[104]:


y=[]
for x in [3,4,5,6,7]:
    y.append(x**2)
y


# ## Exercises

# ### Problem 1:
# <hr style="height: 2.0px"/>

# Prereq: 
# *  [Setup your linked-in learning account](https://canvas.vt.edu/courses/168196/pages/create-your-linked-in-learning-account)
# *  [Getting Started with Python](https://www.linkedin.com/learning/python-quick-start)
# 
# Open a new Jupyter notebook and answer the questions below.  If a question below only requires a text response, just use a "markup" cell.  Include the problem statements below in your notebook. Use the [assignments link](https://canvas.vt.edu/courses/168196/assignments) in Canvas to upload a pdf version of your notebook.   
# 
# 1.  You learned that the two main types of data sequences in Python are the list and the tuple.  Explain in 3 sentences or less what the difference is between the two.  We will mainly use the "list."  When might you want to use the tuple instead?  
# 
# 2.  Which of the following is an example of a list: a. (1,2,3,4,5),  b. [1,2,3,4,5], c. {1,2,3,4,5}, or d. <1,2,3,4,5> ?
# 
# 3.  Find the square root of 83.
# 
# 4.  Find a random integer between 10 and 50.  
# 
# 5.  Write a function that takes a numeric value (x) and returns 0 if x is less than 0, returns x if x is between 0 and 1, returns 1 if x is greater than 1.  
# 
# 6.  Using a For loop, multiply the sequence of numbers "3,4,5,6,7" by 7 and print the result of each iteration.  Your output should be 21, 28, 35, 42, 49.  
# 
# 7.  Write a function that takes the variables: load (in N), diameter ( in m), elastic_modulus (in GPa), and yield_strength (in MPa).  The function should return "not elastic" if the applied stress is greater than the yield_strength and return the strain if the applied stress is less than or equal to the yield_strength.  The strain should be calculated using Hooke's law.  Test values:  load = 5600 N, diameter = 10 mm, E = 97 GPa, and yield_strength = 150 MPa.  Answer:  strain = $7.35 \times 10^{-4}$
# 

# ### Problem 2: 
# <hr style="height: 2.0px"/>

# After completing "Getting Started with Python", take the exam and submit a copy of the certificate that you earned.  The link for the exam can be found at the bottom of the table of contents in the left panel.  

# <img alt="intro_python_startexam.png" src="../images/intro_python_startexam.png" width=250>

# :::{image} ../images/intro_python_startexam.png
# :height: 200px
# :::

# In[ ]:





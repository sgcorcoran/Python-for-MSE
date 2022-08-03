---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.8
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Getting Started
<hr style="height: 3.0px"/>

Make sure you follow these links to setup the Anaconda version of python on your computer: 
*  [Anaconda install](https://docs.anaconda.com/anaconda/install/index.html)
*  [Setup your linked-in learning account](https://canvas.vt.edu/courses/148237/pages/getting-started-with-course)
*  [Getting Started with Python](https://www.linkedin.com/learning/python-quick-start)

After watching and following along with "Getting Started with Python," you should be able to answer this week's homework problems.  Below are just a few additional comments and examples that might help.  


if-else  
f-string  
def  
for loop  
import numpy  
list comprehension  
np.log vs np.log10



>*There are many apps for your phone that also teach python.  Linked-in learning has an app as well so you can watch our first lesson directly on your phone.  The app Python 3 Tutorials is pretty good and you can try searching for apps related to Data Science or Python Pandas.  


### Converting your jupyter notebook to pdf for submission in Canvas

The menu File / Download as / pdf -- does not work!  

You need to use File/Print Preview and then right click to select print.  From the print dialogue, change the printer to `Save as PDF` or `Print to PDF Annotator`.  

```python tags=["remove-input"]
from IPython.display import Image
fig=Image(filename='../images/print_to_pdf.png', width=200)
display(fig)
print('Use the print dialogue to convert your notebook for submitting in Canvas')
```

### Importing numpy

<!-- #region -->
At the top of your notebook, you should import the numpy extension to python.  You will need this for several of the problems this week.  

```python
import numpy as np
```

The "np" is an alias so you can type np.sqrt() for example rather than numpy.sqrt().  
<!-- #endregion -->

In Canvas there is a folder called "short lessons."  These can be helpful as quick reminders on how to do something.  You can also search in google or use the help menu in the jupyter notebook.  

For this week, you might want to look at the short lesson "math operations."  

>*I would also advise beginning a notebook called "cheat sheet" where you place common codes that you will need over and over again.  Also, reminders of how to do certain tasks such as import an excel file, etc.  There is also an android app called "Data Science Cheat Sheets" that contains a nice cheat sheet for Python.*  

```python
import numpy as np #we need this for all statements below that begin np. for example np.log()
```

### Writing your own functions and the if-else statement

Functions are extremely useful in python.  An example is given below.  The formatting is very important especially the indents.  If a line ends with a colon, the next line must be indented.  The function below also gives the formatting for the if, else conditional statement.  Again, notice the indented formatting.  


:::{important}  
Don't use input() statements in your code.  Write functions instead for changing variables for a repeated calculation.  
:::

```python
def is_even(x):
    if x%2==0:  #the mod function "%" gives the remainder after dividing in this case by 2
        print( "That number is even")
    else:
        print("That number is odd")
```

```python
is_even(5)
```

Let's just look at the if-else statement by itself.  Here we have to set x to a value before entering our if-else. Try copying the code below into your own notebook and change the value of x.  

```python
x=5
if x%3==0:  #the mod function here is checking if x is divisible by 3
    print( "Yes, x is divisible by 3")
else:
    print("No, x is not divisible by 3")

```

It is very important in programming to always think logically step by step through your code.  Flow charts are a great way of visualizing what your code is doing (or what you intend your code to do).  Below is a flow chart for the if-else statement.  You can see here that the if-else is just a logical test with two outcomes -> True or False

```python tags=["remove-input"]
# tags:  remove-input
# this will remove the code below when building Jupyter-book and create a button to show the image below when clicked. 

from IPython.display import Image
fig=Image(filename='../images/flow_if_else.png', width=350)
display(fig)
print('Figure 1: some text')
```

```python
### Now written as a function  
def isdiv3(x):
    if x%3==0:  #the mod function gives the remainder after dividing x/3
        print( "Yes, x is divisible by 3")
    else:
        print("No, x is not divisible by 3")
```

```python
isdiv3(18)
isdiv3(19)
```

### f-string for formatting output


*It would be nice if our output replaced "x" with its actual value so that our output was more helpful.  We can do this with the f-string. The f located in front of the string " " says to look for { } and replace the variables with values.*  

```python
def isdiv3(x):
    if x%3==0:  #the mod function gives the remainder after dividing x/3
        print(f"Yes, {x} is divisible by 3")  ## notice the f in front of our string " "
    else: 
        print(f'No, {x} is not divisible by 3') ## notice the use of { } around our variable
```

```python
isdiv3(18)
isdiv3(19)
```

>*The f-string for formatting output might be one of those things you save in your cheatsheet notebook.*


### The `numpy.log()` function is base "e" and `numpy.log10()` is base "10"


This is typically true of most programming languages.  You could also write your own functions so that you could just use ln() and log().


We should have already run the code:  `import numpy as np` previously in this notebook.  If not, run it now.  

```python
def ln(x):
    return np.log(x)
    
def log(x):
    return np.log10(x)
```

```python
ln(100)
```

```python
log(100)
```

<!-- #region tags=["remove-cell"] -->
> *** note for self, will be removed in Jupyter Book ***

* flashcards here for np.log(10), np.log10(10), np.log10(100), np.log(np.e), np.e
<!-- #endregion -->

### Some basic looping

<!-- #region -->
Let's start the dicussion on looping with considering the flow chart for a basic `for` loop.  The `for` loop is given a list of items to be used one-by-one in the loop body.  This could be as simple as:  
```python
for x in [3,5,9]:
    print(x)
```  
which would give the output:  
3  
5  
9
<!-- #endregion -->

```python tags=["remove-input"]
fig=Image(filename='../images/flow_for_loop.png', width=350)
display(fig)
print('Move through item list until the end is reached')
```

```python
for x in [3,4,5,6,7]:
    print(x**2)
```

if you would like to print a list of result rather than the result from each iteration, then we need to store the results into list within the loop body.  `append` can be used for this pupose but don't forget to initialize this list outside of the loop.  

```python
y=[] #initialize an empty list for our outputs
for x in [3,4,5,6,7,8]:
    y.append(x**2) # append the current value of x**2 to the list y
print(y)
```

...or maybe we want to also find the sum of the squares

```python
y=[] #initialize an empty list for our outputs
sum=0 #initialize our variable sum
for x in [3,4,5,6,7,8]:
    y.append(x**2) # append the current value of x**2 to the list y
    sum=sum+x**2 # add the current value of x**2 to our sum
print(y)
print(sum)
```

`sum=sum+x**2` works because the **right side is always calculated first** and then this value is assigned to the variable named on the left. In our case it would look like:  
> sum = 0       initial value (outside loop)  

enter loop:  sum = current value of `sum` + current value of `x**2`   
> sum = 0 + 9   first iteration  
> sum = 9 + 16  second iteration  
> sum = 25 + 36 third iteration  

and so on...

<!-- #region -->
create quiz here asking students what the output for: 

```python
y=[]
for x in [3,4,5,6,7]:
    y.append(x**2)
    print(y)
print(y)

for x in [3,4,5,6,7]:
    print(x**2)
print(x)


for x in [3,4,b,6,7]:
    print(x**2)
    
for x in [3,4,5]:
    m=m+x
print(m)

```


<!-- #endregion -->

### Special loop: List Comprehension


This gives a nice compact way of defining a loop where the returned value is a list of outputs from each iteration.  
**[** *value_to_save* **for** *iteration_var* **in** *list_of_items* **]**

```python
[x**2 for x in [3,4,5,6,7]] #list comprehension style
```

Compare the above code to the for loop: 

```python
y=[]
for x in [3,4,5,6,7]:
    y.append(x**2)
y
```

## Exercises


### Problem 1:
<hr style="height: 2.0px"/>


Prereq: 
*  [Setup your linked-in learning account](https://canvas.vt.edu/courses/127967/pages/getting-started-with-python)
*  [Getting Started with Python](https://www.linkedin.com/learning/python-quick-start)

Open a new Jupyter notebook and answer the questions below.  If a question below only requires a text response, just use a "markup" cell.  Include the problem statements below in your notebook. Use the [assignments link](https://canvas.vt.edu/courses/127967/assignments) in Canvas to upload a pdf version of your notebook.   

1.  You learned that the two main types of data sequences in Python are the list and the tuple.  Explain in 3 sentences or less what the difference is between the two.  We will mainly use the "list."  When might you want to use the tuple instead?  

2.  Which of the following is an example of a list: a. (1,2,3,4,5),  b. [1,2,3,4,5], c. {1,2,3,4,5}, or d. <1,2,3,4,5> ?

3.  Find the square root of 83.

4.  Find a random integer between 10 and 50.  

5.  Write a function that takes a numeric value (x) and returns 0 if x is less than 0, returns x if x is between 0 and 1, returns 1 if x is greater than 1.  

6.  Using a For loop, multiply the sequence of numbers "3,4,5,6,7" by 7 and print the result of each iteration.  Your output should be 21, 28, 35, 42, 49.  

7.  Write a function that takes the variables: load (in N), diameter ( in m), elastic_modulus (in GPa), and yield_strength (in MPa).  The function should return "not elastic" if the applied stress is greater than the yield_strength and return the strain if the applied stress is less than or equal to the yield_strength.  The strain should be calculated using Hooke's law.  Test values:  load = 5600 N, diameter = 10 mm, E = 97 GPa, and yield_strength = 150 MPa.  Answer:  strain = $7.35 \times 10^{-4}$


<!-- #region tags=[] -->
### Problem 2: 
<hr style="height: 2.0px"/>
<!-- #endregion -->

After completing "Getting Started with Python", take the exam and submit a copy of the certificate that you earned.  The link for the exam can be found at the bottom of the table of contents in the left panel.  

```python tags=["remove-input"]
fig=Image(filename='../images/intro_python_startexam.png', width=250)
display(fig)
print('Link for exam')
```

```python

```

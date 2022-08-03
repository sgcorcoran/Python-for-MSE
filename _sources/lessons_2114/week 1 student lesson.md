---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.7.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

**Week 1:** Student Lesson
<hr style="height: 3.0px"/>

Make sure you follow these links to setup the Anaconda version of python on your computer: 
*  [Setup your linked-in learning account](https://canvas.vt.edu/courses/127967/pages/getting-started-with-course)
*  [Getting Started with Python](https://www.linkedin.com/learning/python-quick-start)

After watching and following along with "Getting Started with Python," you should be able to answer this week's homework problems.  Below are just a few additional comments and examples that might help.  


>*There are many apps for your phone that also teach python.  Linked-in learning has an app as well so you can watch our first lesson directly on your phone.  The app Python 3 Tutorials is pretty good and you can try searching for apps related to Data Science or Python Pandas.  


**Converting jupyter notebook to pdf**

The menu File/Download an/pdf -- does not work!  

You need to use File/Print Preview and then right click to select print.  From the print dialogue, change the printer to "save as pdf."  
<div>
<img src="attachment:image.png" width="250" />
</div>

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

**Writing your own functions**

Functions are extremely useful in python.  An example is given below.  The formatting is very important especially the indents.  If a line ends with a colon, the next line must be indented.  The definition below also gives the formatting for the if, else conditional statement.  Again, notice the indented formatting.  

```python
def isdiv3(x):
    if np.mod(x,3)==0:  #the mod function gives the remainder after dividing x/3
        print( "Yes, x is divisible by 3")
    else:
        print("No, x is not divisible by 3")
```

```python
isdiv3(18)
isdiv3(19)
```

*Would be nice if our output replaced "x" with its actual value.  We can do this with the f-string.*  

```python
def isdiv3(x):
    if np.mod(x,3)==0:  #the mod function gives the remainder after dividing x/3
        print(f"Yes, {x} is divisible by 3")
    else:
        print(f'No, {x} is not divisible by 3')
```

```python
isdiv3(18)
isdiv3(19)
```

>*The f-string for formatting output might be one of those things you save in your cheatsheet notebook.*


You could write your own ln() and log() functions:

```python
np.log(10)
```

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
np.log(100)
```

**Some basic looping**

```python
for x in [3,4,5,6,7]:
    print(x**2)
```

```python
y=[]
for x in [3,4,5,6,7]:
    y.append(x**2)
print(y)
```

```python
[x**2 for x in [3,4,5,6,7]] #list comprehension style
```

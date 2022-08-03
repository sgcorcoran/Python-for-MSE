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

# MSE 2114 Week 3: Student Lesson - Importing Data


## Week 3 Homework


**All Problems are due. 1-5 and P1, P2**  <hr style="height: 3.0px"/>

**Prereq:**

This problem requires us to know how to:
* import an excel file
* define a function
* use if, elif, else statements
* use numpy.array() to multiply a sequence of numbers
* generate a random number
* use matplotlib to make a scatter plot

**Problem Statement:**   

(1) Import the load-length data in file "Al7075.xlsx" The header in the excel file should give you all the information you need.  Plot the stress-strain data.  Put the stress in units of MPa.  

(2) Take the first couple of data points and determine the slope by fitting a straight line to the data.  You may want to replot the first quarter or so of the original plot so that you can see how far the linear region extends.  

(3) Add a line to your plot that starts at a strain of 0.002 and has the slope found previously.  Plot this line so that it intersects the stress-strain data curve and read off the yield strength.  You should only plot the first quarter or so of the original plot so that you can clearly see the yield point value.  

(4) Add a horizontal line to your plot at the yield point value estimated above. Refine your estimate if your horizontal line does not pass correctly through the intersection point.  

(5) Export your data to a new excel file. 

**Practice**

(P1)  Write a function that given the ionic radii for a simple ceramic compound returns the expected coordination number.  The coordinaton numbers versus ratio of the radii can be found in Chapter 12,  Table 12.2 on page 408 in Callister 10th ed.  Your function should check if your ratio is greater than 1.0.  If it is, then take the inverse of your ratio.  You may want to consider the `if` `elif` `else` conditionals. Test your function by calculating the coordination number for NaCl.  Remember to use the ionic radii not the atomic radii.  

(P2)  Pick 1000 random points in a square of edge length 2 centered at (0,0).  Determine how many of these points are contained in a circle of radius 1 centered at (0,0).  Multiply the ratio of points in the circle to total number of points by 4, i.e. $4\times \frac{\text{pts in circle}}{\text{total num pts}}$.  What do you get?  



## Lesson Part 1: Importing, Cleaning, Exporting Excel data


### import numpy, pandas, matplotlib, and pathlib

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from pathlib import Path
```

### How to define file paths 


First we need to define our path to the file we want to import.  If you find the file on your machine, you can right click on it and select properties. 

![title](./images/week%203%20image%201.png)

By highlighting the text in the "location" box you can copy ctrl-c and paste directly in your notebook ctrl-v.  For me this would give: 

C:\Users\sgc\Google Drive\Teaching\2114 & 3114 Math I & II\git_2114_3114\data for practice

now I just need to add "\filename" to the end.  For example, 

C:\Users\sgc\Google Drive\Teaching\2114 & 3114 Math I & II\git_2114_3114\data for practice\Student credit hours dept numbers.xlsx

It is very important to remember to include the file extension at the end. 

```python
#Use one of the below in your coding and stick to it.  
# see note below about the "r" in the first line below
path1=Path(r"C:\Users\sgc\Google Drive\Teaching\2114 & 3114 Math I & II\2114 python")
# using forward slash is good and doesn't require the "r"
path2=Path("C:/Users/sgc/Google Drive/Teaching/2114 & 3114 Math I & II/2114 python")
# I'm going to use path1 because that is how windows pastes my filepath 
```

```python
path=Path(r"C:\Users\sgc\Google Drive\Teaching\2114 & 3114 Math I & II\git_2114_3114\data for practice")
filename='Al7075.xlsx'
fullpath=path / filename
# if getting error about object not appearing to be 8-bit string path then use
# str(fullpath)
fullpath
```

Windows likes to use "\\" rather than "/".  The only problem is that "\\" also has another meaning in python so we need to put "r" out front of our string to tell python to interpret our string as a regular expression.  

`
path = Path(r"C:\Users\sgc\Google Drive\Teaching\2114 & 3114 Math I & II\git_2114_3114\data for practice")
`

>Notice the "r" outfront with no space before our string.  

<!-- #region heading_collapsed=true -->
### Import Data using Pandas
<!-- #endregion -->

<!-- #region hidden=true -->
Let's take a look at some student credit hours taught for engineering departments. 
<!-- #endregion -->

```python hidden=true
path=Path(r"C:\Users\sgc\Google Drive\Teaching\2114 & 3114 Math I & II\git_2114_3114\data for practice")
filename='Student credit hours dept numbers.xlsx'
fullpath=path / filename

raw_excel=pd.read_excel(fullpath)
raw_excel
```

<!-- #region heading_collapsed=true -->
### Clean data
<!-- #endregion -->

```python hidden=true
# let's drop rows and columns that have no data
df=raw_excel.dropna(how='all', axis=0) #removes rows
# try changing 'all' to 'any' in these commands.  What is the result? 
df=df.dropna(how='all', axis=1) #now remove columns
df
```

<!-- #region hidden=true -->
looks like we have an extra row at the top.  Let's drop that one also.  Notice the left column which is the row index is 5 so we drop by identifying the index.  
<!-- #endregion -->

```python hidden=true
df=df.drop(5)
# now lets rename our columns
df.columns=['num faculty','dept','on campus','off campus', 'total', 'SCH per faculty']
df
```

```python hidden=true
df=df.drop(6) # we don't need the first row again now labeled "6"
df=df.reset_index(drop=True) #reset row numbering
df=df.fillna(0) #replace NaN with 0
df
```

<!-- #region heading_collapsed=true -->
### Analysis
<!-- #endregion -->

<!-- #region heading_collapsed=true hidden=true -->
#### sorting, slicing, math on columns, adding new columns
<!-- #endregion -->

```python hidden=true
# sort data frame by values in column "num faculty"
sch_data=df.sort_values(['num faculty','dept']).reset_index(drop=True)
#try removing ".reset_index()" and see what you get
#or change drop=True to drop=Fals and see what happens
sch_data
```

```python hidden=true
# we don't need lines 0 - 4 so let's take only 5-15
sch_data=sch_data[5:16]
sch_data
```

```python hidden=true
sch_data=sch_data.reset_index(drop="True")
sch_data
```

<!-- #region hidden=true -->
We can easily refer to a column of data by its header, for example:
<!-- #endregion -->

```python hidden=true
sch_data['dept']
```

<!-- #region hidden=true -->
Let's take the total credit hours and divide by the total faculty then add this to our dataframe.  
<!-- #endregion -->

```python hidden=true
sch_data['credit_faculty']=(sch_data['total']/sch_data['num faculty'])
sch_data
```

<!-- #region hidden=true -->
#### plotting using matplotlib.pyplot,  fitting using scipy.optimize curvefit
<!-- #endregion -->

<!-- #region hidden=true -->
now let's plot the credit_faculty vs the num faculty
<!-- #endregion -->

```python hidden=true
plt.plot(sch_data['num faculty'], sch_data['credit_faculty'], 'ro')
plt.ylabel('student credit hours per faculty')
plt.xlabel('number of faculty in department')
plt.show()
```

<!-- #region hidden=true -->
It looks like a linear relationship exists for smaller departments.  Let's fit the data for departments with faculty less than 30.
<!-- #endregion -->

```python hidden=true
#test the data for cases where the number of faculty is < 30
test=sch_data['num faculty']<30
#now let's select those data
sch_slice=sch_data[test]
sch_slice
```

```python hidden=true
# plt.plot(x, y, 'formatting') 'ro' means red points
plt.plot(sch_slice['num faculty'], sch_slice['credit_faculty'], 'ro')
plt.ylabel('student credit hours per faculty')
plt.xlabel('number of faculty in department')
plt.show()
```

```python hidden=true
#read in package for curve fitting
from scipy.optimize import curve_fit
```

```python hidden=true
#define a function for the fit.  In this case just a line
def lin(x, m, b):
    return m*x+b

best_vals, covar = curve_fit(lin, sch_slice['num faculty'], sch_slice['credit_faculty'])
print(f'Our fit is given by {best_vals[0]:.2f} x + {best_vals[1]:.2f}')
```

```python hidden=true
print(best_vals) #these are in order as defined in function i.e. m , b
```

```python hidden=true
plt.plot(sch_slice['num faculty'], lin(sch_slice['num faculty'],11.105,-61.6635), 'k--')
plt.plot(sch_data['num faculty'], sch_data['credit_faculty'], 'ro')
plt.show()
```

<!-- #region hidden=true -->
Let's add a horizontal line at 275
<!-- #endregion -->

```python hidden=true
plt.plot(sch_slice['num faculty'], lin(sch_slice['num faculty'],11.105,-61.6635), 'k--')
plt.plot(sch_data['num faculty'], sch_data['credit_faculty'], 'ro')
plt.axhline(y=275, linewidth=1, color='b', linestyle='-')
plt.axis([10,70,50,400]) #specify axis limits like this
plt.show()
```

### Exporting data to excel

```python
# .loc[rows, columns] lets us use the names of the columns and rows
#in our case rows = ":" which means all rows
# columns is a list of columns to take ["num faculty",'credit_faculty']
data_to_save=sch_data.loc[:,["num faculty",'credit_faculty']]
data_to_save
```

```python
path=Path(r"C:\Users\sgc\Google Drive\Teaching\2114 & 3114 Math I & II\git_2114_3114\data for practice")
filename='lesson 3 outfile.xlsx'
outpath=path / filename

data_to_save.to_excel(outpath, index = True, header=True)
#try changing index=True and check your output file 
```

Here's what my excel file looks like: 
![image.png](attachment:image.png)


## Lesson Part 2: Practice


### Functions, List comprehensions, Random numbers, Selecting data using conditionals


Let's look at if, elif, else statements again

```python
def myfunc(var1, var2, var3):
    
    #first if, else statement avoids dividing by zero
    if var1 ==0:
        return(0)
    else: ratio=var3/var1
    
    #second if, elif, else statement
    if ratio < 0:
        return(50)
    elif ratio == 0:
        return(1)
    elif ratio == 0.5:
        return(60)
    else: return(ratio)
```

```python
np.linspace(-1,4,21)
```

```python
[myfunc(x,3,1.5) for x in [0,1,2,3]]
```

```python
plt.plot(np.linspace(-1,4,21), [myfunc(x,3,1.5) for x in np.linspace(-1,4,21)], 'ro')
plt.show()
```

### (P2) Let's determine if a random point between 0 and 1 in both x and y falls inside a circle with center (0.5, 0.5) 

```python
# !! important note:  I use np.array below because I'm manually converting a list but
#  you will use np.random which will give you an array as its output
xcoord=np.array([0, 0.5, 1]) #convert lists [] to numpy array
ycoord=np.array([0, -0.5, 0.8])
magnitude=np.sqrt((xcoord-0.5)**2+(ycoord-0.5)**2)
magnitude
```

```python
fig, ax = plt.subplots()
ax.plot(xcoord, ycoord, 'ro')
ax.set_aspect('equal')
plt.show()
```

```python
test=magnitude<0.7
x=xcoord[test] #take all x values where magnitude array is <0.7
y=ycoord[test] #take all y values where magnitude array is <0.7
```

```python
fig, ax = plt.subplots()
ax.plot(xcoord, ycoord, 'ro') # 'ro' means red points
ax.plot(x, y, 'ko') #'ko' means black points
ax.set_aspect('equal')
plt.show()
```

```python
# if I want the number of points I need to find the length of my coordinates
len(xcoord)
```

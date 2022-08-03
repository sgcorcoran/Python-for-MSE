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

**Week 4:**<hr style="height: 3.0px"/>
This problem requires us to know how to:
* import libraries `numpy`, `sympy`, `matplotlib`;
* symbolically manipulate an equation using `sympy.solve()`;
* generate x and y data for a function using `numpy.linspace()`;
* plot the x, y data using `matplotlib.pyplot.plot()`;
* add horizontal lines and text to a plot.

**Problem Statement:**  Computations of the Density and Percent Crystallinity of Polyethylene (Callister 10th ed., section 14.11)
        
The % crystallinity is given by:

 $$  \mathbf{\text{% crystallinity} =  \frac{\rho_c (\rho_s - \rho_a)}{\rho_s (\rho_c - \rho_a)} * 100} $$

(1) Calculate the percent crystallinity of a branched polyethylene that has a density of  $0.925\ 𝑔\ 𝑐𝑚^{-3}$ . The density of a totally amorphous material is  $0.870 \ 𝑔\ 𝑐𝑚^{-3}$  and the density of a totally crystalline material is  $0.998 \ 𝑔\ 𝑐𝑚^{-3}$ .

(2) Calculate the density versus % crystallinity and reproduce the following plot (including the horizontal lines and text):

![image-2.png](attachment:image-2.png)

(3) Export your data to an excel file. 

**Practice**

(P1) Write a function that finds "x" random points in a square of edge length 2 centered at (0,0). Determines how many of these points are contained in a circle of radius 1 centered at (0,0). Returns the value $\left(4\times \frac{\text{pts in circle}}{\text{total num pts}}\right)$.  Plot the value $\left(4\times \frac{\text{pts in circle}}{\text{total num pts}}\right)$ versus number of points, x.  Also include a horizontal line at the value of pi on your plot.  

(P2) Import the csv file "titanic.csv" and (a) determine the percentage of woman that survived and the percentage of men that survived and (b) determine the average ticket price (Fare) for those that survived versus those that did not survive.  0 = did not survive. 1 = survived.  



#### You will need the following extensions

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sympy.solvers import solve #for solving equations symbolically
from sympy import symbols #for solving equations symbolically
```

#### (1) For this part you will want to write a simple function that takes sample_density, amorphous_density and crystalline_density and returns the percent_crystallinity


 $$  \mathbf{\text{% crystallinity} =  \frac{\rho_c (\rho_s - \rho_a)}{\rho_s (\rho_c - \rho_a)} * 100} $$

```python
def crystallinity(density_s, density_a, density_c):
    return density_s*density_a*density_c


```

```python
crystallinity(0.925, 0.870, 0.998)
```

<!-- #region -->
#### (2) You will want to solve the given equation for the sample_density.  Then you can write a function that takes percent_crystallinity, crystalline_density and amorphous_density and returns the sample density. 

For this you need the two import commands that we already ran above: 

```python
from sympy.solvers import solve #for solving equations symbolically
from sympy import symbols #for solving equations symbolically
```
<!-- #endregion -->

Let's say you wanted to solve the equation $a x^2 + b x + c = d$.  First, we tell python that a,b,c,d,x are symbols.  

```python
a,b,c,d,x = symbols('a b c d x')
```

Then we can use the solve command.  The equation that goes into the solve command must equal zero so we reqrite $a x^2 + b x + c = d$   as   $a x^2 + b x + c - d=0$.  Notice that we do not include the "=0" part in the solve function below because that is assumed. 

```python
# solve for x
solve(a*x**2+b*x+c-d, x)
```

```python
def x_solution(a,b,c,d):
    return (-b + np.sqrt(-4*a*c + 4*a*d + b**2))/(2*a)

x_solution(2,9,5,10)
```

```python
x_solution(2,9,0.4,10)
```

below I can plot how our solution varies with the parameter "d"


The np.linspace(min, max, numpts) creates evenly spaced points between two numbers.  The number of points you want is given by the third number.

```python
dd=[1,2,3,4,5]
[x_solution(2,9,5,d) for d in dd]

```

```python
d=np.linspace(0, 50, 20) #creates 20 evenly spaced pts from 0 to 50
x_sol=x_solution(2,9,5,d)
plt.plot(d,x_sol,'ro')
plt.xlabel('d')
plt.ylabel('x solution')
plt.annotate('$a x^2 + b x + c = d$', xy=(5, 2.5), color='b') # you can include text on your plot
plt.annotate('$a x^2$', xy=(40, 0.5), color='b') # you can include text on your plot
plt.show()
```

#### (P1) Write a function that finds "x" random points in a square of edge length 2 centered at (0,0). Determines how many of these points are contained in a circle of radius 1 centered at (0,0). Returns the value $\left(4\times \frac{\text{pts in circle}}{\text{total num pts}}\right)$.  Plot the value $\left(4\times \frac{\text{pts in circle}}{\text{total num pts}}\right)$ versus number of points, x.  Also include a horizontal line at the value of pi on your plot. 


From week 3, we did this for 1000 random points.  My code for this was: 

```python
xcoord=(2)*np.random.random(1000)-1 #1000 random pts from -1 to 1
ycoord=(2)*np.random.random(1000)-1 #1000 random pts from -1 to 1
magnitude=np.sqrt(xcoord**2+ycoord**2) #length from center (0,0) to point
mag_test=magnitude<=1
4*len(xcoord[mag_test])/len(xcoord)
```

```python
len(xcoord[magnitude<=1])
```

```python
len(xcoord)
```

Write the above as a function so you can plot the output vs number of points.  Since your number of point chosen, might go from say 1 to 1,000,000 try using geomspace() rather than linspace().  geomspace() gives pts spaced on a log scale which is much better when our values change by orders of magnitude. You could also use linspace() or arange() but with any reasonable step size for the data on the low end you will end up needing a lot of points!  

Don't forget that your function above requires an integer to be input so you will want to make sure geomspace() is giving you an integer or round your list to the nearest integer.  

```python
xdata=np.geomspace(100,1e6,num=50, dtype=int) #tell it to round to the closest integer dtype=int
xdata
# notice the increasing step size as our numbers get larger
```

#### (P2) Import the csv file "titanic.csv" and (a) determine the percentage of woman that survived and the percentage of men that survived and (b) determine the average ticket price (Fare) for those that survived versus those that did not survive.  0 = did not survive. 1 = survived. 


In lesson 3 we learned how to use pandas to: 
> * import an excel file (now we import a csv file)
> * clean imported data: dropping NAN, filling NAN, renaming columns, dropping rows
> * sorting, slicing, adding new columns
> * Now we need to learn how to group (aggregate) data:  groupby(), sum(), mean()

```python
from pathlib import Path
```

```python
path=Path(r"C:\Users\sgc\Google Drive\Teaching\2114 & 3114 Math I & II\git_2114_3114\data for practice\plastic-cable-insulation-thickness")
filename='raw_clean.csv'
fullpath=path / filename

raw=pd.read_csv(fullpath)
raw.head()
```

```python
# dropping first two columns here since I don't need them
df=raw.drop(['Unnamed: 0','Unnamed: 0.1'],axis=1)
df
```

```python
# rounding some of the numbers so they group better
df['LineSpeed']=df.loc[:,'LineSpeed'].round(1)
df['ExtrTemp']=df.loc[:,'ExtrTemp'].round(0)
df
```

1. Let's find the percentage of Measurements made in Alexandria vs the total number of measurements.  
2. Let's also find the average WaterTemp for all measurements made in Alexandria at a ExtrTemp of 235.0  

```python
# groupby collects all records for the different cities and then
# counts how many records there are
dfgroup=df.groupby(['City']).count()
dfgroup
# try the line below and see what it gives
# dfgroup=df.groupby(['City']).size()
# dfgroup
```

```python
# using .sum() we can get the total number of records in each column
dfgroup.sum()
```

```python
# calculating percent of records in Alexandria vs total of 9997
# using .loc[] to pull from dataframe "dfgroup"
# .loc[row, column]
dfgroup.loc['Alexandria','Measure']/9997*100 #percent
```

```python
# now we are grouping by two columns
# we first collect the Cities
# then group within eqach city by the ExtrTemp
# here we take the mean value in these two categories for each column
dfmean=df.groupby(['City','ExtrTemp']).mean()
dfmean
```

```python
# the mean value of WaterTemp in Alexandria at an ExtrTemp of 235 degrees is
dfmean.loc[('Alexandria',235.0), 'WaterTemp']
```

#### For a lot more control, we could use pivot_table to specify different aggregation functions for each column of values we want to analyze.  You should be able to do what you want with groupby() but the pivot_table is a more manual way to specify many options.  

```python
pd.pivot_table(df, values=['Measure', 'WaterTemp','LineSpeed'], index=['City', 'ExtrTemp'],
                    aggfunc={'Measure': np.mean,
                             'WaterTemp': [min, max, np.mean],
                            'LineSpeed':[np.sum,np.mean,np.size]})
```

```python

```

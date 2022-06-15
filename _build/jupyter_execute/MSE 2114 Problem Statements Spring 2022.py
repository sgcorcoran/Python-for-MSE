#!/usr/bin/env python
# coding: utf-8

# # MSE 2114 Math Methods I

# ## Homework

# **Week 1:** 
# <hr style="height: 2.0px"/>
# 
# Prereq: 
# *  [Setup your linked-in learning account](https://canvas.vt.edu/courses/127967/pages/getting-started-with-python)
# *  [Getting Started with Python](https://www.linkedin.com/learning/python-quick-start)
# 
# Open a new Jupyter notebook and answer the questions below.  If a question below only requires a text response, just use a "markup" cell.  Include the problem statements below in your notebook. Use the [assignments link](https://canvas.vt.edu/courses/127967/assignments) in Canvas to upload a pdf version of your notebook.   
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

# ### Week 2:  
# ***
# 
# Prereq: Week 2 Exercises
# 
# This problem requires us to know how to:
# * comment notebooks using Markdown cells
# * write equations in Markdown cells
# * use `print()` statement and **f-string** for better presentation of your final answer
# * use `numpy` extension
# * use `scipy.special` extension
# 
# **Problem Statement:** Simple numeric problems 
# 
# Find the numeric solutions to the problems below.  Make sure you include the original problem statement for each problem in your jupyter notebook.  Use Markdown to indicate the equations used. These should be nicely formatted, i.e. superscripts, subscripts, greek letters, etc.  Present your final answer using a `print()` statement and include units.  An f-string might be useful.
# 
# (1) (Chap 12 10th ed. Callister) NaCl has a cubic unit cell with an edge length equivalent to $2 r_{Na^{+}} + 2 r_{Cl^{-}}$.  If the ionic radii are 0.102 and 0.181 nm respectively, compute the volume of the unit cell.  Remember to use a Markdown cell to write the final equation you are using.
# >Remember in Python exponents used in calculations are written `**` and not as `^`.  
# 
# (2) (Chap 12 10th ed. Callister) If the atomic weights of Na and Cl are 22.99 and 35.45 $g/mol$ respectively and the unit cell contains $4 Na^+$ and $4 Cl^-$ ions, compute the density of NaCl in units of $g/cm^3$.  Use $6.022 \times 10^{23}$ for Avagadro's number.  
# 
# (3) (Chap 12 10th ed. Callister) Calculate the number of Schottky defects per cubic meter in potassium chloride at 500 $^{\circ}$C. The energy required to form each Schottky defect is 2.6 eV and the density for KCl at 500 $^{\circ}$C is 1.955 $g/cm^3$. The atomic weight for K and Cl is 39.10 and 35.45 g/mol respectively.
# >This problem will require the numpy package. Use the statement: `import numpy as np` then you can use `np.exp()`.
# 
# (4) (Chap 5 10th ed. Callister) We want to harden the steel surface of a plate by carburization.  Our setup is such that the surface concentration of carbon is 1.20 wt%, the initial carbon in our steel sample is 0.2 wt%, at our processing temperature the diffusion coefficient is $1.6 \times 10^{-11}$ $m^2 / s$, and our carburizing time is 5 hours.  Will the concentration at a depth of 0.5 mm exceed our target value of 0.80 wt%?  
# > This problem will require the scipy.special package. Use the statement: `from scipy import special` then you can use `special.erf()`.  
# 
# **Practice**
# 
# (5) Define a function called unitcell_density where given: edgelength, num_atoms_1, num_atoms_2, A1, and A2, the function returns the density in units of $g/cm^3$. Your function can assume a cubic unit cell.  Use your function to repeat problem (2) above.  Use comments to indicate what units are expected for the input variables.  
# 
# (6) Does your function in the previous problem work for single element materials?  Try using it to find the density of gold given the atomic radius of 0.1442 nm and the atomic weight of 196.96 g/mol. Recall that the edge length for fcc gold is given by $2 R \sqrt{2}$ and the fcc unit cell contains a total of 4 atoms. Your answer should be given in units of $g/cm^3$.  

# ### Week 3:
# ***
# Prereq:
# 
# This problem requires us to know how to:
# * import an excel file
# * define a function
# * use `if, elif, else` statements
# * use `numpy.array()` to multiply a sequence of numbers
# * generate a random number, `np.random()`
# * find the length of an array `len()`
# 
# **Problem Statement:** import, manipulate and plot data  
# 
# (1) Import the load-length data in file "Al7075.xlsx" The header in the excel file should give you all the information you need.  Plot the stress-strain data.  Put the stress in units of MPa.  
# 
# (2) Take the first couple of data points and determine the slope by fitting a straight line to the data.  You may want to replot the first quarter or so of the original plot so that you can see how far the linear region extends.  
# 
# (3) Add a line to your plot that starts at a strain of 0.002 and has the slope found previously.  Plot this line so that it intersects the stress-strain data curve and read off the yield strength.  You should only plot the first quarter or so of the original plot so that you can clearly see the yield point value.  
# 
# (4) Add a horizontal line to your plot at the yield point value estimated above. Refine your estimate if your horizontal line does not pass correctly through the intersection point.  
# 
# (5) Export your data to a new excel file. 
# 
# **Practice**
# 
# (P1)  Write a function that given the ionic radii for a simple ceramic compound returns the expected coordination number.  The coordinaton numbers versus ratio of the radii can be found in Chapter 12,  Table 12.2 on page 408 in Callister 10th ed.  Your function should check if your ratio is greater than 1.0.  If it is, then take the inverse of your ratio.  You may want to consider the `if` `elif` `else` conditionals. Test your function by calculating the coordination number for NaCl.  Remember to use the ionic radii not the atomic radii. 
# 
# (P2)  Pick 1000 random points in a square of edge length 2 centered at (0,0).  Determine how many of these points are contained in a circle of radius 1 centered at (0,0).  Multiply the ratio of points in the circle to total number of points by 4, i.e. $4\times \frac{\text{pts in circle}}{\text{total num pts}}$.  What do you get?  
# 

# **Week 4:**<hr style="height: 3.0px"/>
# This problem requires us to know how to:
# * import libraries `numpy`, `sympy`, `matplotlib`;
# * symbolically manipulate an equation using `sympy.solve()`;
# * generate x and y data for a function using `numpy.linspace()`;
# * plot the x, y data using `matplotlib.pyplot.plot()`;
# * add horizontal lines and text to a plot.
# 
# **Problem Statement:**  Computations of the Density and Percent Crystallinity of Polyethylene (Callister 10th ed., section 14.11)
#         
# The % crystallinity is given by:
# 
#  $$  \mathbf{\text{% crystallinity} =  \frac{\rho_c (\rho_s - \rho_a)}{\rho_s (\rho_c - \rho_a)} * 100} $$
# 
# (1) Calculate the percent crystallinity of a branched polyethylene that has a density of  $0.925\ 𝑔\ 𝑐𝑚^{-3}$ . The density of a totally amorphous material is  $0.870 \ 𝑔\ 𝑐𝑚^{-3}$  and the density of a totally crystalline material is  $0.998 \ 𝑔\ 𝑐𝑚^{-3}$ .
# 
# (2) Calculate the density versus % crystallinity and reproduce the following plot (including the horizontal lines and text):
# 
# ![image.png](attachment:image.png)
# 
# (3) Export your data to an excel file. 
# 
# **Practice**
# 
# (P1) Write a function that finds "x" random points in a square of edge length 2 centered at (0,0). Determines how many of these points are contained in a circle of radius 1 centered at (0,0). Returns the value $\left(4\times \frac{\text{pts in circle}}{\text{total num pts}}\right)$.  Plot the value $\left(4\times \frac{\text{pts in circle}}{\text{total num pts}}\right)$ versus number of points, x.  Also include a horizontal line at the value of pi on your plot.  
# 
# (P2) Import the csv file "titanic.csv" and (a) determine the percentage of woman that survived and the percentage of men that survived and (b) determine the average ticket price (Fare) for those that survived versus those that did not survive.  0 = did not survive. 1 = survived.  

# **Week 5:**<hr style="height: 3.0px"/>  
# 

# 1. Read in the data file: Tafel data for 2114.xlsx
# 2. Check the type of each column using .info() for e.g. your_dataframe.info()
# 3. Drop columns with no values
# 4. Convert the column "Current" to numeric (see "cleaning data" section week 5 lesson)
# 5. Drop any row containing NaN -- use the option how='any' rather than how='all' (see 'cleaning data" section week 5 lesson)
# 6. Replace the column "Current" with its absolute value (np.abs())
# 7. Plot the Potential on the x-axis and Current on the y-axis.  Label your axes.  Set your yscale to log.  e.g. plt.yscale('log')
# 8. Replot the previous using the axis scale:  [-1.5,-0.7,1e-8,2e-5]
# 9. Replot the previous on a linear scale with the axis: [-1.08,-1,0,1e-6]
# 10. Take all data with a potential between -1.06 and -1.035 and fit to a line. 
# 11.  Replot #9 and include your fit. 
# 12.  Based on your fit, determine the potential where the current is zero.  
# 13.  Subtract the potential found in #12 from your potential data and replot #8.  You will have to adjust your x axis scale since you just shifted your data.  
# 
# You should get a plot that looks like:  
# 
# ![image.png](attachment:image.png)

# **Week 6:**<hr style="height: 3.0px"/>  

# 1. Read in the data file: week 6 data.xlsx
# 2. Check the type of each column using .info() 
# 3. Drop columns with no values ("all" dropna) - make sure you use the correct axis
# 4. Convert columns to numeric 
# 5. Drop any row containing NaN ("any" dropna) - make sure you use the correct axis
# 6. Add a new column "time, hrs" by converting "time, sec" to hours
# 7. Plot the time in hours on the x-axis and crystallization fraction on the y-axis.  Label your axes.  
# 8. Fit your data (time in hours, crystallization fraction) to the following function:  $y=1-e^{-k \ t^n}$
# 9. Replot your data (color black small points) and include your fit (color red line)
# 10. Using your fitted function, determine the crystallization fraction after 125 hours.  

# **Week 7:**<hr style="height: 3.0px"/>  

# **Problem 1:**  (a) Plot the data in the file "lesson 7 data bond energy.xlsx"  (b) Find the best fit to the data using the function:  $$ E = -\frac{A}{r}+\frac{B}{r^{\ n}}$$ and add this to your plot. For this equation, the Bond Energy is in eV and the atom separation, r, is in nm.  (c) Add a horizontal and vertical line to your plot at the value of the bond energy, $E_0$, and equilibrium atom spacing, $r_0$, respectively.  You don't need to calculate the $(r_0, E_0)$ point. It is sufficient to find this point through trial and error moving your vertical and horizontal lines.  

# **Problem 2:** (a) The longitudinal modulus of elasticity of a tubular shaft measured in bending is given by: $$E = \frac{4 F L^3}{3 \pi \Delta y\ (d_0^4-d_i^4)}$$ where F is the applied load (1000 N), L is the distance between support points in the 3-point bend test (1.0 m), $\Delta y$ is the deflection at the half-way point (0.35 mm), $d_0$ is the outer diameter (70 mm) and $d_i$ is the inner diameter (50 mm). Calculate the longitudinal modulus of elasticity and print this result includding units.    
# (b) For the same setup as above if the modulus is 200 GPa, plot the deflection, $\Delta y$, as a function of the inner diameter where $20 mm \leq d_i \leq 60 mm$.  Make sure you label your axes.  Use small blue points.  

# **Problem 3:**   Read the data file: Concrete_Data_Yeh.csv
# 
# 1.  Find the density of each concrete sample by adding together the data: cement, slag, flyash, water, superplasticizer, courseaggregate, and fineaggregate.  
# 2.  Plot the compressive strength (y-axis) vs age (x-axis) for the concrete samples that have a density between 2450 and 2452.5.  Label your axes and use green triangle markers.  

# **Week 8:**<hr style="height: 3.0px"/>  

# **Problem 1**

# Plot the measured thickness 'Measure' vs the extruder temperature 'ExtrTemp' for 
# 1. Alexandria  as black small filled circles 'ko'
# 2. Cairo  as green small points 'g.'  
# 
# for:  55.0 < LineSpeed < 55.05 and 26.83 < WaterTemp < 26.9

# **Problem 2**

# Plot the measured thickness 'Measure' vs the water temperature 'WaterTemp' for 
# 1. Alexandria  as blue small points 'b.'
# 2. Cairo  as red small points 'r.'  
# 
# for:  55.0 < LineSpeed < 55.05 and 234.85 < ExtrTemp < 234.9

# **Problem 3**

# Plot the measured thickness 'Measure' vs the date 'Date' for
# 
# Alexandria as blue small points 'b.'
# Cairo as red small points 'r.'
# for:  
# 
# >    55.0 < LineSpeed < 55.05 and  
# >    234.85 < ExtrTemp < 234.9 and  
# >    26.83 < WaterTemp < 26.9
# 

# **Problem  4**

# Break up the data "Measure" into 20 groups based upon its value, i.e each group will have a size = ((max of Measure)-(min of Measure))/20.  For each group find the average of the "Measure" and average of the corresponding "LineSpeed".  You should have 20 pairs of points when you are done: (Measure, Linespeed).  Plot these values with Linespeed on the y-axis.  

# There are many ways to think about doing this.  You could create another column in your dataframe called "group" and assign a group number from 1 to 20 for everypoint in your dataframe based on the value of "Measure".  Then you could use a groupby('group').mean() to find the mean of all points in each group.  
# 
# You could find all records within a given range of "Measure" values, find the mean of this group and append the value to an array.  Then iterate through all the ranges for a for loop.  
# 
# You could make a new column of data in your dataframe with values equal to pd.cut(df['Measure'],20), then consider what groupby could do...  
# 
# ... and many other options.
# 
# 

# **Week 9:**<hr style="height: 3.0px"/>  

# Read through the 2 lesson files for this week: ```week 9 pandas groupby.ipynb``` and week ```9b plotting data after using groupby.ipynb```

# There are many questions on data frames so I'm going to look at that for this week first.
# 
# First please watch the following in order (the longest video is only 7.5 minutes):
# 
# https://www.linkedin.com/learning/python-data-analysis-2/pandas-overview?u=57888345 (Links to an external site.)
# 
# https://www.linkedin.com/learning/python-data-analysis-2/dataframes-and-series?u=57888345 (Links to an external site.)
# 
# https://www.linkedin.com/learning/python-data-analysis-2/indexing-in-pandas?u=57888345 (Links to an external site.)
# 
# https://www.linkedin.com/learning/python-data-analysis-2/plotting?u=57888345 (Links to an external site.)
# 
# This entire course is very good if you want to start from the beginning.

# This week you have a choice between two datasets:
# * dataset on homicides in the United States, or
# * dataset on domestic flights in the United States

# If you choose the homicide dataset:  
# * Take a slice of the original dataset to inlcude only columns: 'State', 'Year', and 'Perpetrator Sex'
# * Using conditionals as in the last assignment, find the total number of homicides in a state of your choice for the year 2000
# * Find the total number of homicides for the state of your choice for each year from 1980 to 2014.  (If you first limit your dataset to the state of your choice using conditionals, groupby can then quickly give you homicides for each year)
# * Plot the number of homicides vs year for your chosen state
# * Find the total number of homicides for the entire US for each year
# * Find the total number of homicides for the 1980 to 2014 period for each state

# If you choose the domestic travel dataset: 
# * First to load this dataset use:  ``` pd.read_csv('domestic flight database.tsv', sep='\t', header=None)```
# * Take a slice of the original dataset to include only columns: 'origin city', 'destination city', 'passengers', 'date'
# * Using conditionals as in the last assignment, find the total number of passengers from an origin city of your choice for the year 2000 (200001 to 200012)
# * Find the total number of passengers for the origin city of your choice for each month from 1990 to 2009.  (If you first limit your dataset to the origin city of your choice using conditionals, groupby can then quickly give you passengers for each date which are already per month)
# * Plot the number of passengers vs date for your chosen origin city
# * Find the total number of passengers for the entire US for each month
# * Find the total number of passengers for the 1990 to 2009 period for each origin city

# **Week 10:**
# <hr style="height: 2.0px"/> 

# The above data shows the total number of households in each county of each state and a breakdown of the number of households that have an income in one of the indicated ranges.   
# 
# For example, 2931 households have an income between 75,000 and 100,000 in Autauga County, Alabama.  This represents 2931/21397*100 = 13.7% of all households in Autauga County.    
# 
# 

# <hr style="height: 1.0px"/>   
# 
# **First,** you need to fix the data set to remove duplicates using ```drop_duplicates()```.  Instead of 4930 rows you should get 3142 records.  
# 
# **Determine the following**: 
# 1. The number of households that have an income greater than 100,000 for each county across the USA.  Add this data to the dataframe.  
# 2. The percentage of households for each income range for each county, i.e. divide the data for each row by "households" and multiply by 100.  
#     
# **Create three plots**:
# 1.  The percentage of households with an income less than 50,000 and the percentage of households with an income greater than 100,000 for every state in the US.  
# 2.  The same data but now for every county in Virginia.  
# 3.  A bar chart for the same data but now for Montgomery County, Virginia.  
# 
# The three plots should be laid out similar to the figure below where each plot is the same height but plot 1 has a width of 3, plot 2 has a width of 2 and plot 3 has a width of 1. 
# ![image.png](attachment:image.png)
# 

# **Week 11:**<hr style="height: 3.0px"/>
# 
# 
# **Problem Statement:** 
# 
# (1) For cubic single crystals, the modulus of elasticity in a general $\text{[uvw]}$ direction is given by:  $$\frac{1}{E_{uvw}} = \frac{1}{E_{\text{[100]}}}- 3 \left( \frac{1}{E_{\text{[100]}}}- \frac{1}{E_{\text{[111]}}} \right) \left( \alpha^2 \beta^2 + \beta^2 \gamma^2 + \gamma^2 \alpha^2 \right)$$
# 
# where $\alpha = \frac{u}{\sqrt(u^2+v^2+w^2)}$,  $\beta = \frac{v}{\sqrt(u^2+v^2+w^2)}$, $\gamma = \frac{w}{\sqrt(u^2+v^2+w^2)}$
# 
# For copper, $E_{[100]}=66.7$ GPa and $E_{[111]}=191.1$ GPa.  Calculate the modulus in the $\text{[110]}$ direction and compare to the expected value of 130.3 GPa.  
# 
# (2) Pick 100 random directions, $\text{[uv0]}$ and calculate the elastic modulus, $E_{\text{[uv0]}}$.  
# * Pick u and v randomly with a value between 0 and 1.  
# * Now normalize u and v by dividing both by $\sqrt(u^2+v^2)$
# * Next find the corresponding elastic modulus in the direction [uv0].  
# * Multiply your normalized point $\frac{\text{(u,v)}}{\sqrt{u^2+v^2}}$ by the modulus in that direction i.e.   $$E_{\text{[uv0]}} \times \frac{\text{(u,v)}}{\sqrt{u^2+v^2}}$$. 
# * Plot these points.   
# 
# (3) Now let's pretty up the plot. Reproduce the following with your data: 
# $$ $$
# ![image.png](attachment:image.png)
# 
# **Practice**
# 
# (P1) Write a function to calculate the number of defects per cubic meter in a pure metal (e.g. vacancies) given the temperature, the energy required to form the defect, the density, and the atomic weight. Check your function for copper at 1000 $^{\circ} C$.  The energy of defect formation is 0.9 eV/atom, that atomic weight and density at 1000 $^{\circ}C$ are 63.5 g/mol and 8.4 $g/cm^{3}$ respectively.  The answer is $2.2 \times 10^{25}$ vacancies/$m^3$.  (Callister 10th ed. Chap 4)
# 
# 

# **Week 12:**<hr style="height: 3.0px"/>
# 
# 
# **Problem Statement:** 

# If you think your grade needs help, then take a few problems from a class your finishing up (or makeup some problems) and use python to work out the problems.  Make sure to include at least one plot with every problem (labeling axes, etc).  You can also use one of our datasets and analyze it in a different way, etc.  

# In[ ]:





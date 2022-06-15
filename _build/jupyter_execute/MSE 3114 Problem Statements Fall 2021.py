#!/usr/bin/env python
# coding: utf-8

# # MSE 3114 Math Methods II (Fall 2021)

# >Remember the notebook pdf printout that you turn in needs to be clean and free from any unnecessary code.  The extra code is great when you are working through the problems and necessary if you are asking me for help prior to the due date but then you need to clean it up once you get everything working. 

# **Homework due every Thursday by 11:59 pm**

# ## Applications & Exercises

# **Week 1:**Due Thursday August 26, 2021 by 11:59 pm
# <hr style="height: 3.0px"/>
# 
# Learning objectives:
# * Be able to reinstall Anaconda
# * Be able to import data from an Excel file
# * Be able to import your own modules and functions using *.py file into a Jupyter notebook
# 
# 
# Prereq: 
# *  [Setup your linked-in learning account](https://canvas.vt.edu/courses/107699/pages/getting-started-with-course?module_item_id=768560)
# *  [Getting Started with Python](https://www.linkedin.com/learning/python-quick-start)
# 
# Open a new Jupyter notebook and answer the questions below.  If a question below only requires a text response, just use a "markup" cell.  Include the problem statements in your notebook. Use the assignments link in Canvas to upload a pdf version of your notebook.  
# 
# *Remember the notebook printout that you turn in needs to be clean and free from any unnecessary code.  The extra code is great when you are working through the problems but then you need to clean it up once you get everything working.* 
# 
# <hr style="height:2px;background-color:gray;width:100%">
# 
# **1.** Open a new notebook. Import the data from **Al7075_out.xlsx** and plot the stress vs strain curve.  Make sure you label your axes.  Plot your points as blue triangles.
# 
# <hr style="height:2px;background-color:gray;width:100%">
# 
# **2.** Write a function that uses the metric tensor to find the angle $\theta$ in degrees between 3 atoms as shown for example below.  Your function should allow you to enter the fractional coordinates of the three atoms, [x1,y1,z1], [x2,y2,z2], and [x3,y3,z3], and the lattice parameters, a,b,c,alpha,beta,gamma.  You can use the numbers below to test your code.  The Oxygen - $Si_1$ bond length will be 1.60674 $\mathring{A}$ and the Oxygen - $Si_2$ bond length will be 1.61035 $\mathring{A}$.  
# 
# ![image.png](attachment:image.png)
# 
# The vector, $\overline{v1}$, connecting the $Si_2$ and O atoms is given by $\overline{v1}=Si_2 - O = \left[x2,y2,z2\right]-\left[x1,y1,z1\right]$
# 
# The magnitude of this vector (i.e. the bond length) is given by $\mid\overline{v1}\mid=\sqrt{\overline{v1}\cdot \overline{\overline{g}} \cdot\overline{v1}}$ or in matrix format:  
# 
# $$\mid\overline{v1}\mid=\sqrt{\begin{bmatrix}x2-x1 & y2-y1 & z2-z1 \end{bmatrix}\cdot\begin{bmatrix}g11&g12&g13\\g21&g22&g23\\g31&g32&g33 \end{bmatrix}\cdot\begin{bmatrix}x2-x1 \\ y2-y1 \\ z2-z1 \end{bmatrix}}$$
# 
# Now the cosine of the angle between the $Si_2$ - O - $Si_1$ atoms would be given by:
# 
# $$\cos{\theta}=\frac{\overline{v1}\cdot \overline{\overline{g}} \cdot \overline{v2}}{\mid\overline{v1}\mid\ \mid\overline{v2}\mid}$$
# where $\overline{v2}=Si_1 - O$
# 
# When performing your dot products of $\overline{v2}$, $\overline{\overline{g}}$, and $\overline{v1}$, you can use either of the two formats below.  
# 
# ```python 
#     np.dot(np.dot(A, B), C)
#     np.linalg.multi_dot([A,B,C])
# ```
# 
# <hr style="height:2px;background-color:gray;width:100%">
# 
# **3.**  Making sure that all needed import statements are included, copy your function into a text file named my_func.py.  Then import this file into a blank notebook and run the function to show it works.  
# 
# <hr style="height:2px;background-color:gray;width:100%">
# 

# **Week 2:** Due Thursday Sept 2 11:59pm
# 
# For homework, create your own survey in Google forms that will allow you to rank at least 5 features /items by collecting opinion data on 5 corresponding survey questions and have at least 10 people take it.  The more data you have the better if you can get more than 10.  Send it to family, friends, etc.  The 5 questions should use the same scale so that you will be able to compare.  Use the 5-point likert scale.  
# 
# Download your survey responses and find the mean, std, median, max and min values for each column.  Analyze your survey data by creating at least 3 different plots/charts summarizing aspects of your data.  Perform a t-test to see if the mean values of your survey questions are significantly different from each another.  
# 
# At least one of your plots/charts should be something that I did not do in the lesson.  
# 
# video lesson: https://www.youtube.com/watch?v=VcZCPBZZvtc&list=PL66uKvacDNIfFjQR8mu4M-dv_gQphK5qg&index=4 

# **Week 3: Due Thursday Sept 9 11:59pm** 
# <hr style="height: 3.0px"/>
# 
# video lesson:  
# >1. https://www.youtube.com/watch?v=UzZn_9c89LI&list=PL66uKvacDNIfFjQR8mu4M-dv_gQphK5qg&index=6 
# >2. https://www.youtube.com/watch?v=pycy8yNuiZw&list=PL66uKvacDNIfFjQR8mu4M-dv_gQphK5qg&index=5 (watch only to 15:13)  
# 
# Use the data from the titanic (provided), to create 6 plots in the following layout: 
# 
# ![image.png](attachment:image.png)
# 
# Plot 1: Scatter plot of 'number of people on board'(y) vs 'Age of person'(x).  
# Plot 2: Histogram of the Age of people on board.  
# Plot 3 - 5:  Your Choice.  
# Plot 6: Pie chart of the number of females in 1st, 2nd and 3rd class that died.  
# 
# 
# ```python
# raw=pd.read_csv('titanic.csv')
# raw.head()
# ```

# **Week 4: Due Thursday Sept 16 11:59pm**
# <hr style="height: 3.0px"/>
# 
# **Problem 1:**  Reproduce the shapes found in the image file "week 4 shapes.png". 
# 1. Each shape outline should be colored as in the image file.
# 2. Reduce your point size by plotting "." rather than "o" for the point type.
# 3. Add labels to the x & y axes e.g. "x-pixel coordinate", "y-pixel coordinate" 
# 4. Set your x & y min,max values to correspond to the original image file dimensions.  You might have to look back to 2114 for this step.  
# 

# **Week 5: Due Thursday Sept 23 11:59pm**
# <hr style="height: 3.0px"/>
# 
# **Problem 1:**  Reproduce the scatter plot from image file "crystallization kinetics poly testing 48 2015 p 125.png" with the following requirements: 
# 1. You need to include at least 3 of the data sets (three different temperatures)
# 2. Each data set (temperature) should be in a different color
# 3. Add labels to the x & y axes.  
# 4. Set your x & y min,max values to correspond to the image plot 
# 
# **Problem 2:** Replot your data from problem 1 where the y-axis is log(−𝑙𝑛(1−𝑋𝑡)) and the x-axis is log(t).  Plot this in two different ways.  (1) Your fist plot should be −𝑙𝑛(1−𝑋𝑡) vs t on a log-log plot and your (2) second plot should be (log(t), log(−𝑙𝑛(1−𝑋𝑡))) on a linear-linear plot (i.e. a simple scatter plot).  Be careful here with the log and ln functions.  The default np.log() function is actually base e.  
# 1. Remember Xt corresponds to the fraction of crystallinity, i.e. 60% corresponds to Xt=0.6
# 2. label your axes
# 3. plot all 3 data sets from problem 1

# **Week 6: Due Thursday Sept 30 11:59pm**
# <hr style="height: 3.0px"/>
# 
# **Problem 1:** Let's see how well our method does on an image that is skewed and rotated.  Let's say your just really bad at making a photocopy.  Reproduce the plot below.  Label your axes. 
# 
# ![image-2.png](attachment:image-2.png)
# 
# 
# **Problem 2:** How can we handle log-linear plots?  Our transformation is only a linear transformation.  Hint:  Don't use a log axis on the y-axis but transform your data first. So for example, calibration point (1.70, $10^{-13}$) should be taken as (1.70, -13).  
# 
# Reproduce the plot below.  Use separate data sets for the two different types of points. Label your axes.   
# ![image-3.png](attachment:image-3.png)
# 
# Fig caption: Diffusion coefficients measured directly (open circles) and calculated from the electical conductivity data (closed circles) for $(Na)^+$ in sodium chloride. At the break in the curves between the two regimes, the concentration of intrinsic vacancies equals that due to the extrinsic dopant. From "Physical Ceramics", Chiang, Birnie, and Kingery, John Wiley & Sons (1997), pg 202.
# 
# **Problem 3:** Reproduce the points shown in the plot below. The glass transition temperature corresponds to the inflection point on the curve.  This point is the point of maximum slope.  To determine the glass transition temperature take the derivative of your data and find the point of maximum derivative.  
# 
# Hints: The slope is simply the difference in the y-values of two neighboring points divided by the difference in the x-values.  You might take a look at numpy.diff().  
# 
# Note: Don't forget that since you are taking the difference between two neighboring points, your x-axis for each point has shifted to a value that is the average of the two.  This is called a moving average.  You may have to write a short function to take care of this.  
# 
# Your new slope data and your new x data will both have a length one less than the original data set.  
# What you need to show:  
# (a) plot of data in figure below  
# (b) plot of the derivative of this data versus temperature  
# (c) identify the glass transition temperature as the maximum in the curve    
# 
# ![image-4.png](attachment:image-4.png)
# 
# MDSC plot of polystyrene measuring the glass transition as changes in heat capacity as a function of temperature using either a heating or cooling rate as indicated by the solid lines. The dotted line indicates a quasi-isothermal measurement of the glass transition of polystyrene. Adapted from L. C. Thomas, A. Boller, I. Okazaki, and B. Wunderlich, Thermochim. Acta, 1997, 291, 85.

# **Weeks 7-9: Homework is embedded throughout lesson files**  
# <hr style="height: 3.0px"/>
# 
# The next couple of lessons (weeks 7-9) we will look at several different types and ways of fitting. All lessons will pull data from the literature using the digitizing functions (`selectdata()`, `cal()`) we created in the last couple of lessons.  
# 1. **Week 7**:  `Scipy curve_fit()`  (*Due Thursday Oct 07 11:59pm*)  
# 
#     a. Application: Crystallization Kinetics of Amorphous $TiO_2$.  (Thin Solid Films 519 (2010) 1649-1654)  
#     b. Single Peak Fitting of XRD data  
#     c. Integration under a curve  
#     d. Fitting Transformation vs Time data to the Avrami Equation (You saw the Avrami equation in Chapter 10 of Callister)  
#     
#     
# 2. **Week 8**: new package: `lmfit` https://lmfit.github.io/lmfit-py/  (*Due Thursday Oct 28 11:59pm*)  
# 
#     a. We will first learn to install a new package to our Python installation  
#     b. Application: Cystallization Kinetics of an ionic liquid (Royal Society of Chemistry Advances (RSC Adv.), 2014, vol. 4, p. 22277)  
#     c. Fitting (deconvolution) of two overlapping peaks in calorimetry data  
#     
#     
# 3. **Week 9**:  `Scipy optimize()`    (*Due Thursday Nov 4 11:59pm*)  
# 
#     a. Application:  Creep Analysis of an S590 superalloy Fe-Co-Cr-Ni  
#     b. Creating Larsen-Miller Plot from Creep Data (stress vs rupture time) at various temperatures  
#     c. Interesting problem because instead of a typical fitting problem, here we are manipulating the set of temperature data curves with a fitting parameter that when found will collapse all the curves to one master curve (the Larsen-Miller plot).  

# 

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

Suggested video lessons:

Why use numpy arrays (7 min):  https://www.linkedin.com/learning/numpy-data-science-essential-training/create-arrays-from-python-structures?u=57888345

Array creation (7 min): https://www.linkedin.com/learning/numpy-data-science-essential-training/intrinsic-creation-using-numpy-methods?u=57888345

linspace(), zeros(), ones() and numpy data types (9 min):  https://www.linkedin.com/learning/numpy-data-science-essential-training/linspace-zeros-ones-data-types?u=57888345



## Anisotropy of thermal expansion coefficient


Let's take a look at the anisotropy of thermal expansion in a crystal of zinc. We will take the z-axis to be perpendicular to the close-packed planes.  In the x-y plane, the thermal expansion is isotropic but in the x-z or y-z plane zinc is highly anisotropic.  The thermal expansion in a [uvw] direction can be found from: $$\alpha_{uvw} = \alpha_x\times(n_x^2+n_y^2)+\alpha_z\times n_z^2$$ where $n_x, n_y, n_z$ are the x,y,z components of the unit vector $\frac{[u v w]}{\sqrt{u^2+v^2+w^2}}$ i.e. $$(n_x, n_y, n_z)=\frac{(u,v,w)}{\sqrt{u^2+v^2+w^2}}$$. 



```python
import numpy as np
import matplotlib.pyplot as plt
```

### Let's look at an example for zinc
For zinc $\alpha_{x}=14\times 10^{-6} \ \ {^\circ C}^{-1}$ and $\alpha_{z}=55\times 10^{-6} \ \ {^\circ} C^{-1}$


First let's write a function to find the unit vector in the direction of u,v,w

```python
def unitvec(u,v,w):
    mag=np.sqrt(u**2+v**2+w**2)
    return [u,v,w]/mag
```

```python
# let's test some values for our function unitvec()
print(unitvec(1,0,0))
print(unitvec(1,1,0))
print(unitvec(1,1,1))
```

```python
# What would the values of nx, ny, and nz be for a [uvw] direction = [120]
print(f'unit vector in direction [012] is: {unitvec(0,1,2)}')
print(f'therefore nx is just the first value = {unitvec(0,1,2)[0]}')
print(f'ny the second = {unitvec(0,1,2)[1]}')
print(f'and nz the third = {unitvec(0,1,2)[2]}')
```

Substituting into the following (with $\alpha_x = 14$ and $\alpha_z=55$)
$$\alpha_{uvw} = \alpha_x\times(n_x^2+n_y^2)+\alpha_z\times n_z^2$$
gives the thermal expansion in the [012] direction

```python
# alpha_x*(nx**2+ny**2)+alpha_z*nz**2
14*(0**2+0.4472136**2)+55*0.89442719**2  #in units 10^-6 C^-1
```

```python
# write a def to find alpha
def alpha(nx,ny,nz,ax,az):
    return ax*(nx**2+ny**2)+az*nz**2
```

```python
# let's find alpha in a couple of additional directions
#first let's confirm our answer above [012] that we did above
uvw012=unitvec(0,1,2)
alpha(uvw012[0],uvw012[1],uvw012[2], 14, 55)
```

```python
# let's look at directions [[0,1,2], [0,0,1], [0,1,0], [0,1,1]]
#in your problem you would find these using random number and 
#in your problem the w values are all zero rather than the u values as below
ulist=np.array([0,0,0,0]) 
vlist=np.array([1,0,1,1])
wlist=np.array([2,1,0,1])
#unitvectors
u_unit=unitvec(ulist,vlist,wlist)[0]
v_unit=unitvec(ulist,vlist,wlist)[1]
w_unit=unitvec(ulist,vlist,wlist)[2]
#corresponding expansion coeff.
alphalist= alpha(u_unit,v_unit,w_unit, 14, 55)
print(alphalist)
```

```python
# here we take unit vector components v & w and scale by alpha
xdata=alphalist*v_unit 
ydata=alphalist*w_unit
# plot direction (v_unit,w_unit)*alphalist
plt.plot(xdata, ydata, 'ro')
plt.axes().set_aspect('equal')
plt.show()
```

>If you imagine a vector from (0,0) to any point in the figure above. The length of that vector is equal to the thermal expansion coefficient in that direction.  


There are many ways to improve the visual appeal of our plot.  

```python
# main plot of xdata, ydata defined previously
plt.plot(xdata, ydata, 'bo') # 'bo' means blue point
plt.axes().set_aspect('equal')  # aspect ratio set equal so that scales on x and y are equal

# comment out the line below when you don't know the axes limits
plt.axis([0,30,0,60]) # setting plot axes [xmin, xmax, ymin, ymax]

# add title and label axes
plt.title('Thermal expansion coeff')
plt.xlabel(r'$10^{-6}\ ^\circ C^{-1}$', fontsize=14) 
plt.ylabel(r'$10^{-6}\ ^\circ C^{-1}$', fontsize=14)

# add arrows (xstart, ystart, change in x, change in y)
# arrow(startx,starty,length_in_x, length_in_y)
plt.arrow(0,0,34.5*unitvec(0,1,1)[1], 34.5*unitvec(0,1,1)[2], length_includes_head=True,width=0.5,head_length=4, head_width=3)

# add text xy=[xcoord,ycoord] use plot axis values to place text
plt.annotate('[011]',xy=[17,27])

# put it all together
plt.show()
```

Practice problem P1:  your on your own!

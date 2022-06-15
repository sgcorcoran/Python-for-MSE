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

1. Open a new notebook. Import the data from Al7075_out.xlsx and plot the stress vs strain curve. Make sure you label your axes. Plot your points as blue triangles.

```python
import pandas as pd

import matplotlib.pyplot as plt
```

```python
raw=pd.read_excel('Al7075_out.xlsx')
raw.head()
```

```python
plt.plot(raw['strain'],raw['stress MPa'],'^b')
plt.xlabel('strain')
plt.ylabel('stress, MPa')
plt.show()
```

## Lesson 1 Homework Problem 2


**2.** Write a function that uses the metric tensor to find the angle $\theta$ in degrees between 3 atoms as shown for example below.  Your function should allow you to enter the fractional coordinates of the three atoms, [x1,y1,z1], [x2,y2,z2], and [x3,y3,z3], and the lattice parameters, a,b,c,alpha,beta,gamma.  You can use the numbers below to test your code.  The Oxygen - $Si_1$ bond length will be 1.60674 $\mathring{A}$ and the Oxygen - $Si_2$ bond length will be 1.61035 $\mathring{A}$.  

![image.png](attachment:image.png)



```python
import numpy as np
```

```python
# atom1, atom2 and atom3 are taken as lists [x,y,z]
# atom2 is the vertex of the angle
def angle(atom1, atom2, atom3,a,b,c,alpha, beta, gamma):
    alpha=np.deg2rad(alpha)
    beta=np.deg2rad(beta)
    gamma=np.deg2rad(gamma)
    g=np.array([
    [a*a, a*b*np.cos(gamma), a*c*np.cos(beta)],
    [b*a*np.cos(gamma), b*b, b*c*np.cos(alpha)], 
    [c*a*np.cos(beta),c*b*np.cos(alpha),c*c]
    ])
    atom1=np.array(atom1)
    atom2=np.array(atom2)
    atom3=np.array(atom3)
    v1=atom1-atom2
    v2=atom3-atom2
    v1mag=np.sqrt(np.dot(v1,np.dot(g,v1)))
    v2mag=np.sqrt(np.dot(v2,np.dot(g,v2)))
    temp=np.dot(v1,np.dot(g,v2))
    cos_ang=(temp)/v1mag/v2mag
    ang_degrees=np.rad2deg(np.arccos(cos_ang))
    return(ang_degrees)
   
```

```python
angle([0.4699,0,0],[0.4141,0.2681,0.1188],[0.5301, 0.5301,0.3333], 4.91, 4.91, 5.41, 90,90,120)
```

<!-- #region -->
It works.  So I just need to copy the following code in notepad++ and save as a *.py file.  


```python

import numpy as np

def angle(atom1, atom2, atom3,a,b,c,alpha, beta, gamma):
    alpha=np.deg2rad(alpha)
    beta=np.deg2rad(beta)
    gamma=np.deg2rad(gamma)
    g=np.array([
    [a*a, a*b*np.cos(gamma), a*c*np.cos(beta)],
    [b*a*np.cos(gamma), b*b, b*c*np.cos(alpha)], 
    [c*a*np.cos(beta),c*b*np.cos(alpha),c*c]
    ])
    atom1=np.array(atom1)
    atom2=np.array(atom2)
    atom3=np.array(atom3)
    v1=atom1-atom2
    v2=atom3-atom2
    v1mag=np.sqrt(np.dot(v1,np.dot(g,v1)))
    v2mag=np.sqrt(np.dot(v2,np.dot(g,v2)))
    temp=np.dot(v1,np.dot(g,v2))
    cos_ang=(temp)/v1mag/v2mag
    ang_degrees=np.rad2deg(np.arccos(cos_ang))
    return(ang_degrees)

<!-- #endregion -->

```python

```

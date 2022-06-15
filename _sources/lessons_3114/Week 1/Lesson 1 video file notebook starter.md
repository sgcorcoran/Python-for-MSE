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

## Creating your own functions for import


### Our example comes from crystallography and will require some matrix manipulation so let's 
#### 1. take a refresher on matrices
#### 2. look at creating and testing a function
#### 3. copy function to a text file *.py for import


When dealing with matrices, you will want to use the numpy.linalg module. You can read the documentation here: https://numpy.org/doc/stable/reference/routines.linalg.html

```python
import numpy as np  #the linalg module would then be np.linalg
```

#### defining a matrix as a numpy array

```python

```

#### multiplying matrices np.dot()

```python

```

#### example:  gmatrix used in crystallography

| | |
|-|-|
|![image-2.png](attachment:image-2.png)  |$$ g=\begin{bmatrix}a^{2} & ab \cos{(\gamma)}&ac \cos (\beta) \\ab \cos(\gamma) & b^2 & bc \cos (\alpha) \\ ac  \cos(\beta) & bc \cos(\alpha)&c^2 \end{bmatrix}$$|



#### simple case: gmatrix for white tin (tetragonal)
a = b = 0.583 nm
c = 0.318 nm
$\alpha = \beta = \gamma = 90^{\circ}$

```python

```

#### Volume of the unit cell for Tin = sqrt of determinant of $g$

```python

```

```python

```

#### Gmatrix for any a, b, c, $\alpha, \beta, \gamma$

```python

```

```python

```

#### Write the function & test

```python

```

```python

```

#### Put it all in one cell, test again after restarting Kernel, copy to text file *.py

```python

```

```python

```

Now go an import your .py file in another notebook and see if it works!

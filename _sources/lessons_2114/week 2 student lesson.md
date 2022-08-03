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

**Week 2:**  Student lesson
<hr style="height: 3.0px"/>

Prereq: Week 2 Exercises require us to know how to:
* comment notebooks using Markdown cells 
* formatting equations in markdown cells
* use `print()` statement with an **f-string** for better presentation of your final answer
* use `numpy` extension for `np.sqrt()` and `np.exp()`
* use `scipy.special` extension for `special.erf()`


<!-- #region heading_collapsed=true -->
### markdown cells
<!-- #endregion -->

<!-- #region hidden=true -->
If you double click in any markdown cell (**for example this cell**), you can see the code I wrote to use various formatting or special characters:   

**bold text**, *italic text*, `highlighted text`

or python formatted text: 
```python
print('some text')
```
$\mu$

when done editing a markdown cell just press shift-enter as you would for code cells.  
<!-- #endregion -->

<!-- #region hidden=true -->
If you didn't do it, you should have double clicked above to see the coding.  Then, press shift-enter in the cell when you are done.  
<!-- #endregion -->

<!-- #region heading_collapsed=true -->
### equation formatting in markdown cells
<!-- #endregion -->

<!-- #region hidden=true -->
Now equations require special formatting.  Here are some examples (***remember to double click in this cell to see the coding***):  

* subscript:  $x_2 = \mu \times \sigma$  
* superscript: $x^3$ 
* fraction:  $\frac{3 x}{2}$

Equations start and end with a dollar sign.  Between the dollar sign is LaTeX code which we will talk about more below.  
<!-- #endregion -->

<!-- #region hidden=true -->
>If we were to try `$10^23$`, we would get $10^23$.  We need to use `{23}`.  If `{}` are missing, it is assumed that only 1 character is being superscripted.  
>
>proper formatting:  `$10^{23}$` gives  $10^{23}$
<!-- #endregion -->

<!-- #region hidden=true -->
>This notation is **only** for markdown cells.  Do not use it in code cells or you will get errors.  For example, we can format avagadro's number in a "Markdown" cell as: `$6.02\times10^{23}$` which gives $6.02\times10^{23}$ but in a "Code" cell we would write `6.02*10**23`
<!-- #endregion -->

<!-- #region hidden=true -->
The notation used between the dollar signs is LaTeX so you can go online and use a LaTeX editor to create an equation and paste the results here.  For example, a quick search gives me http://www.hostmath.com/. Here you can click on equation templates and it gives you the LaTeX code.  Just remember to paste it between `$$`.  

`$\int_{a}^{b} \frac{\sqrt[4]{a x}}{x} \text{ d}x$` : 
$\int_{a}^{b} \frac{\sqrt[4]{a x}}{x} \text{ d}x$

use double dollar signs `$$ $$` if you want your equation on it's own line and centered: $$\int_{a}^{b} \frac{\sqrt[4]{a x}}{x} \text{ d}x$$
<!-- #endregion -->

<!-- #region hidden=true -->
double click to see the code for the following: 
$$\begin{cases}a & x = 0\\b & x > 0\end{cases}$$

$$\begin{bmatrix}a & b \\c & d \end{bmatrix}$$
$\color{red}{\sum_a^b}$,  $\overline{ab}$,  $\overrightarrow{ab}$, $\alpha$, $\Delta$, $\delta$
<!-- #endregion -->

<!-- #region heading_collapsed=true -->
### Example Problem: Let's calculate the number of atoms in a cubic meter of a bcc material given the atomic radius of 0.15 nm.  
<!-- #endregion -->

<!-- #region hidden=true -->
The volume of an bcc unit cell is given by $V_{cell}=\left(\frac{4 R}{\sqrt{3}} \right)^3$.  The bcc unit cell contains 2 atoms so we get the number of atoms per cubic meter as: 
$$\frac{2}{\left(\frac{4 R}{\sqrt{3}} \right)^3}$$
if R is given in meters.  
<!-- #endregion -->

```python hidden=true
import numpy as np
```

```python hidden=true
num_atoms_bcc=(2/(4*0.15*10**-9/np.sqrt(3))**3) # notice the double "**" for power
print(num_atoms_bcc)
print('or in nicer formatting:')
print(f'The number of atoms in the bcc unit cell is {num_atoms_bcc:0.2e} atoms/m^3')
```

### some additional help

<!-- #region -->
If you need to use functions such as the sqrt, exponential, sin, etc you will need to import numpy as 
```python
import numpy as np
```
We imported this previously so we don't need to repeat that here. 
<!-- #endregion -->

```python
np.exp(2)
```

```python
np.sqrt(144)
```

```python
#180 degrees = pi radians
np.cos(np.pi/4) #trig functions all expect radians not degrees
```

Some special functions such as the error function requires the special extension from the scipy library.  

```python
from scipy import special
```

```python
special.erf(0.5)
```

<!-- #region -->
You will need to write your own function again this week so check the examples from last week and the video lesson but below is the basic format and an example.  

```python
def function_name(variable_1, variable_2, etc):
    statement_1
    statement_2
    return variable #or print() statement
```
<!-- #endregion -->

```python
def atoms_per_bcc(atomic_radius): #atomic_radius in nm
    num_atoms_bcc=(2/(4*atomic_radius*10**-9/np.sqrt(3))**3)
    return num_atoms_bcc #atoms / m^3
```

```python
atoms_per_bcc(0.15)
```

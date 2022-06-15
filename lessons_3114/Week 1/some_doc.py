import numpy as np
import math

# enter angles in radians e.g. math.radians()
def gmatrix(a,b,c,α,β,γ):
    g=np.array([[a**2, a*b*np.cos(γ), a*c*np.cos(β)],
               [a*b*np.cos(γ), b**2, b*c*np.cos(α)],
                [a*c*np.cos(β),b*c*np.cos(α), c**2]
               ])
    return(g)
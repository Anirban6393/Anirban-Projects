import numpy as np
import math
from scipy.integrate import quad

def f(y, x):    
    """this is the rhs of the ODE to integrate"""
    if x>0 and y>0:
        return math.exp(-x-y)
    else:
        return 0

##For P(Y>X), integrate Y wrt infinity while setting value of x to inifinity as well
# We find the probability of integral sum being zero
x=np.inf
print(quad(f, 1, np.inf, args=(x))[0])
from sympy import *
import numpy as np
def f(x1,x2,x3):
    return x1**2 -2*x1*x2 + 2*x2**2 + x3**2 - x1*x3 + x1 + 3*x2 - x3

x1,x2,x3=symbols("x1 x2 x3")


d1 = diff(f(x1,x2,x3),x1)
d2 = diff(f(x1,x2,x3),x2)
d3 = diff(f(x1,x2,x3),x3)
print("[",d1,",",d2,",",d3,"]")

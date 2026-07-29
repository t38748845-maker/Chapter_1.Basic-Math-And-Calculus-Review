# derivative calculator in python...
def derivative_x(f, x, step_size):
    m = (f(x + step_size) - f(x)) / ((x + step_size) - x)
    return m
def my_function(x):
    return x**2
slope_at_2 = derivative_x(my_function, 2, 0.00001)
print(slope_at_2)

# calculating derivative in sympy...
from sympy import *
x = symbols('x')
f = x**2
dx_f = diff(f)
print(dx_f)

# derivative calculator in python... 
def f(x):
    return x**2
def dx_f(x):
    return 2*x
slope_at_2 = dx_f(2.0)
print(slope_at_2)

# using the substitution feature in sympy...
print(dx_f.subs(x, 2)) # this programme                                                can't runs on                                                     mobile thth wants                                            laptop...!#
# an integeral approximation in python... 
def approximate_integral(a, b, n, f):
    delta_x = (b - a) / n
    total_sum = 0
    
# apply range function...
    for i in range(1, n+1):
        midpoint = 0.5 * (2 * a + delta_x * (2 * i - 1))
        total_sum += f(midpoint)
        
# return total_sum * delta_x...
    return total_sum * delta_x
    
# define function...
def my_function(x):
    return x ** 2 + 1
    
# insert values...
area = approximate_integral(a = 0, b = 1, n = 5, f = my_function)

# print area...
print(area)

# another integral approximation in python...
area = approximate_integral(a = 0, b = 1, n = 1000, f = my_function)

# print area...
print(area)

# Yet another integral approximation in python...
area = approximate_integral(a = 0, b = 1, n = 1_000_000, f = my_function)

# print area...
print(area)

# using sympy to perform integration... 
from sympy import *

# declare x to sympy... 
x = symbols('x')

# use python syntax to declare code... 
f = x ** 2 + 1

# calculate the integeral of the function with respect to x... 
# for the area between x = 0 and 1
area = integrate(f, (x, 0, 1))

# print area... 
print(area)
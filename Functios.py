# Declaring a linear equation in python... 

def f(x):
    return 2 * x + 1
    
x_values = [1, 2, 3, 4]

for x in x_values:
    y = f(x)
    print(y)
    
# Charting a linear function in python using SymPy... 

from sympy import *

x = symbols('x')
f = 2 * x + 1
plot(f)

# Charting an exponential function...

from sympy import *

x = symbols('x')
f = x ** 2 + 1
plot(f)

# Declearing a function with two indepndent variablas in python...

from sympy import *
from sympy.plotting import plot3d

x, y = symbols('x y')
f = 2 * x + 3 * y
plot3d(f)
# calculating partial derivatives with sympy...
from sympy import *
from sympy.plotting import plot3d

# declare x and y to sympy...
x, y = symbols('x y')

# declearing the function...
f = 2*x**3 + 3*y**3
 
# calculate partial derivatives for x and y..
dx_f = diff(f, x) 
dy_f = diff(f, y)

# printing...
print(dx_f)
print(dy_f)

# plot the function...
plot3d(f)
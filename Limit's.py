# using sympy to calculate limits...
from sympy import *

x = symbols('x')
f = 1 / x
result = limit(f, x, oo)
print(result)

# displaying eular's number using sympy... 
from sympy import *
n = symbols('x')
f = (1 + (1 / n)) ** n
result = limit(f, n, oo)
print(result) # E
print(result.evalf())
# output; 2.71828182845905

# simple way to show eular's number...
import math
print(math.e)
# output; 2.718281828459045
# calculating compound interest in python

from math import exp

p = 100
r = .20
t = 2.0
n = 12

a = p * (1 + (r / n) ** (n * t))
print(a)

# calculating continuous interest in python...

from math import exp

p = 100
r = 0.20
t = 2.0

a = p * exp(r * t)
print(a)

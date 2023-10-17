from math import sqrt

pi = 1
piB = 0.5
eps = 1e-6
a = sqrt(0.5)
while abs((2/pi)-(2/piB)) > eps:
    piB = pi
    pi *= a
    a = sqrt(0.5+0.5*a)

pi = 2/pi
print(pi)
    
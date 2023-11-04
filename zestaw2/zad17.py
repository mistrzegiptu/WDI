from math import log

def f(x):
    print(x)
    return x**x - 2020

def df(x):
    return x**x * (1 + log(x))

x0 = 0
x1 = 10
eps = 1e-10

while abs(x1-x0) > eps:
    x0 = x1
    x1 = x1 - f(x1)/df(x1)
    
print(x1)
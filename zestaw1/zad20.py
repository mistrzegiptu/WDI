from math import sqrt

a = int(input())
b = int(input())

eps = 1e-6
while abs(a-b) > eps:
    a, b = sqrt(a*b), (a+b)/2

print(a)
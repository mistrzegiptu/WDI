s = float(input())

a = 1
b = 0
eps = 1e-10

while abs(a - b) > eps:
    b = a
    a = (s/b + b) / 2
print(a)
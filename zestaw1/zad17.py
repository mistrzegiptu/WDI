a = int(input())
b = int(input())

eps = 1e-6

while abs((a+b)/a - a/b) > eps:
    c = a
    a += b
    b = c
print(a/b)
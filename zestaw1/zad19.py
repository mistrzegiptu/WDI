def factorial(n):
    if n == 0:
        return 1
    i = n
    x = 1
    while i!=1:
        x *= i
        i -= 1
    return x
e = 0
e1 = 1
eps = 1e-6
i = 0
while abs(e-e1) > eps:
    e1 = e
    e += 1/factorial(i)
    i += 1

print(e)
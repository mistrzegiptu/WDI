#x^x = 2020

max = 10
min = 1
x = (min + max)/2
eps = 1e-10
while abs(max-min) > eps:
    if x**x > 2020:
        max = x
        x = (max+min)/2
    else:
        min = x
        x = (max+min)/2
print(x)
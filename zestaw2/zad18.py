a0 = 0
a = 1
b = 2
print(b)
n = int(input())

while n == a0:
    c = a
    a = a - b * a0
    a0 = c
    b = b + 2 * a0
    print(b)
    n = int(input())
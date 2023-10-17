n = int(input())

s = 0
a = 1
x = 0
while s <= n:
    s += a
    a += 2
    x += 1
print(x-1)
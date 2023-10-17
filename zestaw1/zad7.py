n = int(input())

a, b = 1, 1
while a*b <= n:
    if a*b==n:
        print(True)
        exit()
    c = a
    a += b
    b = c
print(False)
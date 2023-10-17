from math import isqrt
n = int(input())

i = isqrt(n)
if i*i==n:
    print(i, i)
    exit()
while i > 0:
    if n%i==0:
        print(i, n//i)
        exit()
    i-=1
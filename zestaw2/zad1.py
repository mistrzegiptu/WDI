def isFibonacci(n):
    a, b = 1, 1
    while b <= n:
        c = a
        a += b
        b = c
        if(b == n):
            return True
    return False
    
x = int(input())
d, e = 1, 1
while e <= x:
    if x % e == 0:
        if isFibonacci(x//e):
            print(True)
            exit()
    f = d
    d += e
    e = f

print(False)
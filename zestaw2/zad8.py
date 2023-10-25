def sumFib(n):
    if n == 1:
        return True
    a, b = 1, 1
    
    while b < n:
        a1 = b
        b1 = a - a1
        s = 0
        
        while b1 < n:
            s += b1
            if s == n:
                return True
            c1 = a1
            a1 += b1
            b1 = c1
        
        c = a
        a += b
        b = c
        
    return False
    
x = int(input())
while sumFib(x):
    x+=1
print(x)
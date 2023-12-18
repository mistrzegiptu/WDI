def isPrime(n):
    if n < 2 or n % 2 == 0:
        return False
    if n == 2:
        return True
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True
def F(A, B, num = 0):
    if A == B == 0:
        if isPrime(num):
            print(num)
        return
    if A > 0:
        F(A-1, B, 2*num+1)
    if B > 0:
        F(A, B-1, 2*num)

def f(A, B, num = 0):
    if A == B == 0:
        return 1 if isPrime(num) else 0
    res = 0
    if A > 0:
        res += f(A-1, B, 2*num+1)
    if B > 0:
        res += f(A, B-1, 2*num)
    return res

a, b = 3, 3
print(f(a, b))
F(a, b)
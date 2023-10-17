def isPrime(n):
    if n<2 or n%2==0: return False
    if n==2: return True
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
x = 1
while x <= 30:
    if isPrime((2**x)-1):
        print(((2**x)-1)*2**(x-1))
    x += 1
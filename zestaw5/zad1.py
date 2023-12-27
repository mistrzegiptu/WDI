from math import log10

def isPrime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
def getNum(n, mask):
    num = 0
    while n > 0:
        if mask%2 == 1:
            num = num * 10 + n%10
        n = n // 10
        mask = mask // 2
    reverse = 0
    while num > 0:
        reverse = reverse * 10 + num % 10
        num = num // 10
    
    return reverse

def isPowerOfTwo(n):
    i = 1
    while i <= n:
        if i == n:
            return True
        i *= 2

    return False

def function(n):
    def recursion(n, mask):
        newNum  = getNum(n, mask)
        if isPrime(newNum) and not isPowerOfTwo(mask):
            print(newNum)
        if mask < 2**(int(log10(n))+1):
            recursion(n, mask+1)

    recursion(n, 3)

function(3717)
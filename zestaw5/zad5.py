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

def decimal(bin):
    n = 0
    for i in range(len(bin)):
        if bin[i] == 1:
            n += 2 ** (len(bin)-i-1)
    return n

def function(T):
    def rek(T, i, j):
        n = len(T)
        if j > n-1:
            return False
        if j == n-1:
            if T[j-1] == 0 and j-i+1 != 2:
                return False
            return isPrime(decimal(T[i:j+1]))
        if isPrime(decimal(T[i:j+1])):
            return rek(T, j+1, j+2)
        return rek(T, i, j+1)
    
    return rek(T, 0, 1) if len(T) > 1 else False

T = [1,1,1,0,1,1]
print(function(T))
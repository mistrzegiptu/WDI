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

def function(a, b):
    aLen = int(log10(a)) + 1
    bLen = int(log10(b)) + 1
    aSplit = [0 for _ in range(aLen)]
    bSplit = [0 for _ in range(bLen)]
    i = aLen - 1
    while a > 0:
        aSplit[i] = a % 10
        a = a // 10
        i -= 1
    i = bLen - 1
    while b > 0:
        bSplit[i] = b % 10
        b = b // 10
        i -= 1

    primeCounter = 0

    def rek(i=0, j=0, num=0):
        nonlocal primeCounter
        if i == aLen and j == bLen:
            if isPrime(num):
                print(num)
                primeCounter += 1
            return
        if i < aLen:
            rek(i+1, j, num*10+aSplit[i])
        if j < bLen:
            rek(i, j+1, num*10+bSplit[j])
    
    rek(0, 0, 0)
    print(primeCounter)

function(123, 74)
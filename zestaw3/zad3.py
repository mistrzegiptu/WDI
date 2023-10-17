from math import isqrt
def sito(n):
    primes = [True for _ in range(n+1)]
    primes[0] = primes[1] = False
    
    for i in range(2, isqrt(n)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    
    for i in range(0, n+1):
        if primes[i]:
            print(i)
    return primes

num = int(input())
sito(num)
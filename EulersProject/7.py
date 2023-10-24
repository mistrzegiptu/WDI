from math import isqrt

def sito(n):
    primes = [True for _ in range(n+1)]
    primes[0] = primes[1] = False
    
    for i in range(2, isqrt(n)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    
    cnt = 0
    for k in range(2, n+1):
        if primes[k]:
            cnt += 1
            if cnt == 10001:
                print(k)
                return k

sito(1000000)
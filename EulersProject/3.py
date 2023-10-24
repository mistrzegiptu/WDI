def isPrime(l):
    if l < 2 or l%2 == 0:
        return False
    if l == 2:
        return True
    i = 3
    while i*i <= l:
        if l % i == 0:
            return False
        i += 2
    return True

n = 600851475143

i = 2
while i*i<=n:
    if n%i == 0 and isPrime(i):
        print(i)
    i += 1
def isPrime(n):
    if n < 2 or n%2 == 0:
        return False
    if n == 2:
        return True
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True
    
def nLen(n):
    counter = 0
    while n > 0:
        counter += 1
        n = n//10
    
    return counter

def bitLen(n):
    counter = 0
    while n > 0:
        counter += n % 2
        n = n // 2
    
    return counter
    

a = 123
b = 75
primes = 0
aLength = nLen(a)
bLength = nLen(b)

for i in range(1, 2**(nLen(a)+nLen(b))):
    a2 = a
    b2 = b
    if(bitLen(i) == nLen(a)):
        suma = 0
        for j in range(0, aLength + bLength):
            if i % 2 == 0:
                suma += (b2%10)*10**j
                b2 = b2 // 10
            else:
                suma += (a2%10)*10**j
                a2 = a2 // 10
            i = i // 2
        if(isPrime(suma)):
            primes += 1

print(primes)
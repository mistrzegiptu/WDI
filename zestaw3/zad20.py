t = [2,23,33,35,7,4,6,7,5,11,13,22]

def factorial(n):
    factors = []
    i = 2
    while i <= n:
        if n%i == 0:
          factors.append(i)
          while n%i == 0:
            n = n//i
            
        i += 1
        
    return factors
    
def isDivisible(n, T):
    for x in T:
        if n%x == 0:
            return True
    
    return False

def unicalPrimes(T):
    n = len(T)
    maxLen = 0
    
    for i in range(n):
        product = 1
        counter = 0
        while i < n:
            if isDivisible(product, factorial(T[i])):
                break
            product *= T[i]
            counter += 1
            i += 1
            
        maxLen = max(maxLen, counter)
        
    return maxLen
    
print(unicalPrimes(t))
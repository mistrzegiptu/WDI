t1 = [1,2,3,4]
t2 = [9,7,4,8]
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

def primeSums(t1, t2):
    n = len(t1)
    counter = 0
    
    for i in range(2**n):
        sum = 0
        for j in range(n):
            if i % 2 == 0:
                sum += t1[j]
            else:
                sum += t2[j]
            
            i = i // 2
            
        if isPrime(sum):
            print(sum)
            counter += 1
        
    return counter

primeSums(t1,t2)
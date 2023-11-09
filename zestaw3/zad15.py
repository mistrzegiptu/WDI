t = [1,4,6,5,3,10,5,7,8]

def isPrime(n):
    if n < 2 or n % 2 == 0:
        return False
    if n == 2:
        return True
        
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i+=2
        
    return True
    
def isComposite(n):
    return (not isPrime(n)) and n != 1
    
oneComposite = False
n = len(t)
a = 1
b = 1

for i in range(n):
    if i > b:
        c = a
        a += b
        b = c
    if i == b:
        if not isComposite(t[i]):
            print(False)
            exit()
    else:
        if isPrime(t[i]):
            oneComposite = True
            
print(oneComposite)
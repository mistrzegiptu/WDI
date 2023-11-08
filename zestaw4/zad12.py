from random import *

def isComposite(n):
    if n == 1 or n == 2: 
        return 0
    
    i = 2
    while i*i <= n:
        if n % i == 0:
            return True
        i += 1
        
    return False
    
def plaster(T):
    n = len(T)
    L = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            L[i][j] = isComposite(T[i][j])
            
    
    counter = 0
    
    for i in range(1, n-1):
        for j in range(1, n-1):
            li = -L[i][j]
            
            for i1 in range(i-1, i+2):
                for j1 in range(j-1, j+2):
                    li += L[i1][j1]
                    
            if li >= 6:
                counter += 1
                
    return counter
        
def main(T):
    n = len(T)
    first = plaster(T[0])
    
    for i in range(1, n):
        if plaster(T[i]) != first:
            return False
            
    return True
    
x = 3
tab = [[[randint(1, 1000) for _ in range(x)] for _ in range(x)] for _ in range(x)]
print(tab)
print(main(tab))
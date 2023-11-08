from random import *

def onlyOddDigit(n):
    
    while n > 0:
        if (n % 10) % 2 == 0:
            return False
        n = n // 10
        
    return True
    
N = int(input())

t = [randint(1, 1000) for _ in range(N)]

for i in range(N):
    if onlyOddDigit(t[i]):
        print(t[i], True)
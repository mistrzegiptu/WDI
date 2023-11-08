from random import *

def oddDigit(n):
    
    while n > 0:
        if (n % 10) % 2 == 1:
            return True
        n = n // 10
        
    return False
    
N = int(input())

t = [randint(1, 1000) for _ in range(N)]

for i in range(N):
    if not oddDigit(t[i]):
        print(t[i], False)
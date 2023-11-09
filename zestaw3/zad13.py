from random import *

n = 15
t = [randrange(1,10) for _ in range(n)]
maxLen = 0
i = 0

for i in range(n-1):
    for j in range(n-1, 0, -1):
        length = 0
        while t[i] == t[j]:
            length += 1
            if i == n-1 or j == 0:
                break
            i += 1
            j -= 1
        
        maxLen = max(maxLen, length)
        
print(t)
print(maxLen)
        
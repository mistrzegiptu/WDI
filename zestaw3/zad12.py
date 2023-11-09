from random import *

N = int(input())
t = [randrange(1, 99, 2) for _ in range(N)]

longestPositive = 0
longestNegative = 0

for i in range(N-1):
    j = i
    length = 1
    r = t[j+1] - t[j]
    while j < N-1:
        if t[j+1]-t[j] != r:
            break
        length += 1
        j += 1
    if r > 0:
        longestPositive = max(length, longestPositive)
    else:
        longestNegative = max(length, longestNegative)
    
print(longestPositive-longestNegative)
from random import randint

def minCost(T, k):
    minSum = 10**10
    def f(T, k, w = 0, sum = 0):
        nonlocal minSum
        n = len(T)
        if w == n-1:
            minSum = min(minSum, sum)
        else:
            if k != 0:
                f(T, k-1, w+1, sum+T[w+1][k-1])
            if k != n-1:
                f(T, k+1, w+1, sum+T[w+1][k-1])
            
            f(T, k, w+1, sum+T[w+1][k-1])
    
    f(T, k, sum=T[0][k])
    return minSum
### FOR TESTING
T = [[randint(1, 3) for _ in range(8)] for _ in range(8)]
for i in range(8):
    for j in range(8):
        print(T[i][j], end=' ')
    print()

print(minCost(T, 0))
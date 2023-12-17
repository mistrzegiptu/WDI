T = [[random() for _ in range(8)] for _ in range(8)]
for i in range(8):
    for j in range(8):
        print(T[i][j], end=" ")
    print()
def minCost(T):
    minSum = float(inf)
    def f(T, k, w = 0, sum = 0):
        n = len(T)
        if w == n-1:
            nonlocal minSum = min(nonlocal minSum, sum)
        else:
            if k != 0:
                f(T, k-1, w+1, sum+T[w+1][k-1])
            if k != n-1:
                f(T, k+1, w+1, sum+T[w+1][k-1])
            
            f(T, k, w+1, sum+T[w+1][k-1])
    
    f(T, k, suma=T[0][k])
    return minSum

print(minCost(T))
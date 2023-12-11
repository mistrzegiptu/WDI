def minCost(T):
    nonlocal minSum
    def f(T, k, w = 0, sum = 0):
        n = len(T)
        if w == n-1:
            minSum = min(minSum, sum)
        else:
            if k != 0:
                f(T, k-1, w+1, sum+T[w+1][k-1])
            if k != n-1:
                f(T, k+1, w+1, sum+T[w+1][k-1])
            
            f(T, k, w+1, sum+T[w+1][k-1])
    
    f(T, k, suma=T[0][k])